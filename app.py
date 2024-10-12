
from flask import Flask
from flask import request

from flask_cors import CORS

from asgiref.wsgi import WsgiToAsgi

import settings

from core.postgres import PostgresConnection
from core.log import Log
from core.utils import recursive_filtering, mount_response_message

from entities.article import Article
from entities.project import Project


app = Flask(__name__)
CORS(app, origins=settings.CORS_ALLOWED_ORIGINS)

asgi_app = WsgiToAsgi(app)

log = Log('endpoints-log')

postgres_connection = PostgresConnection('Backend Data')

@app.route("/get/articles", methods=['GET'])
def list_articles():
    try:
        response = postgres_connection.retrieve_all('Articles')
        log.info('Articles retrieved')

        result = recursive_filtering(response, 0, [])
        return result

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to retrieve articles. {error}')
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)
        return out

@app.route("/get/article/<id>", methods=['GET'])
def list_single_articles(id: int): # pylint: disable=redefined-builtin
    try:
        response = postgres_connection.retrieve_single('Articles', id=id)

        log.info(f'Article retrieved with the following id: {id}')
        return response

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to retrieve article with the following id: {id}. {error}')
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)
        return out

@app.route("/create/article", methods=['POST'])
def create_article():
    try:
        article_data = request.get_json()

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

        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)
        log.info(f'Article Created with the following id: {article.id}')

        return out

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to create the article: {error}')
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)
        return out

@app.route("/delete/article/<id>", methods=['DELETE'])
def delete_article(id: int): # pylint: disable=redefined-builtin
    try:
        postgres_connection.delete("Articles", id=id)

        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)

        log.info(f'Article with id {id} was deleted successfully')

        return out

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to delete the article. {error}')
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)
        return out


@app.route("/update/article/<id>", methods=['PUT'])
def update_article(id: int): # pylint: disable=redefined-builtin
    try:
        update_data = request.get_json()

        title = update_data.get('Title')
        content = update_data.get('Content')
        description = update_data.get('Description')
        image_url = update_data.get('image_url')

        postgres_connection.update("Articles", id=id, title=title, content=content, description=description, image_url=image_url)

        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)

        log.info('Article updated successfully')

        return out

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to update the article. {error}')
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)
        return out


#==============================================
# project endpoints
#==============================================
@app.route('/get/projects', methods=['GET'])
def list_projects():
    try:
        response = postgres_connection.retrieve_all('Projects')
        log.info('Projects retrieved')
        return response

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to retrieve projects. {error}')
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)
        return out

@app.route('/get/project/<id>', methods=['GET'])
def list_project(id: int): # pylint: disable=redefined-builtin
    try:
        response = postgres_connection.retrieve_single('Projects', id=id)

        log.info('Project Retrieved')
        result = recursive_filtering(response, 0, [])
        return result

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to retrieve projects. {error}')
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)
        return out


@app.route('/create/project', methods=['POST'])
def create_project():
    try:
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

        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)

        log.info('Project Created')

        return out

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'failed to created the project. {error}')
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)
        return out


@app.route('/delete/project/<id>', methods=['DELETE'])
def delete_project(id: int): # pylint: disable=redefined-builtin
    try:
        postgres_connection.delete('Projects', id=id)
        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)

        log.info(f'Project with id {id} was deleted successfully')

        return out

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to delete project. {error}')
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)
        return out

@app.route('/update/project/<id>', methods=['PUT'])
def update_project(id: int): # pylint: disable=redefined-builtin
    try:
        update_data = request.get_json()

        title = update_data.get('title')
        description = update_data.get('description')
        image_url = update_data.get('image_url')
        content = update_data.get('content')

        postgres_connection.update('Projects', id=id, title=title, description=description, image_url=image_url, content=content)

        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)

        log.info('Project updated successfully')

        return out

    except Exception as error: # pylint: disable=broad-exception-caught
        log.error(f'Failed to update the project. {error}')
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)
        return out
