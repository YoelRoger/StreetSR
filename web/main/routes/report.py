from flask import Blueprint, render_template, current_app, redirect, url_for, flash, request
import json
from flask_breadcrumbs import register_breadcrumb
from ..utilities.functions import sendRequest
from ..forms.report import ReportsFilter
#from flask import make_response


report = Blueprint("report", __name__, url_prefix="/report")
@report.route("/")
@register_breadcrumb(report, '.', 'Reports')
def index():
    filter = ReportsFilter(request.args, meta={"csrf": False})
    req = sendRequest(method="get", url="/sensors-info", auth=True)
    filter.userId.choices = [(int(user["id"]), user["name"]) for user in json.loads(req.text)["Report"]]
    filter.userId.choices.insert(0, [0, "All Reports"])
    data = {}
