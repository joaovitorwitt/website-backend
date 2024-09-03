from flask import Flask


app = Flask(__name__)


@app.route("get/articles", methods=['GET'])
def list_articles():
    pass

@app.route("create/articles", methods=['POST'])
def create_article():
    pass

@app.route("delete/articles<id>")
def delete_article(id: int):
    pass

@app.route("update/article/<id>")
def update_article(id: int):
    pass

@app.route("get/article/<id>")
def list_single_articles(id: int):
    pass


