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


def get_cloudinary_video_object(instance,
                                as_html=False,
                                field_name="video",
                                width=None,
                                height=None,
                                sign_url=False,  # True For private videos
                                fetch_format="auto",
                                resource_type="video",
                                controls=True,
                                autoplay=True,
                                poster=None,
                           
                                quality="auto"):
    if not hasattr(instance, "video"):
        return None

    video_object = getattr(instance, "video")
    if not video_object:
        return None

    video_options = {
        "sign_url": sign_url,
        "quality": quality,
        "fetch_format": fetch_format,
        "controls": controls,
        "autoplay": autoplay,
        "poster": poster,
        # "muted": muted

    }

    if width is not None:
        video_options["width"] = width

    if height is not None:
        video_options["height"] = height

    if height and width:
        video_options["crop"] = "limit"

    video_url = video_object.build_url(**video_options)
    if as_html:
        video_html = f"""
        <video controls={controls} autoplay={autoplay} poster={poster}>
            <source type="video/mp4" src={video_url} />
        <source type="video/ogg" src={video_url} />
            </video>
            """
        return video_html.format(video_url=video_url).strip()
        return video_object.video(**video_options)

    return video_url
