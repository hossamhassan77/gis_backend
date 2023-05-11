"""
Calculate the similarity of two images.

[Install scikit-image]
!python -m pip install -U scikit-image
"""

import os
import cv2
from tqdm import tqdm
from skimage.metrics import structural_similarity as image_similarity
from pydantic import BaseModel

class Similarity():

    def create_result_folder(source_path, db_path):
        result = os.path.join(source_path, '..\Result')
        if not os.path.exists(result):
            os.mkdir(result)
        images_name = os.listdir(source_path)
        DBs = os.listdir(db_path)
        images = [cv2.cvtColor(cv2.imread(os.path.join(source_path, img)), cv2.COLOR_BGR2GRAY) for img in images_name]
        DBs = [cv2.cvtColor(cv2.imread(os.path.join(db_path, img)), cv2.COLOR_BGR2GRAY)  for img in DBs]
        return images, DBs, result, images_name

    # images, DBs, result, images_name = create_result_folder(source_path, db_path)

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

            if len(good_matches) >=100:
                return len(good_matches), True, img1
            
            else:
                return 0, False, img1
            
        imagesSims = [similarity_two_images(imgDB, image ) for imgDB in tqdm(DB)]

        return imagesSims
    
    def get_similarity(images, result, images_name, DBs):
        for i in tqdm(range(len(images))):

            img = images[i]
            
            result_image_path = os.path.join(result, images_name[i][:-4])
            if not os.path.exists(result_image_path):
                os.mkdir(result_image_path)
            
            images_similarity = Similarity.similarity_of_images(cv2.resize(img, (1280, 1280)), DBs)
            images_similarity = sorted(images_similarity, key=lambda x: x[0], reverse=True)

            minS = images_similarity[-1][0]+0.00001
            maxS = images_similarity[0][0]

            simIndex = 0

            for img2 in images_similarity[:3]:

                sim = img2[0]

                score = (sim-minS)/(maxS-minS)
                img2 = cv2.resize(img2[2], (1280,1280))
                img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
                cv2.imwrite(os.path.join(result_image_path, f'{simIndex}-{score}.jpg'), img2)
                simIndex+=1


# images, DBs, result, images_name = Similarity.create_result_folder(r'D:\SimilarityOfImages\Datasets\test_case_1\Source', r'D:\SimilarityOfImages\Datasets\test_case_1\DB')
# Similarity.get_similarity(images, result, images_name, DBs)