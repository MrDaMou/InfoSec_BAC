from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = '1'


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
        
        return redirect('/profile?userid=' + str(matching_users[0].id))

@app.route('/profile')
def profile():
    if 'userid' in request.args:
        matching_users = [user for user in users if user.id == int(request.args['userid'])]
        if len(matching_users) != 0:
            return render_template('profile.html', title='Profile', username=matching_users[0].username, userid=matching_users[0].id, fav_singer=matching_users[0].favourite_singer)

    return render_template('login.html', title='Login', login_required=True)

@app.route("/logout")
def logout():
    return redirect('/')

class User():
    def __init__(self, id, username, password, favourite_singer):
        self.id = id
        self.username = username
        self.password = password
        self.favourite_singer = favourite_singer

    def get_id(self):
        return self.id
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

users = [User(1, 'Paul', '123', 'Taylor Swift'), User(2 ,'Moritz', '456', 'Katy Perry')]