
from flask import Flask
from flask import request

from asgiref.wsgi import WsgiToAsgi

import settings

from core.postgres import PostgresConnection
from core.log import Log

from entities.article import Article
from entities.project import Project

app = Flask(__name__)

asgi_app = WsgiToAsgi(app)

log = Log('endpoints-log')

postgres_connection = PostgresConnection('test-new-infra')

@app.route("/get/articles", methods=['GET'])
def list_articles():
    try:
        response = postgres_connection.retrieve_all('Articles')
        log.info('Articles retrieved')
        return response

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to retrieve articles. {error}')
        out = {
            'response': 'failed',
            'status_code': settings.HTTP_BAD_REQUEST
        }
        return out

@app.route("/get/article/<id>", methods=['GET'])
def list_single_articles(id: int): # pylint: disable=redefined-builtin
    response = postgres_connection.retrieve_single('Articles', id=id)

    log.info(f'Article retrieved with the following id: {id}')
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

    log.info('Article Created')

    return out

@app.route("/delete/article/<id>", methods=['DELETE'])
def delete_article(id: int): # pylint: disable=redefined-builtin
    postgres_connection.delete("Articles", id=id)

    out = {
        'response': 'OK',
        'status_code': settings.HTTP_OK_REQUEST
    }

    log.info(f'Article with id {id} was deleted successfully')

    return out


@app.route("/update/article/<id>", methods=['PUT'])
def update_article(id: int): # pylint: disable=redefined-builtin
    update_data = request.get_json()

    title = update_data.get('Title')
    content = update_data.get('Content')
    description = update_data.get('Description')
    image_url = update_data.get('image_url')

    log.info(type(update_data))

    postgres_connection.update("Articles", id=id, title=title, content=content, description=description, image_url=image_url)

    out = {
        'response': 'OK',
        'status_code': settings.HTTP_OK_REQUEST
    }

    log.info('Article updated successfully')

    return out


#==============================================
# project endpoints
#==============================================
@app.route('/get/projects', methods=['GET'])
def list_projects():
    response = postgres_connection.retrieve_all('Projects')
    log.info('Projects retrieved')

    return response


@app.route('/get/project/<id>', methods=['GET'])
def list_project(id: int): # pylint: disable=redefined-builtin
    response = postgres_connection.retrieve_single('Projects', id=id)

    log.info('Project Retrieved')
    return response


@app.route('/create/project', methods=['POST'])
def create_project():
    project_data = request.get_json()

    project = Project(
        title=project_data['title'],
        description=project_data['description'],
        content=project_data['content'],
        image_url=project_data['image_url']
    )

    postgres_connection.insert('Projects',
                               id=project.id,
                               title=project.title,
                               description=project.description,
                               content=project.content,
                               image_url=project.image_url,
                               url_title=project.url_title,
                               date=project.date,
                               created_at=project.creation_time
                            )

    out = {
        'response': 'OK',
        'status_code': settings.HTTP_OK_REQUEST
    }

    log.info('Project Created')

    return out


@app.route('/delete/project/<id>', methods=['DELETE'])
def delete_project(id: int): # pylint: disable=redefined-builtin
    postgres_connection.delete('Projects', id=id)
    out = {
        'response': 'OK',
        'status_code': settings.HTTP_OK_REQUEST
    }

    log.info(f'Project with id {id} was deleted successfully')

    return out


@app.route('/update/project/<id>', methods=['PUT'])
def update_project(id: int): # pylint: disable=redefined-builtin
    update_data = request.get_json()

    title = update_data.get('title')
    description = update_data.get('description')
    image_url = update_data.get('image_url')
    content = update_data.get('content')

    postgres_connection.update('Projects', id=id, title=title, description=description, image_url=image_url, content=content)

    out = {
        'response': 'OK',
        'status_code': settings.HTTP_OK_REQUEST
    }

    log.info('Project updated successfully')

    return out
