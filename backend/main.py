from fastapi import FastAPI

from backend.api.hardware import router as hardware_router
from backend.api.efi import router as efi_router
from backend.api.panic import router as panic_router
from backend.api.database import router as database_router

app = FastAPI(title="Hackintosh Builder PRO")

app.include_router(hardware_router)
app.include_router(efi_router)
app.include_router(panic_router)
app.include_router(database_router)

@app.get("/")
def root():
    return {"status":"running"}
