from flask import Flask, send_from_directory
from main.func import main_blueprint
from loader.func import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
# Регистрирую блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Обозначаю папку с изображениями"""
    return send_from_directory("uploads", path)


app.run()

