def user_image_path(instance, filename):
    """Customizes the upload path for user images"""
    return f'user_iamge/{instance.username}/{filename}'


def create_activation_code(instance):
    import hashlib
    string = instance.email + str(instance.id)
    encode_string = string.encode()
    md5_object = hashlib.md5(encode_string)
    activation_code = md5_object.hexdigest()
    instance.activation_code = activation_code