from flask import Flask, jsonify, render_template, request
import json
from pathlib import Path
from requetor import *

def get_path():
    p = Path.cwd()
    return str(p)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify( ["hello world, here are some route available",
        "/all for all article scrapped",
        "/by_name to get a specified article",
        "exemple : /by_name?article_name=High-growth startups should start de-risking their path to IPO now",
        "/by_author to get all the article written by a specified author",
        "/by_category to get all the article in a category"] )

@app.route('/all', methods=['GET'])
def all():
    data = get_all_article()
    return jsonify(data)

@app.route('/by_name', methods=['GET'])
def name():
    article_name = request.args.get('article_name')
    data = get_article_by_name(article_name)
    return jsonify(data)

@app.route('/by_author', methods=['GET'])
def author():
    article_author = request.args.get('article_author')
    data = get_article_by_author(article_author)
    return jsonify(data)

@app.route('/by_category', methods=['GET'])
def cat():
    article_category = request.args.get('article_category')
    data = get_article_by_category(article_category)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)