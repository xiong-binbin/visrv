import os, base64, shutil
from . import main, api
from .interface import *
from datetime import datetime
from flask_restful import Resource
from flask import render_template, request, send_from_directory


base_path = os.getcwd() + '/store/'
pdf_path = os.getcwd() +'/app/static/pdf/'

@main.route('/')
@main.route('/article')
@main.route('/editor')
@main.route('/project')
@main.route('/tools')
def index():
    if 'chrome' == request.user_agent.browser:
        return render_template('index.html')
    else:
        return render_template('welcome.html')

@main.route('/upload/<dir>', methods=['POST'])
def upload(dir):
    f = request.files['file']
    i = len(f.filename.split('.')[-1])
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    name = now + '.' + f.filename[-i:]
    path = base_path + dir + '/' + name
    f.save(path)
    if f.filename[-i:] == 'pdf':
        shutil.copyfile(path, pdf_path + name)
    return name

@main.route('/download/<dir>', methods=['GET'])
def download(dir):
    fileName = request.args.get('file')
    return send_from_directory(base_path + dir, fileName, as_attachment=True)



@api.resource('/api/page')
class Page(Resource):
    def get(self):
        name = request.args.get('name')
        return get_page(name)
    
    def post(self):
        data = request.get_data()
        return post_page(data)

@api.resource('/api/article')
class Article(Resource):
    def get(self):
        id = request.args.get('id')
        return get_article(id)
    
    def post(self):
        data = request.get_data()
        return post_article(data)

@api.resource('/api/document')
class Document(Resource):
    def get(self):
        id = request.args.get('id')
        return get_document(id)
    
    def post(self):
        data = request.get_data()
        return post_document(data)

@api.resource('/api/tools')
class Tools(Resource):
    def post(self):
        data = request.get_data()
        return post_tools(data)

