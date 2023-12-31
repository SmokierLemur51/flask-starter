from flask import Blueprint, render_template


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route("/")
def portal():
    context = {'title': "StarterProject"}
    return render_template('portal.html', context=context)