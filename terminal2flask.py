from flask import Flask, render_template, jsonify, request
from flask.ext.socketio import SocketIO, emit
import logging
from threading import Thread
logging.basicConfig()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
# thread = None
@app.route('/')
def index():
    return render_template('index.html')

# this bit seems to be needed to register the /test endpoint. otherwise does nothing
@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})


@app.route('/message',methods=['GET'])
def get_message():
    if request.method == 'GET':
        msg=request.args.get('message')
        print msg
        thread = Thread(target=bgthread,args=(msg,))
        thread.start()
        return msg
    else:
        return 'FAIL'


def bgthread(msg):
    socketio.emit('my response',{'data': msg},
                          namespace='/test')

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)