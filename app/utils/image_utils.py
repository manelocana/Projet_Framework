


import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app




def save_image(image_file, folder):
    if not image_file or not image_file.filename:
        return None

    original_name = secure_filename(image_file.filename)
    unique_name = f"{uuid.uuid4().hex}_{original_name}"

    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], folder)

    os.makedirs(upload_path, exist_ok=True)

    image_file.save(os.path.join(upload_path, unique_name))

    return unique_name





def delete_image(filename, folder):
    if not filename:
        return

    path = os.path.join(
        current_app.config['UPLOAD_FOLDER'], folder, filename)

    if os.path.exists(path):
        os.remove(path)
