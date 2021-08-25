from app import app, db
from app.models import User, Spare


@app.shell_context_processor
def make_shell_conext():
    return {'db': db, 'User': User, 'Spare': Spare}

