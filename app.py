import logging

from flask import Flask
from flask import request

from core.postgres import PostgresConnection
import settings

from entities.article import Article


app = Flask(__name__)

# fix this
log = logging.getLogger(__name__)


@app.route("/get/articles", methods=['GET'])
def list_articles():

    postgres_connection = PostgresConnection('test-new-infra')

    response = postgres_connection.retrieve_all('123')

    return response

@app.route("/create/article", methods=['POST'])
def create_article():
    # get the data from the request
    article_data = request.get_json()

    # instantiate
    article = Article(
        title=article_data['title'],
        description=article_data['description'],
        content=article_data['content'],
        image_url=article_data['image_url']
    )

    postgres_connection = PostgresConnection('test-new-infra')

    postgres_connection.insert("Articles",
                               id=article.id,
                               title=article.title,
                               description=article.description,
                               created_at=article.creation_time,
                               date=article.date,
                               content=article.content,
                               image_url=article.image_url,
                               url_title=article.url_title
                            )
    
    out = {
        'response': 'OK',
        'status_code': settings.HTTP_OK_REQUEST
    }

    # return a status code 200 and a message indicating that the article was created
    # json.dumps(article.__dict__)
    return out

@app.route("/delete/articles<id>")
def delete_article(id: int):
    pass

@app.route("/update/article/<id>")
def update_article(id: int):
    pass

@app.route("/get/article/<id>")
def list_single_articles(id: int):
    pass


# project endpoints
@app.route('/get/projects', methods=['GET'])
def list_projects():
    pass


@app.route('/get/project/<id>', methods=['GET'])
def list_project(id: int):
    pass


@app.route('/create/project', methods=['POST'])
def create_project():
    pass


@app.route('/delete/project/<id>', methods=['DELETE'])
def delete_project(id: int):
    pass


@app.route('/update/project/<id>', methods=['PUT'])
def update_project(id: int):
    pass
