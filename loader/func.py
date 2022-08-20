from json import JSONDecodeError
from flask import request, render_template, Blueprint
from functions import add_post_json
import logging

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename="basic.log", level=logging.INFO)

@loader_blueprint.route('/post/')
def post_form():
    """экземпляр блюпринта с формой для публикации поста"""
    return render_template('post_form.html')


@loader_blueprint.route('/post/', methods=['POST'])
def new_post():
    """получение поста из формы"""
    content = request.form.get('content')
    picture = request.files.get('picture')
    """проверка на наличие картинки и текста"""
    if not picture or not content:
        return 'Вы не загрузили картинку или текст'

    filename = picture.filename
    """проверка расширения файла"""
    if filename.lower().split('.')[-1] not in ['jpeg', 'png', 'jpg']:
        logging.info("Загруженный файл не картинка")
        return 'Неверное расширение файла'

    picture.save(f"./uploads/{filename}")
    pic_path = '/' + f"./uploads/{filename}"
    post_dict = {"pic": pic_path, "content": content}
    """проверки на наличие файла json"""
    try:
        add_post_json(post_dict)
    except FileNotFoundError:
        logging.info("Ошибка загрузки файла")
        return 'Файл не найден'
    except JSONDecodeError:
        logging.info("Ошибка загрузки файла")
        return 'Невалидный файл'

    return render_template('post_uploaded.html', pic=pic_path, content=content)

