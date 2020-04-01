import sys

from flask import Flask, redirect, url_for

HELP_MESSAGE = """
usage: main map.csv
"""

MAP_FILE = ""

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('static', filename="index.html"))


@app.route("/map")
def get_map():
    map_file = open(MAP_FILE)
    content = map_file.read()
    map_file.close()
    return content


def main():
    if len(sys.argv) < 2:
        print(HELP_MESSAGE)
        sys.exit()

    global MAP_FILE

    if len(sys.argv) >= 2:
        MAP_FILE = sys.argv[1]

    app.run()


if __name__ == '__main__':
    main()
