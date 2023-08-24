import os
import secrets
from PIL import Image
from flask_mail import Message
from flask import url_for
from flask_blog import create_app, mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(create_app.root_path, 'static/image', picture_filename)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        'Password reset mail',
        sender='muhammadbehroz777@gmail.com',
        recipients=[user.email]
    )

    msg.body = f'''To reset password please visit the link 
    {url_for('users.reset_token', token=token, _external=True)}'''
    mail.send(msg)
