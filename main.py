from flask import Flask, render_template, redirect, request, abort
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/domforyou.db")
    app.run(debug=True)


@app.route("/")
def index():
    return render_template('base.html', title='AAAA')


if __name__ == '__main__':
    main()