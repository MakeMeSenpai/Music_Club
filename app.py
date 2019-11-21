from jinja2 import Environment, PackageLoader, select_autoescape
from flask import Flask, render_template

env = Environment(
    loader=PackageLoader('app', 'base.html index.html music.html'),
    autoescape=select_autoescape(['html', 'xml'])
)
app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    #template = env.get_template()
    return render_template('index.html')

@app.route("/music")
def music():
    #template = env.get_template()
    return render_template('music.html')

if __name__ == '__main__':
    app.run(debugger=True)