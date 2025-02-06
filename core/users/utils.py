import os
import secrets
from werkzeug.utils import secure_filename
from flask import current_app


def create_path(location, file) -> str:
    pic_path = os.path.join(str(current_app.static_folder), f"images/{location}")
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)

    image_file = secure_filename(file.filename)
    random_string = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image_file)
    image = random_string + f_ext
    file.save(os.path.join(pic_path, image))
    return f"images/{location}/" + str(image)
