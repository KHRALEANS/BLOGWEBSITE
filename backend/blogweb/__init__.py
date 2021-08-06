from flask import Blueprint
#from backend.blogweb import blog_web

bp = Blueprint('blog_app', __name__, template_folder="../../frontend/dist/",
               static_folder="../../frontend/dist/blog/lib", url_prefix='/blog')
