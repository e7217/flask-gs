from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from apis import Api, Firstapi, WorkComplete

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# MONGO
app.config["MONGODB_SETTINGS"] = {"DB": "testing"}
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "flask+mongoengine=<3"
app.debug = True
app.config["DEBUG_TB_PANELS"] = (
    "flask_debugtoolbar.panels.versions.VersionDebugPanel",
    "flask_debugtoolbar.panels.timer.TimerDebugPanel",
    "flask_debugtoolbar.panels.headers.HeaderDebugPanel",
    "flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel",
    "flask_debugtoolbar.panels.template.TemplateDebugPanel",
    "flask_debugtoolbar.panels.logger.LoggingPanel",
    "flask_mongoengine.panels.MongoDebugPanel",
)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

api = Api(app)
socketio = SocketIO(app)
toolbar = DebugToolbarExtension(app)

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
api.add_resource(WorkComplete, '/WorkComplete')
if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app, debug=True, log_output=True)



