from flask import render_template, request, redirect, url_for
from app import app
from app import db
from app.models import User,todolist
from cryptography.fernet import Fernet
key = Fernet.generate_key() 
cipher_suite = Fernet(key)

@app.route('/app/agent',methods=['POST'])
def signUp():
    try:
        agent_id = str(request.form.get('agentId'))
        password = str(request.form.get('password'))
        encoded_pass = encrypt(password)
        new_user = User(agent_id,encoded_pass)
        db.session.add(new_user)
        db.session.commit()
        return "Account Created",200
    except():
        return "Failure"
def encrypt(text):
    t = bytes(text, "utf-8")
    encoded_text = cipher_suite.encrypt(t)
    return encoded_text.decode("utf-8")
def decrypt(text):
    decoded_text = cipher_suite.decrypt(text)
    return decoded_text.decode("utf-8")

@app.route('/app/agent/auth')
def auth():
    try:
        agent_id = str(request.form.get('agent_id'))
        password = str(request.form.get('password'))``
        pass = db.session.query(User).filter(User.agent_id==agent_id)
        a = pass.password
        if a==encrypt(password):
            session['agent_id'] = agent_id
            return "Success"+"agent_id",200
        else:
            return "Failure",401
    except:
        return "Failure",401

@app.route('app/sites/list')
def list():
    todo = todolist.query.filter(todolist.agent_id == session['agent_id']).order_by(todolist.due_date).all()
    return todo

@app.route('app/sites', methods=['POST'])
def add():
    try:
        agent_id = str(request.form.get('agent_id'))
        title = str(request.form.get('title'))
        desc = str(request.form.get('description'))
        category = str(request.form.get('category'))
        date = request.form.get('date')
        new_todo = todolist(agent_id,title,desc,category,date)
        return "Success",200
    except:
        return "Failure",401
