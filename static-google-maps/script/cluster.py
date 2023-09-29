import sys
import os
import math
import numpy as np

from shutil import copyfile
from img2vec_pytorch import Img2Vec
from PIL import Image

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

import time
start_time = time.time()
"""
    This example groups the images from test_images folder into k_value (default: 2) categories, and copies them into separate folders.
    For cats and dogs you should end up with a folder of cats and a folder of dogs.

    It uses Img2Vec to get the image vector, then applies PCA for dimensionality reduction and KNN for clustering.
"""

input_path = './DB'
files = os.listdir(input_path)

img2vec = Img2Vec(model='resnet101')
vec_length = 2048  # Using resnet-18 as default

samples = len(files)  # Amount of samples to take from input path

# Matrix to hold the image vectors
vec_mat = np.zeros((samples, vec_length))

# If samples is < the number of files in the folder, we sample them randomly
sample_indices = np.random.choice(range(0, len(files)), size=samples, replace=False)

for index, i in enumerate(sample_indices):
    file = files[i]
    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename)).convert('RGB')
    vec = img2vec.get_vec(img)
    vec_mat[index, :] = vec

pca_model = PCA(n_components=2)
pca_model.fit(vec_mat)

db_vec = pca_model.transform(vec_mat)

source =  Image.open('./source/YUN_0081.JPG').convert('RGB')
source_vec = img2vec.get_vec(source)
source_vec = pca_model.transform([source_vec])

mindr = 1e9
best_indx = -1
min_distance = 50

for index, i in enumerate(sample_indices):

    p1 = db_vec[index, :]
    p2 = source_vec[0]
    dr = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    if dr<=min_distance:
        if dr<mindr:
            mindr = dr
            best_indx = i

if best_indx != -1:
    
    file = files[best_indx]
    filename = os.fsdecode(file)
    copyfile(input_path + '/' + filename, './' + 'source/' + filename)

end_time = time.time()
duration = round(end_time - start_time, 3)
file_name = os.path.splitext(filename)[0]
print({"coords":file_name,
       "time": f"{duration} second"})