
from fastapi import FastAPI
import requests

# Create server1
app1 = FastAPI()

@app1.get("/")
async def root():
    return {"message":"this is the server1"}

@app.post("/get_file/")
async def get_file(file_name: str):
    file_path = os.path.join("/path/to/folder", file_name)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            contents = f.read()
            return {"file": contents}
    else:
        return {"file": None}
