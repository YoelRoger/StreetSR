from flask import Blueprint, render_template, redirect, url_for, flash
from flask_breadcrumbs import register_breadcrumb
#from ..forms.user_form import UserForm, UserEdit
from ..utilities.functions import sendRequest
#from .auth import admin_required

#from flask_login import login_required

import json

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/")

#@login_required
#@admin_required
@register_breadcrumb(user, '.', 'Users')
def index():
    req = sendRequest(method="get", url="/users", auth=False)
    users = json.loads(req.text)['Users']
    title = "Users List"
    return render_template("users.html", title=title, users=users)  # Mostrar template


"""@user.route("/add-user", methods=["GET", "POST"])
"""

"""@user.route("/edit/<int:id>", methods=["GET","POST"])"""

"""@user.route('delete/<int:id>')"""