import pytest


class TestPostsDAO:
    def test_get_posts_all(self, posts_dao_fix, test_keys_should_be):
        posts = posts_dao_fix.get_posts_all()
        assert type(posts) == list, "Возвращает не список"
        assert len(posts) > 0, "Возвращает пустой список"
        assert set(
            posts[0].keys()) == test_keys_should_be, "Неверный список ключей"

    def test_search_for_posts(self, posts_dao_fix, test_keys_should_be):
        posts = posts_dao_fix.search_for_posts('квадратная')
        sentence_to_check = "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! " \
                            "Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не " \
                            "съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне " \
                            "вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были " \
                            "родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все " \
                            "остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как " \
                            "и я, в этот свой офис, было бы совсем неинтересно."
        assert type(posts) == list, "Возвращает не список"
        assert len(posts) > 0, "Возвращает пустой список"
        assert set(posts[0].keys()) == test_keys_should_be, "Неверный список ключей"
        assert posts[0]['content'] == sentence_to_check, "Возвращается неверный пост по поиску"

    def test_get_posts_by_pk(self, posts_dao_fix, test_keys_should_be):
        post = posts_dao_fix.get_posts_by_pk(1)
        assert type(post) == dict, "Возвращает не словарь"
        assert set(post.keys()) == test_keys_should_be, "Неверный список ключей"
        assert post['pk'] == 1, "Возвращает неправильный пост по номеру pk"
        with pytest.raises(ValueError):
            posts_dao_fix.get_posts_by_pk(0)

    def test_get_posts_by_user(self, posts_dao_fix, test_keys_should_be):
        posts = posts_dao_fix.get_posts_by_user('leo')
        assert type(posts) == list, "Возвращает не список"
        assert set(
            posts[0].keys()) == test_keys_should_be, "Неверный список ключей"
        assert posts[0]['poster_name'] == 'leo', "Возвращает неправильный пост по имени"
        with pytest.raises(ValueError):
            posts_dao_fix.get_posts_by_user('xxx')
