# класс для передачи всей информации о посте, комментариях, тэгах одним обьектом в шаблон
class Post:
    def __init__(self, value, comment, tag):
        self.value = value
        self.comment = comment
        self.tag = tag

    # метод позволяет выводить превью контента
    def get_preview_content(self):
        return f'{self.value["content"][0:30]}...'
