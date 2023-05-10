import random
import string
import requests
import json
import pandas
import sys
import time
import status_codes
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class webODM_class(BaseModel):
    photos_folder: str

    def create_token():
        token = requests.post('http://localhost:8000/api/token-auth/',
                            data={'username':'hossamwakeb',
                                'password': 'Qwe321qwe@'}).json()
        return(token['token'])
    
    def create_project(token):
        project = requests.post('http://localhost:8000/api/projects/', 
                            headers={'Authorization': 'JWT {}'.format(token)},
                            data={'name':'APIs'}).json()
        return(project['id'])

    def convert_photos_folder_to_ImgList(photos_folder):
        images = []
        for filename in os.listdir(photos_folder):
            if os.path.isfile(os.path.join(photos_folder, filename)):
                name, extension = os.path.splitext(filename)
                extension = extension.lower()
                if extension == ".jpg":
                    image = ('images', (rf'{photos_folder}\{filename}', open(rf'{photos_folder}\{filename}', 'rb'), 'image/jpg'))
                    images.append(image)
        return(images)

    def post_task_to_projects(project_id, images, token):
        post_request = requests.post('http://localhost:8000/api/projects/{}/tasks/'.format(project_id), 
                    headers={'Authorization': 'JWT {}'.format(token)},
                    files=images,
                    data={
                        'options': json.dumps([
                        {'name': "pc-csv", 'value': True, "auto-boundary": True}
                        ])}).json()
        return(post_request)

    def get_point_cloud_csv(post, token, project_id):
        task_id = post['id']
        while True:
            res = requests.get('http://localhost:8000/api/projects/{}/tasks/{}/'.format(project_id, task_id), 
                        headers={'Authorization': 'JWT {}'.format(token)}).json()

            if res['status'] == status_codes.COMPLETED:
                print("Task has completed!")
                break
            elif res['status'] == status_codes.FAILED:
                print("Task failed: {}".format(res))
                sys.exit(1)
            else:
                print("Processing, hold on...")
                time.sleep(3)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=25))    
        res = requests.get(f"http://localhost:8000/api/projects/{project_id}/tasks/{task_id}/download/{file_name}.csv", 
                            headers={'Authorization': 'JWT {}'.format(token)},
                            stream=True)
        with open(rf"{file_name}.csv", 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)
        csv_file = pandas.read_csv(rf"{file_name}.csv")

        return(json.dumps(csv_file))