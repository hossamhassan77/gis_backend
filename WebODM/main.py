import uvicorn
from fastapi import FastAPI
from webODM import webODM_class

app = FastAPI()

@app.get("/from_images_to_pointCloud")
def main(request: webODM_class):
    token = webODM_class.create_token()
    project = webODM_class.create_project(token)
    image_list = webODM_class.convert_photos_folder_to_ImgList(request.photos_folder)
    task_to_project = webODM_class.post_task_to_projects(project,image_list, token)
    get_csv = webODM_class.get_point_cloud_csv(task_to_project, token, project)
    json_data = webODM_class.csv_to_json(get_csv)
    return get_csv

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)