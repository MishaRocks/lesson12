from json import JSONDecodeError
from flask import request, render_template, Blueprint
from functions import add_post_json
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post/')
def post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post/', methods=['POST'])
def new_post():
    content = request.form.get('content')
    picture = request.files.get('picture')

    if not picture or not content:
        return 'Вы не загрузили картинку или текст'

    filename = picture.filename

    if filename.lower().split('.')[-1] not in ['jpeg', 'png', 'jpg']:
        return 'Неверное расширение файла'

    picture.save(f"./uploads/{filename}")
    pic_path = '/' + f"./uploads/{filename}"
    post_dict = {"pic": pic_path, "content": content}
    try:
        add_post_json(post_dict)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('post_uploaded.html', pic=pic_path, content=content)

