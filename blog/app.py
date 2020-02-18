import os
from flask import Flask, request, render_template
from posts_views import posts_app

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(posts_app, url_prefix='/posts')

@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()