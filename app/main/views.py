from flask import render_template,url_for
from . import main
# from app import app


@main.route('/')
def index():
    """
  View root page function that returns the index page and its data
  """

    title = 'Pomodoro'

    return render_template('index.html', title=title)
