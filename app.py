
from flask import Flask


import logging

import settings

from core.postgres import PostgresConnection

from core.utils import recursive_filtering, mount_response_message

from entities.article import Article
from entities.project import Project


app = Flask(__name__)


log = logging.getLogger(__name__)

postgres_connection = PostgresConnection('Backend Data')

@app.route("/get/articles", methods=['GET'])
def list_articles():
    try:
        response = postgres_connection.retrieve_all('Articles')

        result = recursive_filtering(response, 0, [])
        return result

    except Exception: # pylint: disable=broad-exception-caught
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)
        return out

@app.route("/get/article/<id>", methods=['GET'])
def list_single_articles(id: int): # pylint: disable=redefined-builtin
    try:
        response = postgres_connection.retrieve_single('Articles', id=id)

        log.info(f'Article retrieved with the following id: {id}')
        return response

    except Exception: # pylint: disable=broad-exception-caught
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)
        return out


@app.route("/delete/article/<id>", methods=['DELETE'])
def delete_article(id: int): # pylint: disable=redefined-builtin
    try:
        postgres_connection.delete("Articles", id=id)

        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)

    except Exception: # pylint: disable=broad-exception-caught
        out = mount_response_message('failed', settings.HTTP_BAD_REQUEST)

    return out


@app.route('/get/projects', methods=['GET'])
def list_projects():
    try:
        breakpoint()
        response = postgres_connection.retrieve_all('Projects')
        log.info('Projects retrieved')
        return response

    except Exception: # pylint: disable=broad-exception-caught
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)
        return out

@app.route('/get/project/<id>', methods=['GET'])
def list_project(id: int): # pylint: disable=redefined-builtin
    try:
        response = postgres_connection.retrieve_single('Projects', id=id)

        result = recursive_filtering(response, 0, [])
        return result

    except Exception: # pylint: disable=broad-exception-caught
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)
        return out


@app.route('/delete/project/<id>', methods=['DELETE'])
def delete_project(id: int): # pylint: disable=redefined-builtin
    try:
        postgres_connection.delete('Projects', id=id)
        out = mount_response_message('OK', settings.HTTP_OK_REQUEST)

    except Exception: # pylint: disable=broad-exception-caught
        out = mount_response_message('ERROR', settings.HTTP_BAD_REQUEST)

    return out