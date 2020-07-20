#This is a Flask application
from flask import Flask, render_template, request, url_for, redirect
import asclepius


app = Flask(__name__)
@app.route('/')

#This is the landing page
def index():
    return render_template('index.html')

#This is the posts page where users can view posts and create posts
@app.route('/posts', methods=["GET","POST"])
def posts():
    posts = asclepius.Post.load_all()
    if request.method=="POST":
        title=request.form.get("title")
        description=request.form.get("description")
        asclepius.Account.write_post(title, description)
        return redirect(url_for('posts')) 
    return render_template("posts.html", posts=posts)


if __name__=="__main__":
    app.run(debug=False, host="0.0.0.0")
