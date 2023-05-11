"""
Calculate the similarity of two images.

[Install scikit-image]
!python -m pip install -U scikit-image
"""

import os
import cv2
from tqdm import tqdm
from skimage.metrics import structural_similarity as image_similarity

test_case = r'D:\SimilarityOfImages\Datasets\test_case_2'
images_path = os.path.join(test_case, 'Source')
DB_images = os.path.join(test_case, 'DB')

result = os.path.join(test_case, 'Result')

if not os.path.exists(result):
    os.mkdir(result)

images_name = os.listdir(images_path)
DBs = os.listdir(DB_images)

images = [cv2.cvtColor(cv2.imread(os.path.join(images_path, img)), cv2.COLOR_BGR2GRAY) for img in images_name]
DBs = [cv2.cvtColor(cv2.imread(os.path.join(DB_images, img)), cv2.COLOR_BGR2GRAY)  for img in DBs]

def similarity_of_images(image, DB):

    def similarity_two_images(img1, img2):

        # Detect keypoints and extract features
        sift = cv2.SIFT_create()
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)

        # Match the features
        bf = cv2.FlannBasedMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        # Apply Lowe's ratio test to filter good matches
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)

        if len(good_matches) >=800:
            return len(good_matches), True, img1
        
        else:
            return 0, False, img1
        
    imagesSims = [similarity_two_images(imgDB, image ) for imgDB in tqdm(DB)]

    return imagesSims

for i in tqdm(range(len(images))):

    img = images[i]
    
    result_image_path = os.path.join(result, images_name[i][:-4])
    if not os.path.exists(result_image_path):
        os.mkdir(result_image_path)
      
    images_similarity = similarity_of_images(cv2.resize(img, (1280, 1280)), DBs)
    images_similarity = sorted(images_similarity, key=lambda x: x[0], reverse=True)

    minS = images_similarity[-1][0]+0.00001
    maxS = images_similarity[0][0]

    simIndex = 0

    for img2 in images_similarity[:3]:

        sim = img2[0]

        score = (sim-minS)/(maxS-minS)
        img2 = cv2.resize(img2[2], (640, 640))
        img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
        cv2.imwrite(os.path.join(result_image_path, f'{DB_images}-{score}.jpg'), img2)

        simIndex+=1