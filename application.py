from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/state')
def state():
    return render_template('state.html', title='By State')


@app.route('/school')
def school():
    return render_template('school.html', title='By School')


@app.route('/team')
def team():
    return render_template('team.html', title='The Team')


@app.route('/tools')
def tools():
    return render_template('tools.html', title='Tools')


if __name__ == '__main__':
    # for dataset in open('static/datasets'):
    #     data = load_data(dataset)

    app.run()
