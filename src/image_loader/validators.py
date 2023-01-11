from fastapi import UploadFile
from starlette import status
from starlette.exceptions import HTTPException


def validate_image_loader_image(image: UploadFile) -> None:
	if image.filename.split(".")[-1] not in ["png", "jpg", "jpeg"]:
		raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
