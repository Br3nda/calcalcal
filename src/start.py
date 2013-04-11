from bottle import route, run, template, static_file
import os
DIR = os.path.dirname(os.path.realpath(__file__))
static_dir = os.path.realpath(DIR + '/../www/')

@route('/')
def index(name='World'):
    return template('index')

@route('/<path:path>')
def callback(path):
    print path
    print static_dir
    return static_file(path, root=static_dir)

run(host='localhost', port=8080,reloader=True)