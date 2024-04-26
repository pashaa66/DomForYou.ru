from flask import Flask, render_template, redirect, request, abort
from data import db_session
import os
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.users import User
from data.announcements import Announcements
from forms.login import LoginForm
from forms.announcement import CreateAnnouncementForm
from forms.register import RegisterFormUser, RegisterFormRealtor
from werkzeug.utils import secure_filename
from data.map_api import get_coodrinates, create_map

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

def main():
    db_session.global_init("db/dom_for_you.db")
    app.run(debug=True)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    announcement_list = db_sess.query(Announcements).all()
    return render_template('index.html', title='Объявления', announcements=announcement_list)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register_menu.html', title='Регистрация')

@app.route('/creating_an_announcement', methods=['GET', 'POST'])
def creating_an_announcement():
    form = CreateAnnouncementForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        location = f'{form.city.data}, {form.street.data}, {form.number_of_house.data}'
        announcement = Announcements(
            title=form.title.data,
            description=form.description.data,
            location=location,
            price=form.price.data,
            announcement_type=form.announcement_type.data,
            square=form.square.data,
            kitchen_square=form.kitchen_square.data,
            number_of_rooms=form.number_of_rooms.data,
            floor=form.floor.data,
            number_of_floors=form.number_of_floors.data,
            year_of_construction=form.year_of_construction.data,
            is_sell=form.is_sell.data
        )
        file = form.photo.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.static_folder, 'img\img_announcement', filename))
        announcement.path_to_photo = 'img/img_announcement/' + filename
        coord = get_coodrinates(form.city.data, form.street.data, form.number_of_house.data)
        map = create_map(coord)
        map.save(os.path.join(app.static_folder, 'img\img_announcement', map))
        # current_user.announcement.append(announcement)
        # db_sess.merge(current_user)
        db_sess.add(announcement)
        db_sess.commit()
        return redirect('/')
    return render_template('creating_an_announcement.html', title='Создание объявления', form=form)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message='Неправильный логин или пароль',
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register_buyer', methods=['GET', 'POST'])
def register_buyer():
    form = RegisterFormUser()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register_buyer.html', title='Регистрация',
                                   form=form,
                                   message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register_buyer.html', title='Регистрация',
                                   form=form,
                                   message='Такой пользователь уже есть')
        buyer = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            email=form.email.data,
            role='buyer'
        )
        buyer.set_password(form.password.data)
        db_sess.add(buyer)
        db_sess.commit()
        return redirect('/login')
    return render_template('register_buyer.html', title='Регистрация', form=form)

@app.route('/register_realtor', methods=['GET', 'POST'])
def register_realtor():
    form = RegisterFormRealtor()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register_realtor.html', title='Регистрация',
                                   form=form,
                                   message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register_realtor.html', title='Регистрация',
                                   form=form,
                                   message='Такой пользователь уже есть')
        if db_sess.query(User).filter(User.phone_number == form.phone_number.data).first():
            return render_template('register_buyer.html', title='Регистрация',
                                   form=form,
                                   message='Такой пользователь уже есть')
        realtor = User(
            name=form.name.data,
            surname=form.surname.data,
            age=form.age.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            experience=form.experience.data,
            role='realtor'
        )
        realtor.set_password(form.password.data)
        db_sess.add(realtor)
        db_sess.commit()
        return redirect('/login')
    return render_template('register_realtor.html', title='Регистрация', form=form)

@app.route('/announcement/<int:id>')
def announcement(id):
    db_sess = db_session.create_session()
    current_announcement = db_sess.query(Announcements).filter(Announcements.id == id).first()
    if not current_announcement:
        abort(404)
    return render_template('announcement.html', announcement=current_announcement, title=current_announcement.title)

if __name__ == '__main__':
    main()
