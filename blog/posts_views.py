from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template, abort
from base_connect import Session, Base, engine
from models import Post, Tag, tags_posts_table


posts_app = Blueprint('posts_app', __name__)


@posts_app.route('/', endpoint='posts')
def posts_list():
    Base.metadata.create_all(engine)
    session = Session()
    return render_template(
        'posts/posts.html',
        posts=session.query(Post).all(),
        tag = session.query(Tag).all(),
    )


@posts_app.route('/<int:id>/', endpoint='post')
def post_info(id):
    try:
        Base.metadata.create_all(engine)
        session = Session()
        post=session.query(Post).get(id)
    except KeyError:
        raise NotFound(f'There is no post #{id}')
    return render_template(
        'posts/post.html',
        post=post,
    )


@posts_app.route('/tag/<int:tag>/', endpoint='tag')
def tag_info(tag):
    try:
        Base.metadata.create_all(engine)
        session = Session()
        post = session.query(Post).join(tags_posts_table).join(Tag).filter(Tag.id == tag).all()
        tag = session.query(Tag).all()
        data = (post, tag)
        print(data)
    except KeyError:
        raise NotFound(f'There is no tag #{id}')
    return render_template(
        'posts/posts.html',
        tag=tag,
        posts=post,
        
    )