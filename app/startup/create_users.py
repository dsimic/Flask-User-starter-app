from datetime import datetime
from app import app, db
from app.core.models import User, Role


def create_users():
    """ Create users when app starts """
    # Create all tables
    db.create_all()

    # Adding roles
    admin_role = find_or_create_role('admin', u'Admin')

    # User role
    user_role = find_or_create_role('user', u'User')

    # Add admin users
    for elem in app.config['APP_USER_ADMINS']:
        print "Creating user", elem
        user = find_or_create_user(
            elem[0], elem[1], elem[2], elem[3],
            admin_role
        )
    # Add providers
    for elem in app.config['APP_USER_REGULAR']:
        print "Creating user", elem
        user = find_or_create_user(
            elem[0], elem[1], elem[2], elem[3],
            user_role
        )
    # Save to DB
    db.session.commit()

    return user


def find_or_create_role(name, label):
    """ Find existing role or create new role """
    role = Role.query.filter(Role.name == name).first()
    if not role:
        role = Role(name=name, label=label)
        db.session.add(role)
    return role


def find_or_create_user(
    first_name, last_name, email, password, role=None
):
    """ Find existing user or create new user """
    user = User.query.filter(User.email == email).first()
    if not user:
        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=app.user_manager.hash_password(password),
                    active=True,
                    confirmed_at=datetime.utcnow())
        if role:
            user.roles.append(role)
        db.session.add(user)
    return user
