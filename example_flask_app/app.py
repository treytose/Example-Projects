from flask import Flask, render_template, request, redirect, url_for
from lib.libgoal import Goal

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/create_goal', methods=['POST'])
def create_goal():
    form_data = request.form.to_dict()

    print('My Form Data: ', form_data)

    goal = Goal()
    goal.create_goal(form_data['my_goal'])
    return redirect(url_for('index_page'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)