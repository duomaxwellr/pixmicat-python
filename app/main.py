import tempfile
from fastapi import FastAPI, Header, File, UploadFile
from PIL import Image

app = FastAPI()
# im = Image.open("")

@app.get("/")
async def main():
    return "OK"