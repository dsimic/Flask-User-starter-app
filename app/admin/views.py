from flask_admin import expose, AdminIndexView
from flask_user import current_user
from app.core.forms import MyInviteForm
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request


class AuthMixin(object):
    """
    Enforces accessibility.

    Make sure to put this Mixin before ModelView in the class inheritance
    scheme.
    """
    def is_accessible(self):
        if current_user.is_authenticated and current_user.has_role('admin'):
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user.login', next=request.url))


class MyModelView(AuthMixin, ModelView):
    """
    Model view with proper role based permissions.

    Crucial: AuthMixin must go before ModelView in above base class list.
    """
    pass


class MyAdminIndexView(AuthMixin, AdminIndexView):
    """
    Index view with proper role based permissions.

    Crucial: AuthMixin must go before AdminIndexView in above base class list.
    """
    @expose('/')
    def index(self):
        form = MyInviteForm(role=1)
        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()
