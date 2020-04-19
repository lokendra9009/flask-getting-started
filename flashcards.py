from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from datetime import datetime
from model import db, save_db

app = Flask(__name__)

# print(type(__name__))
counter = 0


@app.route("/")
def welcome():
    global counter
    now = datetime.now()
    date_string = now.strftime("%d-%m-%Y %H:%M:%S")
    counter += 1
    return render_template("welcome.html", blogs=db)


@app.route("/blog/<int:index>")
def blog(index):
    try:
        blog_content = db[index]
        return render_template("blog.html", blog=blog_content, index=index, max_index=len(db) - 1)
    except IndexError:
        abort(404)


@app.route("/add_blog", methods=["GET", "POST"])
def add_blog():
    if request.method == 'POST':
        blog = {"Title": request.form['title'],
                "Content": request.form['content']}
        db.append(blog)
        save_db()
        return redirect(url_for('welcome'))
    else:
        return render_template("add_blog.html")


@app.route("/api/blog/")
def api_blog_list():
    return jsonify(db)


@app.route("/api/blog/<int:index>")
def api_blog_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)


@app.route("/remove_blog/<int:index>", methods=['GET', 'POST'])
def remove_blog(index):
    try:
        if request.method == "POST":
            db.pop(index)
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_blog.html", blog=db[index])
    except IndexError:
        abort(404)
#
# @app.route("/date/")
# def datepage():
#     now = datetime.now()
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     return f"Today's date is {dt_string}!"


# @app.route("/visitcount/")
# def visit_counter():
#     global counter
#     counter += 1
#     return f"The visit count is {counter}"
