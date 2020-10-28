const fs = require('fs')

var augment = function(){
    path="standalones/"
    fs.readdir(path, (err, files) => {
        if (err) console.error(err);
        files.forEach(img => {
            console.log(img)
        })
    })
    //loop through pictures directory
    //augment images in directory
    //save new images in /augmented
    //empty standalones directory
}

var generateCanva = function(qt, zlevel){
    // random selection of pollen in /augmented
    // create gray image 961x626 
    // add noise to image
    //random positioning of pollens on the image
}

augment()