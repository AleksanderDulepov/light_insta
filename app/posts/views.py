from flask import render_template, Blueprint, current_app, request
from app.posts.dao.posts_dao import PostsDAO
from app.comments.dao.comments_dao import CommentsDAO
import utils

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder='templates')


# вьюшка для страницы подробной информации о посте
@posts_blueprint.route('/posts/<int:post_id>', methods=['GET'])
def one_post_page(post_id):
    posts_dao = PostsDAO(current_app.config.get('POSTS_PATH'))
    comments_dao = CommentsDAO(current_app.config.get('COMMENTS_PATH'))
    try:
        post = posts_dao.get_posts_by_pk(post_id)
        # список комментов к постам
        comments = utils.get_comments_for_choisen_posts([post], posts_dao, comments_dao)
        # список тэгов по каждому посту
        tags = utils.get_tags_for_choisen_posts([post], posts_dao)
        # соединяем все результаты в обьекте
        posts_to_output = utils.get_objects_list([post], comments, tags)

        return render_template('post.html', posts=posts_to_output)

    except ValueError:
        return render_template('error.html', description=f'Нет поста с id={post_id}')


# вьюшка для стартовой страницы поиска
@posts_blueprint.route('/search', methods=['GET'])
def search_start_page():
    return render_template('search_start.html')


# вьюшка для страницы с результатами поиска
@posts_blueprint.route('/search/', methods=['GET'])
def search_page():
    posts_dao = PostsDAO(current_app.config.get('POSTS_PATH'))
    comments_dao = CommentsDAO(current_app.config.get('COMMENTS_PATH'))

    word = request.args['word_to_find']
    posts = posts_dao.search_for_posts(word)

    # список комментов к постам
    comments = utils.get_comments_for_choisen_posts(posts, posts_dao, comments_dao)
    # список тэгов по каждому посту
    tags = utils.get_tags_for_choisen_posts(posts, posts_dao)

    # соединяем все результаты в обьекте
    posts_to_output = utils.get_objects_list(posts, comments, tags)

    return render_template('search.html', posts=posts_to_output, finded_word=word)


# вьюшка для страницы пользователя
@posts_blueprint.route('/users/<username>', methods=['GET'])
def user_posts_page(username):
    posts_dao = PostsDAO(current_app.config.get('POSTS_PATH'))
    comments_dao = CommentsDAO(current_app.config.get('COMMENTS_PATH'))
    try:
        posts = posts_dao.get_posts_by_user(username, comments_dao.get_all_users())
        # список комментов к постам
        comments = utils.get_comments_for_choisen_posts(posts, posts_dao, comments_dao)
        # список тэгов по каждому посту
        tags = utils.get_tags_for_choisen_posts(posts, posts_dao)
        # соединяем все результаты в обьекте
        posts_to_output = utils.get_objects_list(posts, comments, tags)
        return render_template('user-feed.html', finded_username=username, posts=posts_to_output)
    except ValueError:
        return render_template('error.html', description=f'Нет пользователя с именем {username}')


# вьюшка для вывода результатов перехода по тэгу
@posts_blueprint.route('/tag/<tagname>', methods=['GET'])
def tags_posts_page(tagname):
    posts_dao = PostsDAO(current_app.config.get('POSTS_PATH'))
    comments_dao = CommentsDAO(current_app.config.get('COMMENTS_PATH'))
    try:
        posts = posts_dao.search_tags_in_posts(tagname)
        # список комментов к постам
        comments = utils.get_comments_for_choisen_posts(posts, posts_dao, comments_dao)
        # список тэгов по каждому посту
        tags = utils.get_tags_for_choisen_posts(posts, posts_dao)
        # соединяем все результаты в обьекте
        posts_to_output = utils.get_objects_list(posts, comments, tags)
        return render_template('tag.html', finded_tag=tagname, posts=posts_to_output)
    except ValueError:
        return render_template('error.html', description=f'Нет постов с тэгом {tagname}')
