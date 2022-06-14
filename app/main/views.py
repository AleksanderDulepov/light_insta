from flask import render_template, Blueprint, current_app
from app.posts.dao.posts_dao import PostsDAO
from app.comments.dao.comments_dao import CommentsDAO
import utils

main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route('/', methods=['GET'])
def main_page():
    posts_dao = PostsDAO(current_app.config.get('POSTS_PATH'))
    comments_dao = CommentsDAO(current_app.config.get('COMMENTS_PATH'))

    # список постов
    posts = posts_dao.get_posts_all()
    # список комментов к постам
    comments = utils.get_comments_for_choisen_posts(posts, posts_dao, comments_dao)
    # список тэгов по каждому посту
    tags = utils.get_tags_for_choisen_posts(posts, posts_dao)

    # соединяем все результаты в обьекте класса Post
    posts_to_output = utils.get_objects_list(posts, comments, tags)

    return render_template('app/main/templates/index.html', posts=posts_to_output)
