![image](https://github.com/user-attachments/assets/2afe6782-1c62-4703-8392-e27e5462e13a)

Cancer is one of the leading causes of human morbidity and mortality worldwide and we want to find new ways to detect it.AI is changing how we do clinical diagnosis of tumors. In this paper, when A.I. The study shows how important it is to use deep learning models like CNN to look at tons of image 
data.Using clever techniques including record enhancement, switch detection and model tweaking, this study seeks to improve the accuracy and speed of analysis It also looks at issues related to the use of AI in hospitals, a knowledge of how AI makes choices is included and It also ensures a good match 
between data and how doctors have already created the model.

![image](https://github.com/user-attachments/assets/a1e8dbd4-b510-4836-8f0d-231108825047)


Import libraries:-
With Fast ai, the code begins via uploading the important libraries to set up a gadget getting to know 

environment:

Fastai: An incredible library built on pinnacle of PyTorch that simplifies the education of neurons.
Create an information set:-
Path definition: The code specifies the listing of the facts set. It is important to make sure that the path is 
accurate so that the version can access the snap shots. 
Types: Two classes are described for the type of venture: ‘no’ (indicating no tumor) and ‘yes’ 
(indicating tumor).
This binary segmentation problem is common in medical imaging.
DataBlockcreation:-
Blocks: The code specifies that the data consists of images (ImageBlock) and their corresponding 
categories (CategoryBlock). 
Obtaining Resources: The function get_image_files is used to retrieve an image document from the 
desired path. 
Splitter: The RandomSplitter feature is used to randomly break up the data set into training and 
validation units, wherein 20% of the records is saved for validation. This allows the overall performance 
of the model to be checked on unseen data.
Data Enhancement Progress:-
Squish Method: The code resizes the photos with the use of the "Squish" approach, which changes the 
decision at the same time as keeping the factor ratio the sameThis facilitates keeping the photographs 
constant. 
Random Resized Crop: The code makes use of random cropping, permitting the version to examine from 
different parts of the picture. This approach enables us to prevent overfitting through introducing 
changes to the schooling information.


Model construction and schooling:-

CNN Learner: Convolutional neural network learner is constructed using ResNet architecture (first 
ResNet18, then ResNet34). ResNet algorithms are known to carry out properly in photo classification 
obligations because of the residual connectivity.
Fine-tuning: The model is being fine-tuned in multiple stages (in this case 5). Micro-tuning is a method 
of continuously training a previously trained model on new data, allowing the model to adapt to the 
specific characteristics of the new data
1. Sample Analysis:
Confusion matrix: Once trained, the code generates a confusion matrix to visualize the performance 
of the model. The uncertainty matrix shows true positives, false positives, true negatives, and false 
negatives, and allows a detailed analysis of the predictions in the model
2. Sample storage:
The trained model is exported and stored as a Pk report. This permits for destiny programs without 
having to retrain the version, making it less difficult to apply.
3. Account and User Interface:
Loading models: The saved version is loaded for calculations on a brand-new version. The 
load_learner feature is used to load the version from a saved file.
