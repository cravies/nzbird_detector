# 🦜 nzbird_detector 🦜
Detect NZ bird species in photos using YOLOv3 or v7.
<br></br>
See "tech_report.pdf" for theoretical documentation.
<br></br>
"slides.pdf" contains slides for an explanation of object detection, CNNs, and YOLO.

https://user-images.githubusercontent.com/95381252/197306200-b7d074d6-a21c-46dc-a082-eadf80ba2b06.mp4

# Basic Explanation
- I used the pretrained YOLO models as they are state of the art for object detection and they are easy to train on a custom problem
- The main problem is making a pipeline where you can efficiently scrape and label data
- The models take about 1000 labeled images for each class
- Thus I wrote a pipeline to scrape data on select birds from <a href="https://www.macaulaylibrary.org">Macaulay Library</a> (bird db), label that data, and perform augmentation to increase the dataset size
- This pipeline works with any bird species (not just NZ birds), you just need to download csv files of your species from <a href="https://www.macaulaylibrary.org">Macaulay db</a>. (This requires an account).
- I trained the model on google colab pro, so the script is written to use this environment, grabbing the training files from my google drive. If you train it off of colab you will have to change the script to point to your own local data directory.
- To get good results you may have to tweak the conf_thresh and iou_thresh hyperparameters: these are command line arguments that represent two different types of confidence threshold the model has to reach before it will predict a "hit".

# Downloading, augmenting and labelling data

- First download OpenLabelling
```bash
git clone https://github.com/Cartucho/OpenLabeling
```
- Now move the files from /label/ into the OpenLabeling repo /OpenLabeling/main
- Get the csv of birds you want to scrape and download from the <a href="https://www.macaulaylibrary.org">Macaulay library.</a>
- There are already some example csvs in the repository if you want to know what they look like.
- You have to make an account to download big csvs with hundreds of birds, which YOLO needs to work.
- Edit the download_birds.py to include these csvs.
- Now to download those bird images run 
```bash
make all
```
- This downloads the files, splits them into train,test,val folders, and runs augmentation 
to increase the size of the dataset. 
- Now we move them to the OpenLabelling directory
```
make move
```
- Now change to the openlabelling directory and label some training images with OpenLabelling 
```
make tr
```
- Label testing images with
```
make te
```
- Label validation images with
```
make v
```

# Training model (assumes you are using colab. If not, just change the dataset location in script)
- Download either of the .ipynb files (v3 or v7)
- Upload this file to colab to run
- Compress your train,test,val folders (including "out" label folders) in a folder called 'bird_data'. Upload it to your google drive
- Note: the train folder will need to be compressed otherwise it will be too large.
- Put the train and train_out folders into a zip folder named 'trains' inside 'bird_data'
- Run all in the ipynb. It should take 2+ hours to train(with premium) more with free colab
- Note: colab will need permission to grab the data from your drive
- You can see the saved results on video and image tests in your drive

Note: 
The results of the model is quite dependent on the hyperparameters conf_thresh (confidence bounding box threshold).
Setting a lower confidence threshold makes the model more sensitive and leads to false positives. 
Conversely, setting a high confidence threshold makes the model insensitive and leads to false negatives.
To get good results before deploying,you should tweak this hyperparameter.
The best value will depend on the type of data you input. When the model runs it outputs a ROC curve that shows you false positive/ negative rates at different confidence thresholds. You can use the optimal value as the default if you don't feel like tweaking it for different scenarios.
