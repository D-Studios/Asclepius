#JSON is used
import json

#This class is used to create posts
class Post:
    #The id of the post
    id=0
    #Initializing Post
    def __init__(self, post_id, title, body):
        self.post_id = post_id
        self.title = title
        self.body = body

    #Writing a post
    @staticmethod
    def write_post(title, body):
        post_id = Post.new_id()
        post = Post(post_id, title, body)
        post.store_post()

    #Determining the id for the new post
    @staticmethod
    def new_id():
        Post.id=Post.id+1
        if Post.id==28:
            Post.id=1
        return Post.id

    #Loading all the posts
    @staticmethod
    def load_all():
        global posts
        with open("json/posts.json") as post_data:
            posts = json.load(post_data)
        return posts

    #Storing the post in the JSON file
    def store_post(self): 
        posts[self.post_id] = {
            'title': self.title,
            'body': self.body
        }
        with open("json/posts.json","w") as post_data:
            post_data.write(json.dumps(posts,indent=2))

