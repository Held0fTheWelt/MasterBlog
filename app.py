import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

BLOG_POSTS_FILE = Path(__file__).parent / "data" / "blog_posts.json"


def load_blog_posts():
    """Load blog posts from the JSON storage file."""
    with open(BLOG_POSTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route('/')
def index():
    blog_posts = load_blog_posts()
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
