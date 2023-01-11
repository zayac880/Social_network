from flask import Flask, request, render_template
from utils import get_posts_all, get_comments_by_post_id, get_post_by_pk, search_for_posts, get_posts_by_user
import logging


logging.basicConfig(level=logging.INFO, filename="C:/Users/Alex/Desktop/Sky_python/kursovaya_inst/logs/py_log.log")


app = Flask(__name__)


@app.route("/")
def home():
   items = get_posts_all()
   return render_template("index.html", items=items)


@app.route("/search")
def search():
   query = request.args.get("s")
   posts = search_for_posts(query)
   count_posts = len(posts)
   return render_template("search.html", posts=posts, count_posts=count_posts)


@app.route("/posts/<postid>")
def viewing(postid):
   comments = get_comments_by_post_id(postid)
   item = get_post_by_pk(postid)
   return render_template("post.html", item=item, comments=comments)


@app.route("/user-feed/<username>")
def post_user(username):
   user = get_posts_by_user(username)
   return render_template("user-feed.html", user=user)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_server_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
