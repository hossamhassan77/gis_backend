import requests
import json
import sys
import time
import status_codes

res = requests.post('http://localhost:8000/api/token-auth/',
                    data={'username':'hossamwakeb',
                        'password': 'Qwe321qwe@'}).json()
token = res['token']

res = requests.post('http://localhost:8000/api/projects/', 
                    headers={'Authorization': 'JWT {}'.format(token)},
                    data={'name':'APIs project'}).json()
project_id = res['id']

images = [
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0040.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0040.JPG', 'rb'), 'image/jpg')), 
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0041.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0041.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0042.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0042.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0043.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0043.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0044.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0044.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0045.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0045.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0046.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0046.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0076.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0076.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0077.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0077.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0078.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0078.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0079.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0079.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0080.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0080.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0081.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0081.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0082.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0082.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0097.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0097.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0098.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0098.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0099.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0099.JPG', 'rb'), 'image/jpg')),
    ('images', (r'D:\wakeb\drone_to_map\images\YUN_0100.JPG', open(r'D:\wakeb\drone_to_map\images\YUN_0100.JPG', 'rb'), 'image/jpg'))
]

options = json.dumps([
    {'name': "fast-orthophoto", 'value': True, "auto-boundary": True}
])

res = requests.post('http://localhost:8000/api/projects/{}/tasks/'.format(project_id), 
            headers={'Authorization': 'JWT {}'.format(token)},
            files=images,
            data={
                'options': options
            }).json()

task_id = res['id']

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

res = requests.get("http://localhost:8000/api/projects/{}/tasks/{}/download/orthophoto.tif".format(project_id, task_id), 
                        headers={'Authorization': 'JWT {}'.format(token)},
                        stream=True)
with open(r"orthophoto.tif", 'wb') as f:
    for chunk in res.iter_content(chunk_size=1024): 
        if chunk:
            f.write(chunk)
print("Saved ./orthophoto.tif")