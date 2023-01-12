from flask import Blueprint, jsonify
from utils import get_posts, get_post_by_pk



api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')

@api_blueprint.route('/api/posts', methods=['GET'])
def load_posts():
    posts = get_posts()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<post_id>', methods=['GET'])
def read_post(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)
