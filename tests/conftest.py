import pytest
import run
from app.posts.dao.posts_dao import PostsDAO
from app.comments.dao.comments_dao import CommentsDAO

#для всех фикстур:
app = run.app


# ключи постов
@pytest.fixture()
def test_keys_should_be():
    return {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


# ключи комментариев
@pytest.fixture()
def test_keys_should_be_comments():
    return {'post_id', 'commenter_name', 'comment', 'pk'}


# тест-клиент
@pytest.fixture()
def test_client():
    return app.test_client()


# тестовый обьект класса PostsDAO
@pytest.fixture()
def posts_dao_fix():
    posts_dao_instance = PostsDAO(app.config.get('POSTS_PATH'))
    return posts_dao_instance

# тестовый обьект класса CommentsDAO
@pytest.fixture()
def comments_dao_fix():
    comments_dao_instance = CommentsDAO(app.config.get('COMMENTS_PATH'))
    return comments_dao_instance