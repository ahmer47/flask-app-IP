from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    ip_addr = request.remote_addr
    hostname = request.headers.get('Host')
    return '<h1> HELLO WORLD ' + 'and the Host IP : ' + hostname


@app.route('/client')
def client():
    ip_addr = request.environ['REMOTE_ADDR']
    hostname = request.headers.get('Host')
    return '<h1> HELLO WORLD ' + 'and the Host IP : ' + hostname


@app.route('/client')
def proxy_client():
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    hostname = request.headers.get('Host')
    return '<h1> HELLO WORLD ' + 'and the Host IP : ' + hostname


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
