from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from apis import Api, Firstapi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

api = Api(app)
socketio = SocketIO(app)

## url
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    send("hello")
    print('received message: ', message)

@socketio.on('mymessage')
def handle_my_custom_event(message):
    print('received event: ', message)
    socketio.emit('mymessage', message)

## api
api.add_resource(Firstapi, '/Firstapi')

if __name__ == '__main__':
    # app.run()
    socketio.run(app, debug=True, log_output=True)



