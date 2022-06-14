import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    # загрузка данных из файла
    def load_data(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return json.load(file)

    # список всех пользователей из базы комментариев
    def get_all_users(self):
        comments = self.load_data()
        all_users = set()
        for comment in comments:
            all_users.add(comment['commenter_name'].lower())
        return all_users

    # получение всех комментариев
    def get_comments_all(self):
        comments = self.load_data()
        return comments

    # получение всех комментариев конкретного поста
    def get_comments_by_post_id(self, post_id, all_posts_id: list):
        if post_id in all_posts_id:
            comments = self.load_data()
            current_post_comments = []
            for comment in comments:
                if comment['post_id'] == post_id:
                    current_post_comments.append(comment)
            return current_post_comments
        else:
            raise ValueError(f'Поста с id {post_id} не существует')
