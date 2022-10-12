from taskbox import db

# Configuratons, such as preset database values go here
def resetDB():
    db.drop_all()
    db.create_all()