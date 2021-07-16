import json
import logging
from flask import Flask
app = Flask(__name__)


@app.route("/status")
def health_check():
    response = app.response_class(
        response=json.dumps({'result': 'OK - healthy'}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successful')
    return response


@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({
            'status': 'success',
            'code': 0,
            'data': {
                'UserCount': 140,
                'UserCountActive': 23
            }
        }),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successful')
    return response


@app.route("/")
def hello():
    app.logger.info('Main request successful')
    return "Hello World!"


if __name__ == "__main__":
    ## Stream logs to a file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
