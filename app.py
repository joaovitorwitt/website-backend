import json

import logging

from flask import Flask
from flask import request

from entities.article.article import Article


app = Flask(__name__)

log = logging.getLogger(__name__)


@app.route("/get/articles", methods=['GET'])
def list_articles():
    pass

@app.route("/create/article", methods=['POST'])
def create_article():
    article_data = request.get_json()

    article = Article(
        title=article_data['title'],
        description=article_data['description'],
        content=article_data['content'],
        image_url=article_data['image_url']
    )

    # return a status code 200 and a message indicating that the article was created
    return json.dumps(article.__dict__)



@app.route("/delete/articles<id>")
def delete_article(id: int):
    pass

@app.route("/update/article/<id>")
def update_article(id: int):
    pass

@app.route("/get/article/<id>")
def list_single_articles(id: int):
    pass
