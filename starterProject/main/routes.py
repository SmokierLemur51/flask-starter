from flask import Blueprint, render_template


main = Blueprint('main', __name__, template_folder="templates")


@main.route("/")
def index():
    context = {'title': "StarterProject"}
    return render_template('index.html', context=context)