from bottle import route, run, template, static_file, get, post
import os
DIR = os.path.dirname(os.path.realpath(__file__))
static_dir = os.path.realpath(DIR + '/../www/')

import calcalcal.web


@get('/api/events.json')
def callback():
    return calcalcal.web.get_events()


@route('/')
def index():
    return static_file('index.html', root=static_dir)


@route('/<path:path>')
def callback(path):
    print path
    print static_dir
    return static_file(path, root=static_dir)

run(host='localhost', port=8080, reloader=True)