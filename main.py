from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/cek-pdf")
async def cek_pdf(file: UploadFile = File(...)):
    filename = file.filename
    hasil = {
        "filename": filename,
        "keywords_found": {
            "SPM": True,
            "SP2D": False,
            "SPP": True
        }
    }
    return JSONResponse(content=hasil)
