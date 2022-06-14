import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    # загрузка данных из файла
    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # список всех пользователей из постов
    def get_all_users(self):
        posts = self.load_data()
        all_users = set()
        for post in posts:
            all_users.add(post['poster_name'].lower())
        return all_users

    # список всех id постов
    def get_all_posts_id(self):
        posts = self.load_data()
        all_posts_id = []
        for post in posts:
            all_posts_id.append(post['pk'])
        return all_posts_id

    # получение всех постов
    def get_posts_all(self):
        posts = self.load_data()
        return posts

    # поиск постов по ключевому слову
    def search_for_posts(self, query):
        posts = self.load_data()
        query = query.lower()
        good_posts = []
        for post in posts:
            if query in post['content'].lower():
                good_posts.append(post)
        return good_posts

    # поиск поста по id
    def get_posts_by_pk(self, pk):
        posts = self.load_data()
        for post in posts:
            if post['pk'] == pk:
                return post
        raise ValueError(f'Поста с id {pk} не существует')

    # поиск всех постов конкретного пользователя
    def get_posts_by_user(self, username, all_users_from_comments={}):
        username = username.lower()
        all_users_from_posts = self.get_all_users()
        all_users = all_users_from_posts.union(all_users_from_comments)
        if username in all_users:
            posts = self.load_data()
            users_posts = []
            for post in posts:
                if post['poster_name'].lower() == username:
                    users_posts.append(post)
            return users_posts
        else:
            raise ValueError(f'Пользователя {username} не существует')

    # получение всех тэгов конкретного поста по id
    def get_tags_by_pk(self, pk):
        post = self.get_posts_by_pk(pk)
        tags = []
        word_list = post['content'].lower().split(" ")
        for word in word_list:
            if word[0] == "#":
                tags.append(word[1::])
        return tags

    # поиск постов по тэгу
    def search_tags_in_posts(self, tagname):
        tag_query = f'#{tagname}'
        posts_with_tag = self.search_for_posts(tag_query)
        if posts_with_tag:
            return posts_with_tag
        else:
            raise ValueError(f'Постов в тэгом {tagname} не существует')
