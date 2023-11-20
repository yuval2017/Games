# app.py
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Dictionary to map usernames to request.sid
users = {}

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat/<room>')
# def chat(room):
#     return render_template('chat.html', room=room)


@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = data['message']
    username = data['username']
    print(f"Received message in room '{room}' from {username}: {message}")
    socketio.emit('message', {'message': f"{username}: {message}"}, room=room)

@socketio.on('private_message')
def handle_private_message(data):
    print("send private")
    room = data['room']
    message = data['message']
    username = data['username']
    target_user = data['target_user']

    print(f"Received private message in room '{room}' from {username} to {target_user}: {message}")

    # Get the request.sid for the target user from the users dictionary
    target_sid = users.get(target_user)

    if target_sid:
        # Emit the private message only to the target user
        socketio.emit('message', {'message': f"{username} to you: {message}"}, room=target_sid)
    else:
        print(f"Target user '{target_user}' not found.")

@socketio.on('join')
def on_join(data):
    username = data['username']
    users[username] = request.sid
    room = data['room']
    join_room(room)
    message = f"{username} has joined the room."
    socketio.emit('message', {'message': message}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    message = f"{username} has left the room."
    socketio.emit('message', {'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=False)
