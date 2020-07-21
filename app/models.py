from app import db

class User(db.Model):
    __tablename__ = 'userdetails'
    id = db.Column('id',db.Integer, primary_key=True)
    agent_id = db.Column('agent_id',db.Unicode)
    password = db.Column('password',db.Unicode)


    def __init__(self, agent_id, password):
        self.agent_id = agent_id
        self.password = password

class todolist(db.Model):
    __tablename__ = 'todolist'
    id = db.Column('id',db.Integer, primary_key=True)
    agent_id = db.Column('agent_id',db.Integer)
    title = db.Column('title',db.Unicode)
    description = db.Column('description',db.Unicode)
    category = db.Column('Category',db.Unicode)
    due_date = db.Column('due_date',db.Date)

    def __init__(self,agent_id,title,description,category,due_date):
        self.agent_id = agent_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
