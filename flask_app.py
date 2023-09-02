from flask import Flask
from flask import render_template, Markup, request, abort
import markdown

flask_app = Flask(__name__, static_folder='./templates/static', template_folder='./templates', root_path='./')
flask_app.config['JSON_AS_ASCII'] = False

# 下面这里开始导入蓝图
from Exp16Room import *
# 下面这里开始注册蓝图
flask_app.register_blueprint(Exp16Room_blue)


@flask_app.route('/')
def flask_app_index():
    extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
                  'markdown.extensions.toc']
    markdown_content = ""
    with open(f'{flask_app.template_folder}/markdown/Exp.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html = markdown.markdown(markdown_content, extensions=extensions)
    content = Markup(html)
    return render_template('flask_app_index.html', content=content, title='Exp')


@flask_app.route('/help_info')
def flask_app_help_info():
    extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
                  'markdown.extensions.toc']
    markdown_content = ""
    with open(f'{flask_app.template_folder}/markdown/help_info.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html = markdown.markdown(markdown_content, extensions=extensions)
    content = Markup(html)
    return render_template('flask_app_help_info.html', content=content, title='信息和帮助')



@flask_app.route('/error_help')
def flask_app_error_help():
    extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
                  'markdown.extensions.toc']
    markdown_content = ""
    with open(f'{flask_app.template_folder}/markdown/error_help.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html = markdown.markdown(markdown_content, extensions=extensions)
    content = Markup(html)
    return render_template('flask_app_index.html', content=content, title='Exp.16Room')


@flask_app.errorhandler(404)
def flask_app_page_not_found(error):
    return render_template('Exp_state_404.html'), 404


@flask_app.errorhandler(500)
def flask_app_page_not_found(error):
    return render_template('Exp_state_500.html'), 500


if __name__ == '__main__':
    print(flask_app.url_map)
    flask_app.run(debug=True)

