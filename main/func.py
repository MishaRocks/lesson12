from json import JSONDecodeError
from flask import request, render_template, Blueprint
from functions import open_file
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename="basic.log", level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    """публикация фаормы поиска"""
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    """реализация поиска"""
    logging.info("Выполняется поиск")
    s = request.args.get('s').lower()
    posts_found = []
    """проверка файла json"""
    try:
        for i in open_file():
            if s in i["content"].lower():
                posts_found.append(i)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'

    return render_template('post_list.html', posts_found=posts_found, result=s)
