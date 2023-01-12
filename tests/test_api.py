from flask import Flask
from api.api import api_blueprint


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.register_blueprint(api_blueprint)



def test_app():
    response = app.test_client().get('/api/posts/1')
    assert response.json.get("poster_name") == 'leo', "Имя получено неверно"
    assert response.json.get("pk") == 1, "pk получено неверно"


def test_app_all_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200, "Статус код запроса всех постов неверный"
    assert type(response.json) == list, "Получен не список"



