from flask import Flask, Blueprint, render_template

from app.main.views import main_blueprint
from app.posts.views import posts_blueprint
from app.api.views import api_blueprint

app = Flask(__name__, template_folder='./')

# импортируем конфиг разработки
app.config.from_pyfile('config/development.py')
# json в unicode
app.config['JSON_AS_ASCII'] = False

# регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)


# обработчики ошибок
@app.errorhandler(404)
def page_not_found(e):
    return render_template('basic_templates/404.html'), 404

@app.errorhandler(500)
def internal_server(e):
    return render_template('basic_templates/500.html'), 500


if __name__ == "__main__":
    app.run()
