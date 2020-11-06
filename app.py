from flask import Flask, render_template, request, redirect, url_for
from Profilers import UserProfiler
import UI
app = Flask(__name__)


@app.context_processor
def utility_processor():
    return dict(get_color=UI.get_color,
                get_tag=UI.get_tag)


@app.route('/user/<user>', methods=['GET','POST'])
def user(user):
    if request.method == 'GET':
        try:
            us = UserProfiler(user)
            return render_template('index.html', user=user, reports=us.get_yearly_report_table())
        except Exception:
            return render_template('error.html')
    return redirect(url_for('user',user=request.form['user']))


@app.route('/', methods=['GET','POST'])
def start():
    if request.method == 'POST':
        if request.form['user'] == '':
            return render_template('error.html')
        return redirect(url_for('user',user=request.form['user']))
    return render_template('start.html')


if __name__ == '__main__':
    app.run()
