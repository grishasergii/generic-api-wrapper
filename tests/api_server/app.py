from flask import Flask

app = Flask(__name__)


@app.route("/test-resource-1", methods=["GET"])
def question_random():
    """Returns a random question."""
    return {"data": "test-resource-1"}


@app.route("/tests/<resource_id>", methods=["GET"])
def get_question(resource_id):
    """Returns a question by id."""
    return {"data": resource_id}


if __name__ == "__main__":
    app.run()
