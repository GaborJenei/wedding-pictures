import os
from flask import Flask, render_template


app = Flask(__name__)

# Get the filenames
pics_day1 = os.listdir('./static/day1')


@app.route('/')
def index():
    return render_template('index.html', pics_day1=pics_day1)


if __name__ == '__main__':
    app.run(debug=True)
