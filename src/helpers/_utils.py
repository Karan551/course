from decouple import config
import cloudinary


CLOUDINARY_CLOUD_NAME = config("CLOUDNIARY_CLOUD_NAME", cast=str)
CLOUDINARY_PUBLIC_API_KEY = config("CLOUDNIARY_API_KEY", cast=str)
CLOUDINARY_SECRET_KEY = config("CLOUDNIARY_SECRET_KEY")


def cloudinary_init():
    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_PUBLIC_API_KEY,
        api_secret=CLOUDINARY_SECRET_KEY,
        secure=True
    )
