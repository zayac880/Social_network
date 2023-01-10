from flask import Flask, jsonify
from utils import get_posts, get_post_by_pk
import logging


logging.basicConfig(level=logging.INFO, filename="../logs/py_log.log", filemode="w",
                    format="%(asctime)s [%(levelname)s] %(message)s")

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/posts', methods=['GET'])
def load_posts():
    posts = get_posts()
    return jsonify(posts)

@app.route('/posts/<post_id>', methods=['GET'])
def read_post(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == "__main__":
    app.run(debug=True, port=5009)