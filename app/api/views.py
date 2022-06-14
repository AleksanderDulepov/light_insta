from flask import Blueprint, current_app, jsonify, render_template
from app.posts.dao.posts_dao import PostsDAO
import logging
from logs.loggers import create_logger

api_blueprint = Blueprint('api_blueprint', __name__)

create_logger()
basic_logger = logging.getLogger('basic')


# возвращает все посты в json
@api_blueprint.route('/api/posts', methods=['GET'])
def full_list_api_page():
    posts_dao = PostsDAO(current_app.config.get('POSTS_PATH'))

    basic_logger.info("Запрос /api/posts")

    posts = posts_dao.get_posts_all()
    return jsonify(posts)


# возвращает контретный пост в json по id
@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def current_post_api_page(post_id):
    posts_dao = PostsDAO(current_app.config.get('POSTS_PATH'))
    try:
        post = posts_dao.get_posts_by_pk(post_id)
        basic_logger.info(f"Запрос /api/posts/{post_id}")
        return jsonify(post)
    except ValueError:
        return render_template('basic_templates/error.html', description=f'Нет поста с id {post_id}')
