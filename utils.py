import json

def get_posts_all():
    """Функция загружает посты из файла"""
    with open("C:/Users/Alex/Desktop/Sky_python/kursovaya_inst/data/posts.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
        return posts


def get_posts_by_user(user_name):
    """Функция возвращает посты определенного пользователя."""
    post = []
    for user in get_posts_all():
        if user["poster_name"] in user_name:
            post.append(user)
    if not post:
        return ValueError
    else:
        return post


def get_comments_by_post_id(post_id):
    """Функция возвращает комментарии определенного поста."""
    with open("C:/Users/Alex/Desktop/Sky_python/kursovaya_inst/data/comments.json", "r", encoding="utf-8") as f:
        comment = []
        comments = json.load(f)
        for comment_one in comments:
            if comment_one["post_id"] == int(post_id):
                comment.append(comment_one)
        if not comment:
            return ValueError
        else:
            return comment


def search_for_posts(query):
    """Функция возвращает список постов по ключевому слову."""
    posts_for_query = []
    for post in get_posts_all():
        if str(query) in post["content"]:
            posts_for_query.append(post)
    return posts_for_query


def get_post_by_pk(pk):
    """Функция возвращает один пост по его pk."""
    number = []
    number.append(int(pk))
    for post in get_posts_all():
        if post["pk"] in number:
            return post


def get_posts():
    """Функция возвращает все посты"""
    data = get_posts_all()
    return data
