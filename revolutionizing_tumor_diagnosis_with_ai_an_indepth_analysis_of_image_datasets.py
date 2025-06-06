# -*- coding: utf-8 -*-
"""Revolutionizing Tumor Diagnosis with AI: An InDepth Analysis of Image Datasets

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18aLwMdoo2fWrYIyfjmFCdxAwv4paiKX3
"""

import os
import sys
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from urllib.parse import unquote, urlparse
from urllib.error import HTTPError
from zipfile import ZipFile
import tarfile
import shutil

CHUNK_SIZE = 40960
DATA_SOURCE_MAPPING = 'brain-mri-images-for-brain-tumor-detection:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-data-sets%2F165566%2F377107%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20240926%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20240926T055126Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3Dbdf62f44eb0785ab88e5dac6344fdbf3175bbfc7336562e1557bad3d72e7fa8f24eb970bbbb6f47e90fd1004b083efba04767e3086834f8505d6f217dfb02c458e654a73fa6cea20abc47268ce409fc2b301091ec699377d39fb08868c1198f71125a45e78f5304999f7da4736bfa0a241078c204c6c7c8aaaa1b59f5f3a22a2e3eeddf1e83c5559670aca1a51ddce90c7cc342bf440cb01010a4dccb035c6a7589b43bf2b6403e7303717b2b94bafd41f0dfabd34b0a8a0e441071ef1770af938f61d02a1a1b6fb4356f85d92b70ba9677ee3e4e5f324be89895e73ca2760a40f7172c4ba0aac8bdf73ff70ef8fa44a3a9eb1cf12f3a54458580e91c27dbd3b'

KAGGLE_INPUT_PATH='/kaggle/input'
KAGGLE_WORKING_PATH='/kaggle/working'
KAGGLE_SYMLINK='kaggle'

!umount /kaggle/input/ 2> /dev/null
shutil.rmtree('/kaggle/input', ignore_errors=True)
os.makedirs(KAGGLE_INPUT_PATH, 0o777, exist_ok=True)
os.makedirs(KAGGLE_WORKING_PATH, 0o777, exist_ok=True)

try:
  os.symlink(KAGGLE_INPUT_PATH, os.path.join("..", 'input'), target_is_directory=True)
except FileExistsError:
  pass
try:
  os.symlink(KAGGLE_WORKING_PATH, os.path.join("..", 'working'), target_is_directory=True)
except FileExistsError:
  pass

for data_source_mapping in DATA_SOURCE_MAPPING.split(','):
    directory, download_url_encoded = data_source_mapping.split(':')
    download_url = unquote(download_url_encoded)
    filename = urlparse(download_url).path
    destination_path = os.path.join(KAGGLE_INPUT_PATH, directory)
    try:
        with urlopen(download_url) as fileres, NamedTemporaryFile() as tfile:
            total_length = fileres.headers['content-length']
            print(f'Downloading {directory}, {total_length} bytes compressed')
            dl = 0
            data = fileres.read(CHUNK_SIZE)
            while len(data) > 0:
                dl += len(data)
                tfile.write(data)
                done = int(50 * dl / int(total_length))
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {dl} bytes downloaded")
                sys.stdout.flush()
                data = fileres.read(CHUNK_SIZE)
            if filename.endswith('.zip'):
              with ZipFile(tfile) as zfile:
                zfile.extractall(destination_path)
            else:
              with tarfile.open(tfile.name) as tarfile:
                tarfile.extractall(destination_path)
            print(f'\nDownloaded and uncompressed: {directory}')
    except HTTPError as e:
        print(f'Failed to load (likely expired) {download_url} to path {destination_path}')
        continue
    except OSError as e:
        print(f'Failed to load {download_url} to path {destination_path}')
        continue

print('Data source import complete.')

"""#  🎡 Brain MRI Images for Brain Tumor Detection

![image.png](attachment:1eef094e-452c-4a43-9958-58d60157c785.png)

# Import Libraries
"""

!pip install -Uqq fastbook
import fastbook

import warnings
warnings.filterwarnings('ignore')

from fastbook import *

"""# Dataset"""

path = Path('../input/brain-mri-images-for-brain-tumor-detection')

"""### 👉 How many categories in our dataset"""

Object_types = 'no','yes'

"""### 📒 Creating DataBlock"""

Object_types = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))

from google.colab import drive
drive.mount('/content/drive')

dls = Object_types.dataloaders("/content/drive/MyDrive/Tumor Dataset 2")

"""## We see our dataset images 🙌👍"""

dls.valid.show_batch(max_n=8, nrows=2)

"""# Squish method
#### 👉 We resize our datasets by using **Squish method** and making all the same size
"""

Object_types = Object_types.new(item_tfms=Resize(128, ResizeMethod.Squish))
dls = Object_types.dataloaders("/content/drive/MyDrive/Tumor Dataset 2")
dls.valid.show_batch(max_n=8, nrows=2)

"""# Random Resize Crop
#### Here we are **crop our images from different angles** and we take randam parts of same image
#### This will help us to avoid the overfitting 🤴
"""

from pathlib import Path

path = Path("/content/drive/MyDrive/Tumor Dataset 2")

# Check subfolders
subfolders = [f for f in path.ls() if f.is_dir()]
print(f"Subfolders (classes) found: {[f.name for f in subfolders]}")

# Count images inside each subfolder
for folder in subfolders:
    images = list(folder.glob("*.jpg"))
    print(f"{folder.name}: {len(images)} image(s)")

from fastai.vision.all import *

path = Path("/content/drive/MyDrive/Tumor Dataset 2")

Object_types = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=RandomResizedCrop(128, min_scale=0.3),
    batch_tfms=aug_transforms()
)

dls = Object_types.dataloaders(path, bs=64)

dls.train.show_batch(max_n=8, nrows=2, unique=True)

from fastai.vision.all import *

Object_types = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=RandomResizedCrop(128, min_scale=0.3),
    batch_tfms=aug_transforms()
)

path = "/content/drive/MyDrive/Tumor Dataset 2"
dls = Object_types.dataloaders(path, bs=64)
dls.train.show_batch(max_n=8, nrows=2, unique=True)

"""The batch size is by default bs = 64. you can change that value for a lower one, it will also work.
when bs = 64 is not working

dls = Object_types.dataloaders(path,bs=5)

#### Now our dataset is ready for training     
# resnet18 (NNs)
##### We are using **accuracy matrix** there are other matrices also you can check official fastai documentation
"""

learn = cnn_learner(dls, resnet18, metrics=accuracy)
learn.fine_tune(5)

"""# 📌 Confusion_matrix"""

interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()

"""## resnet34"""

learn1 = cnn_learner(dls, resnet34, metrics=accuracy)
learn1.fine_tune(5)

interp = ClassificationInterpretation.from_learner(learn1)
interp.plot_confusion_matrix()

"""#### ~~ 👉 Not much improvement in using resnet34.      
#### ~~ 👍 It predict 10 false values and resnet18 predict 11. (Almost)          
#### ~~ 👉 look at both confusion matrices.  
### ~~ 👉 But its a **worth try**.

# Most wrong prediction
### ~ Or our model not understand or confused in showing results             
### ~ Only one image which is yes but model predict no
"""

interp.plot_top_losses(4, nrows=1)

from fastai.vision.widgets import *

"""# Save our Model"""

learn.export()

path = Path()
path.ls(file_exts='.pkl')

learn_inf = load_learner(path/'export.pkl')

"""### Check how model working"""

learn_inf.predict('/content/drive/MyDrive/Tumor Dataset 2/Tumor/G_86_HF_.jpg')

learn_inf.dls.vocab

"""# Creating 📱 App from the Model

"""

btn_upload = widgets.FileUpload()
btn_upload

btn_upload = SimpleNamespace(data = ['/content/drive/MyDrive/Tumor Dataset 2/Tumor/G_86_HF_.jpg'])

img = PILImage.create(btn_upload.data[-1])

out_pl = widgets.Output()
out_pl.clear_output()
with out_pl: display(img.to_thumb(128,128))
out_pl

pred,pred_idx,probs = learn_inf.predict(img)

lbl_pred = widgets.Label()
lbl_pred.value = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'
lbl_pred

btn_run = widgets.Button(description='Classify')
btn_run

def on_click_classify(change):
 img = PILImage.create(btn_upload.data[-1])
 out_pl.clear_output()
 with out_pl: display(img.to_thumb(128,128))
 pred,pred_idx,probs = learn_inf.predict(img)
 lbl_pred.value = f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}'
btn_run.on_click(on_click_classify)

btn_upload = widgets.FileUpload()
btn_upload

"""### App is working congratulations 🎉🎉"""

VBox([widgets.Label('Select your image!'),
      btn_upload, btn_run, out_pl, lbl_pred])