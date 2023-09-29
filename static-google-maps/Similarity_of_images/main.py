from fastapi import FastAPI
from similarity import Similarity
import uvicorn

app = FastAPI()

@app.get("/similarity")
async def similarity(source_path: str, db_path: str):
    images, DBs, result, images_name = Similarity.create_result_folder(source_path, db_path)
    Similarity.get_similarity(images, result, images_name, DBs)
    return({"Result": "Saved"})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)