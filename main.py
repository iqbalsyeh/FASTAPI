from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/cek-pdf")
async def cek_pdf(file: UploadFile = File(...)):
    # Baca nama file dan isi file (dummy saja)
    filename = file.filename

    # Simulasi: misalnya kita bilang "dokumen ini ditemukan SPM dan SP2D"
    hasil = {
        "filename": filename,
        "keywords_found": {
            "SPM": True,
            "SP2D": False,
            "SPP": True
        }
    }

    return JSONResponse(content=hasil)

# Untuk development lokal
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
