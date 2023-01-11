import uvicorn as uvicorn
from fastapi import FastAPI

from src.config import ProjectConfig
from src.image_loader.routers.image_loader_router import router as image_loader_router


app = FastAPI(title="Vivida Systems Test Task")


if ProjectConfig.DEBUG is True:
	app = FastAPI(title="Vivida Systems Test Task")
else:
	app = FastAPI(title="Vivida Systems Test Task", docs_url=None, redoc_url=None)


app.include_router(router=image_loader_router, prefix="/image_loader", tags=["IMAGE LOADER"])


if __name__ == '__main__':
	uvicorn.run("main:app", host=ProjectConfig.APP_HOST, port=ProjectConfig.APP_PORT, reload=ProjectConfig.DEBUG)
