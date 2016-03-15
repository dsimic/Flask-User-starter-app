from . import views
from app import app, db
from flask_admin import Admin
from . views import MyModelView as ModelView
from app.core.models import User, Role, UsersRoles
from app.core.models import UserInvitation

admin = Admin(
    app, name="MyApp", template_mode='bootstrap3',
    index_view=views.MyAdminIndexView())

# Flask and Flask-SQLAlchemy initialization here

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Role, db.session))
admin.add_view(ModelView(UsersRoles, db.session))
admin.add_view(ModelView(UserInvitation, db.session))
