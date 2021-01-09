import torch.utils.data
from ssd.structures.container import Container
import numpy as np
import os
import xml.etree.ElementTree as ET
from PIL import Image

class VOCDataset(torch.utils.data.Dataset):
    class_names = ('background',
                    "abatia_canescens", "abelia_grandiflora", "abelia_rupestris",
                    "abies_cilicica", "acacia_pennata", "acacia_perryi", "adenia_perrieri",
                    "allophylus_comorensis", "ceratopteris_cornuta", "chilopsis_linearis",
                    "cleome_dumosa", "colignonia_rufopilosa", "euphorbia_orthoclada",
                    "gratiola_officinalis", "mibora_minima", "mutisia_andersonii",
                    "plantago_lanceolata", "tristerix_grandiflorus", "turpinia_occidentalis",
                    "vaccinium_secundiflorum", "vernonia_mandrarensis", "weberbauera_spathulifolia",
                    "weigela_florida", "wisteria_sinensis", "woodwardia_radicans",
                    "xyloolaena_richardii", "zelkova_schneideriana", "ziziphus_jujuba")
    
    def __init__(self, data_dir, split, transform=None, target_transform=None):
        self.data_dir = data_dir
        self.split = split
        self.transform = transform
        self.target_transform = target_transform
        image_sets_file = os.path.join(self.data_dir, "ImageSets", "Main", "%s.txt" % self.split)
        self.ids = VOCDataset._read_image_ids(image_sets_file)
        self.class_dict = {class_name: i for i, class_name in enumerate(self.class_names)}
    
    def __getitem__(self, index):
        image_id = self.ids[index]
        boxes, labels = self._get_annotation(image_id)
        image = self._read_image(image_id)
        if self.transform:
            image, boxes, labels = self.transform(image, boxes, labels)
        if self.target_transform:
            boxes, labels = self.target_transform(boxes, labels)
        targets = Container(
            boxes=boxes,
            labels=labels,
        )
        return image, targets, index
    
    def get_annotation(self, index):
        image_id = self.ids[index]
        return image_id, self._get_annotation(image_id)

    def __len__(self):
        return len(self.ids)

    @staticmethod
    def _read_image_ids(image_sets_file):
        ids = []
        with open(image_sets_file) as f:
            for line in f:
                ids.append(line.rstrip())
        return ids
    
    def _get_annotation(self, image_id):
        annotation_file = os.path.join(self.data_dir, "Annotations", "%s.xml" % image_id)
        objects = ET.parse(annotation_file).findall("object")
        boxes = []
        labels = []
        
        for obj in objects:
            class_name = obj.find('name').text.lower().strip()
            bbox = obj.find('bndbox')
            x1 = float(bbox.find('xmin').text) - 1
            y1 = float(bbox.find('ymin').text) - 1
            x2 = float(bbox.find('xmax').text) - 1
            y2 = float(bbox.find('ymax').text) - 1
            boxes.append([x1, y1, x2, y2])
            labels.append(self.class_dict[class_name])
        
        return (np.array(boxes, dtype=np.float32),
                np.array(labels, dtype=np.int64))
        
    def get_img_info(self, index):
        img_id = self.ids[index]
        annotation_file = os.path.join(self.data_dir, "Annotations", "%s.xml" % img_id)
        anno = ET.parse(annotation_file).getroot()
        size = anno.find("size")
        im_info = tuple(map(int, (size.find("height").text, size.find("width").text)))
        return {"height": im_info[0], "width": im_info[1]}

    def _read_image(self, image_id):
        image_file = os.path.join(self.data_dir, "JPEGImages", "%s.jpg" % image_id)
        image = Image.open(image_file).convert("RGB")
        image = np.array(image)
        return image