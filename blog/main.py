from flask import url_for, render_template, redirect
users_list = ['roma','CMH','minecraft']
from . import app, db
from .forms import UsersRegister, UsersSearch, Main
from .models import User, Post
from datetime import datetime

@app.route('/' ,methods=['GET','POST'])
def main():
    main = Main()
    return render_template('main.html', form=main)
    


@app.route('/register',methods=['GET', 'POST'])
def register():
    register = UsersRegister()
    if not register.validate_on_submit():
        return render_template('index.html', form=register)
    if User.query.filter(User.username == register.username.data).first():    
        return 'User {} already create'.format(register.username.data)
    else: 
        user = User(
            username = register.username.data
        )
        post = Post(
            text = 'пользователь создан' + str(datetime.now())
        )
        db.session.add(post)
        db.session.add(user)
        db.session.commit()
        return redirect(register.username.data)


@app.route('/search',methods=['GET', 'POST'])
def search():
    search = UsersSearch()
    if not search.validate_on_submit():
        return render_template('search.html', form=search)
    if User.query.filter(User.username == search.username.data).first():    
        return redirect(search.username.data)
    else:
        return 'User not found'
    

@app.route('/<username>')
def user(username):
    if User.query.filter(User.username == username).first():    
        return Post.query.filter(Post.username == username).all()
    
    else:
        return 'User not found'



if __name__ == '__main__':
    app.run()

