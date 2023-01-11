from fastapi import APIRouter, Depends, UploadFile
from starlette import status

from src.auth.dependecies import get_user
from src.common.utils import get_function_docs, get_function_response_type
from src.image_loader.contrrollers.image_loader_controller import ImageLoaderController
from src.image_loader.repositories.image_alchemy_repository import ImageAlchemyRepository
from src.image_loader.repositories.image_meta_data_alchemy_repository import ImageMetaDataAlchemyRepository
from src.image_loader.schemas.image_meta_data_schema import ImageMetaDataUploadSchema
from src.image_loader.schemas.image_search_filter_schema import ImageSearchFilterSchema
from src.users.schemas.user_schema import UserSchema


router = APIRouter()

__image_repository = ImageAlchemyRepository
__image_meta_data_repository = ImageMetaDataAlchemyRepository


@router.post(
	path="",
	description=get_function_docs(ImageLoaderController.save_image),
	response_model=get_function_response_type(ImageLoaderController.save_image),
	status_code=status.HTTP_201_CREATED)
def upload_image(image: UploadFile, user: UserSchema = Depends(get_user), image_meta_data: ImageMetaDataUploadSchema = Depends()):
	return ImageLoaderController(
		image_repository=__image_repository,
		image_meta_data_repository=__image_meta_data_repository
	).save_image(image=image, user=user, image_meta_data=image_meta_data)


@router.post(
	path="/filter",
	description=get_function_docs(ImageLoaderController.get_images),
	response_model=get_function_response_type(ImageLoaderController.get_images),
	status_code=status.HTTP_200_OK)
def get_images(image_search_filter: ImageSearchFilterSchema, user: UserSchema = Depends(get_user)):
	return ImageLoaderController(
		image_repository=__image_repository,
		image_meta_data_repository=__image_meta_data_repository
	).get_images(user=user, image_search_filter=image_search_filter)
