import os
import random
import sys


xml_path = 'Dataset/Annotations/'
dest = 'Dataset/Image‡Sets/Main/'

if not os.path.exists(dest):
    os.makedirs(dest)

trainval_percent = 0.9
train_percent = 0.8
total_xml = os.listdir(xml_path)
num = len(total_xml)
l = range(num)
tv = int(num * trainval_percent)
tr = int(num * train_percent)
trainval = random.sample(l, tv)
train = random.sample(trainval, tr)

print("Train and Val size: ", tv)
print("Train size: ", tr)

ftrainval = open(dest + 'trainval.txt', 'w')
ftest = open(dest + 'test.txt', 'w')
ftrain = open(dest + 'train.txt', 'w')
fval = open(dest + 'val.txt', 'w')


for i in l:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()