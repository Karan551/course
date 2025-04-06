def get_cloudinary_image_object(instance, field_name="image", as_html=False, width=1200):

    if not hasattr(instance, field_name):
        return None

    image_object = getattr(instance, field_name)
    if not image_object:
        return None

    image_options = {
        "width": width
    }

    if as_html:
        return image_object.image(**image_options)

    img_url = image_object.build_url(**image_options)
    return img_url
