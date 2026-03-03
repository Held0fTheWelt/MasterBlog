import json
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

BLOG_POSTS_FILE = Path(__file__).parent / "data" / "blog_posts.json"


def load_blog_posts():
    """Load blog posts from the JSON storage file."""
    with open(BLOG_POSTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_blog_posts(posts):
    """Save blog posts to the JSON storage file."""
    with open(BLOG_POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)


def fetch_post_by_id(post_id):
    """Return the blog post with the given id, or None if not found."""
    posts = load_blog_posts()
    for p in posts:
        if p["id"] == post_id:
            return p
    return None


@app.route('/')
def index():
    blog_posts = load_blog_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        posts = load_blog_posts()
        new_id = max((p["id"] for p in posts), default=0) + 1
        new_post = {
            "id": new_id,
            "author": request.form.get("author", "").strip(),
            "title": request.form.get("title", "").strip(),
            "content": request.form.get("content", "").strip(),
        }
        posts.append(new_post)
        save_blog_posts(posts)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    posts = load_blog_posts()
    posts = [p for p in posts if p["id"] != post_id]
    save_blog_posts(posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        posts = load_blog_posts()
        for p in posts:
            if p["id"] == post_id:
                p["author"] = request.form.get("author", "").strip()
                p["title"] = request.form.get("title", "").strip()
                p["content"] = request.form.get("content", "").strip()
                break
        save_blog_posts(posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
