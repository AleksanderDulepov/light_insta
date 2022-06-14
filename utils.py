from app.posts.class_Post import Post


# создание обьектов класса Post и запаковка их в список
def get_objects_list(posts, comments, tags):
    objects_list = []
    values_together = list(zip(posts, comments, tags))
    for i in values_together:
        objects_list.append(Post(i[0], i[1], i[2]))
    return objects_list


# список комментариев по каждому посту
def get_comments_for_choisen_posts(posts, posts_dao, comments_dao):
    comments = []
    for post in posts:
        comments_current_post = comments_dao.get_comments_by_post_id(post['pk'], posts_dao.get_all_posts_id())
        comments.append(comments_current_post)
    return comments


# список тэгов по каждому посту
def get_tags_for_choisen_posts(posts, posts_dao):
    tags = []
    for post in posts:
        current_post_tags = posts_dao.get_tags_by_pk(post['pk'])
        tags.append(current_post_tags)
    return tags
