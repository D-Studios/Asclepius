import datetime
import json

class Account:
    @staticmethod
    def write_post(title, body):
        post_id = Post.new_id()
        post = Post(post_id, title, body)
        post.store_post()

class Post:
    id=0
    def __init__(self, post_id, title, body):
        self.post_id = post_id
        self.title = title
        self.body = body

    @staticmethod
    def new_id():
        Post.id=Post.id+1
        if Post.id==28:
            Post.id=1
        return Post.id#Get a new ID for fresh posts

    @staticmethod
    def load_all():
        global posts
        with open("json/posts.json") as post_data:
            posts = json.load(post_data)
        return posts

    #USE USER OBJECT AS ARGUMENT
    def store_post(self): #Store a post to JSON
        posts[self.post_id] = {
            'title': self.title,
            'body': self.body
        }
        with open("json/posts.json","w") as post_data:
            post_data.write(json.dumps(posts,indent=2))

