from taskbox import app, db, bcrypt
from taskbox.models import LoginForm, Todo, RegisterForm, User
from flask import render_template, request, redirect, url_for
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from quotes import Quotes
from questions import Questions

#testing login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/',methods=['POST','GET'])
#@login_required #05/03/22 attempted to make login required in order to access index.html(homepage)
def index():
    todolist()
    return render_template("index.html",QUOTES = Quotes())
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home')) #if login goes through, present index.html
    return render_template('login.html', form=form) #form in login.html is = to form = LoginForm()

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

#END Began working on login 04/30/22



@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/todolist')
    except:
        return 'There was a problem deleting that task'

#routing to update tasks page
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        
        form = request.form
        task.content = form['content']
        if 'progress' in form:
            task.progress = form['progress']

        try:
            db.session.commit()
            return redirect('/todolist')
        except:
            return 'There was an issue updating this task.'
    else:
        return render_template('update.html', task=task)

@app.route('/progress/<int:id>', methods=['GET', 'POST'])
def progress(id):
    task = Todo.query.get_or_404(id)
    # No GET method is no longer used. Idk why I even used it in the first place.
    if request.method == 'GET':
        try:
            tasks = Todo.query.order_by(Todo.date_created).all()
            return render_template('todolist.html', tasks=tasks)
        except:
            return 'There was an error in displaying the progress of this task.'
    if request.method == 'POST':
        task.progress = int(request.form["progress"])
        try:
            db.session.commit()
            return redirect('/todolist')
        except:
            return 'There was an error in updating the progress of this task.'

#routing to timer webpage
@app.route('/timer',methods=['POST','GET'])
def timer():
    return render_template("timer.html")

#routing to the journal webpage
@app.route('/journal',methods=['POST','GET'])
def journal():
    return render_template("journal.html", QUESTIONS=Questions())

#routing to about us webpage
@app.route('/about_us')
def about_us():
    return render_template("about_us.html")

#routing to the todolist webpage 
@app.route('/todolist', methods=['POST', 'GET'])
def todolist():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/todolist')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('todolist.html', tasks=tasks)

@app.route('/home',methods=['POST','GET'])
def home():
    todolist()
    return render_template("home.html", QUOTES = Quotes())

#routing to system_guide webpage
@app.route('/Documentation')
def systems_guide():
    return render_template("guidemanual.html")

#routing to system_guide webpage
@app.route('/references')
@login_required
def references():
    return render_template("references.html")