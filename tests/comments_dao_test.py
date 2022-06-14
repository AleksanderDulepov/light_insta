import pytest


class TestCommentsDAO:
    def test_get_comments_all(self, comments_dao_fix, test_keys_should_be_comments):
        comments = comments_dao_fix.get_comments_all()
        assert type(comments) == list, "Возвращает не список"
        assert len(comments) > 0, "Возвращает пустой список"
        assert set(comments[0].keys()) == test_keys_should_be_comments, "Неверный список ключей"

    def test_get_comments_by_post_id(self, comments_dao_fix, test_keys_should_be_comments):
        comments = comments_dao_fix.get_comments_by_post_id(1, [1])
        assert type(comments) == list, "Возвращает не список"
        assert set(comments[0].keys()) == test_keys_should_be_comments, "Неверный список ключей"
        assert comments[0]['post_id'] == 1, "Возвращает неправильный комментарий по посту"
        with pytest.raises(ValueError):
            comments_dao_fix.get_comments_by_post_id(0, [1])
