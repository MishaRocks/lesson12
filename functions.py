import json


# загрузка базы постов для публикации в поиске
def open_file():
    with open('posts.json', 'r', encoding="utf-8") as file:
        return json.load(file)


# добавление поста в json
def add_post_json(post):
    posts = open_file()
    posts.append(post)
    with open('posts.json', 'w', encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
