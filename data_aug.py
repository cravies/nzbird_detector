#!/usr/bin/env python3

from PIL import Image
import numpy as np
import albumentations as A
import os
import splitfolders

"""
This file performs data augmentation to increase 
training data size.
It then splits the input file into train,test,validation
dataset.
"""

# Define augmentation pipeline
transform = A.Compose([
        A.RandomRotate90(),
        A.Flip(),
        A.Transpose(),
        A.OneOf([
            A.GaussNoise(),
        ], p=0.2),
        A.OneOf([
            A.MotionBlur(p=.2),
            A.MedianBlur(blur_limit=3, p=0.1),
            A.Blur(blur_limit=3, p=0.1),
        ], p=0.2),
        A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.2),
        A.OneOf([
            A.OpticalDistortion(p=0.3),
            A.GridDistortion(p=.1),
            A.Affine(p=0.3),
        ], p=0.2),
        A.OneOf([
            A.CLAHE(clip_limit=2),
            A.Sharpen(),
            A.Emboss(),
            A.RandomBrightnessContrast(),            
        ], p=0.3),
        A.HueSaturationValue(p=0.3),
])

def dupes():
    """
    Just double checking if train test val have any overlapping files
    """
    folds = ["./train/kea","./test/kea","./val/kea"]
    files=[]
    for folder in folds:
        files.append(os.listdir(folder))
    res = []
    for folder in files:
        for file in folder:
            res.append(file)
    #check if any files appear twice
    import collections
    print("duplicates: ",
        [item for item,count in collections.Counter(res).items() if count > 1]
    )

def data_aug(name,FROM,TO):
    """
    Perform data augmentation on images files in
    FROM, the input folder and output the images in 
    TO, the output folder.
    in format name_i.png where i is an int
    """
    
    #items already in augmented dir
    target_dir = os.listdir(TO)
    
    #enumerate over images
    for i,img in enumerate(os.listdir(FROM)):
        name = f'{FROM}/{img}'
        image = Image.open(name)
        image = np.asarray(image)
        #transform image
        transformed = transform(image=image)
        image = transformed["image"]
        image = Image.fromarray(image)
        savename = f'{TO}/{bird}_{img}_aug.png'
        if savename not in target_dir:
            #avoid saving duplicates
            image.save(savename)

if __name__=="__main__":
    #lets run data augmentation on all our birds
    for bird in ['kea','takahe','tui']:
        data_aug(bird,f'./input/{bird}',f'./input/{bird}_aug')
    #train test split
    # split into train, val, test folders
    splitfolders.ratio(
        "./input",
        output="./",
        seed=1337,
        ratio=(0.9,0.05,0.05)
    )
    dupes()
