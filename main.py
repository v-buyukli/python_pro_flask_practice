import flask
import requests

from services import users_generator, hw_calculating


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", name="World")


@app.route("/requirements/")
def get_requirements():
    with open("requirements.txt", "r") as f:
        content = f.read()
    return flask.render_template("requirements.html", content=content)


@app.route("/users/generate")
def users_generate():
    try:
        number = int(flask.request.args.get("numberUsers", default=100))
    except (KeyError, ValueError):
        return flask.redirect("/")

    users = users_generator.generate_users(number)
    return flask.render_template("users_generate.html", users=users)


@app.route("/mean/")
def mean_view():
    avg_height, avg_weight = hw_calculating.get_avg_values()
    return flask.render_template("mean.html", avg_height=avg_height, avg_weight=avg_weight)


@app.route("/space/")
def space_view():
    response = requests.get("http://api.open-notify.org/astros.json").json()
    people = len(response["people"])
    return flask.render_template("space.html", people=people)


if __name__ == "__main__":
    app.run()
