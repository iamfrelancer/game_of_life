from flask import Flask, render_template, url_for, request
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    row, column = 25, 25
    if request.method == 'POST':
        row, column = request.form['row'], request.form['column']
    GameOfLife(int(row), int(column))
    return render_template('index.html', row=row, column=column)


@app.route('/live')
def live():
    life = GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    life.counter += 1
    return render_template('live.html', life=life)


if __name__ == '__main__':
    app.run(debug=True)
