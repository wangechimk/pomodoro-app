from flask import render_template, url_for, redirect
from . import main
from .forms import ActivityForm
from flask_login import login_required, current_user
from ..models import Activity
from datetime import datetime


@main.route('/')
def index():
    """
  View root page function that returns the index page and its data
  """

    title = 'Pomodoro'

    return render_template('index.html', title=title)


@main.route('/add-activity', methods=['POST', 'GET'])
@login_required
def add_activity():
    form = ActivityForm()
    if form.validate_on_submit():
        activity = Activity(user_id=current_user._get_current_object().id,
                            amount_time=form.amount_time.data,
                            break_time=form.break_time.data,
                            break_activity=form.break_activity.data,
                            )
        activity.save()
        return redirect(url_for('main.index'))
    return render_template("activity/activity.html", form=form)
