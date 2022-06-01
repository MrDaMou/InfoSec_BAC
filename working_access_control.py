from flask import Flask, render_template, request, redirect
import flask_login

app = Flask(__name__)
app.secret_key = 'r9/EZCr;NWug>[_>'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@app.route("/")
def index():
    return render_template('index.html', title='Start')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        
        if 'next' in request.args:
            print("ayy")
            if 'profile' in request.args['next']:
                print("ayy")
                return render_template('login.html', title='Login', login_required=True)

        return render_template('login.html', title='Login')


    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        matching_users = [user for user in users if user.username == username and user.password == password]
        if len(matching_users) != 1:
            return "Login failed. Please check credentials"
        
        flask_login.login_user(matching_users[0])
        return redirect('/profile')

@app.route('/profile')
@flask_login.login_required
def profile():
    return render_template('profile.html', title='Profile', username=flask_login.current_user.username, userid=flask_login.current_user.id, fav_singer=flask_login.current_user.favourite_singer)

@app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect('/')

class User(flask_login.UserMixin):
    def __init__(self, id, username, password, favourite_singer):
        self.id = id
        self.username = username
        self.password = password
        self.favourite_singer = favourite_singer

    def get_id(self):
        return self.id

users = [User(1, 'Paul', '123', 'Taylor Swift'), User(2 ,'Moritz', '456', 'Katy Perry')]

@login_manager.user_loader
def load_user(userid):
    user_match = [user for user in users if user.id == userid]
    if len(user_match) == 1:
        return user_match[0]
    return None