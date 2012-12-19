from flask import Flask, g, render_template
from views import *
import time

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404

@app.before_request
def before_request():
    g.start = time.time()

@app.after_request
def after_request(response):
    diff = time.time() - g.start
    if app.debug:
        print "Exec time: %s" % str(diff)

    if response.response:
        response.response[0] = response.response[0].replace('__EXECUTION_TIME__', str(diff))
        response.headers["content-length"] = len(response.response[0])

    return response


app.add_url_rule('/', view_func=ShowRoom.as_view('ShowRoom'))
