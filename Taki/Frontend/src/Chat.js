// Chat.js
import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import { useLoaderData } from 'react-router-dom';

const socket = io('http://localhost:5000');

export async function loader({ params }) {
  const username = `User${Math.random()}`;
  // Join the chat room when the component mounts
  socket.emit('join', { username, room: params.room });

  
  return { username, room: params.room };
}

function Chat() {
  const [messages, setMessages] = useState([]);
  const [messageInput, setMessageInput] = useState('');
  const [targetUser, setTargetUser] = useState('');
  const {username, room} = useLoaderData()
  useEffect(() => {
    
    // Listen for incoming messages
    socket.on('message', (data) => {
      setMessages((prevMessages) => [...prevMessages, data.message]);
    });

    // Clean up the event listener when the component unmounts
    return () => {
      socket.emit('leave', { username, room });
      // Also, you might want to remove the 'leave' event listener to avoid potential issues
      socket.off('leave');
    };
  }, [username ,room]);

  const sendMessage = (e) => {
    e.preventDefault();
    const newMessage = { room, target_user: targetUser, message: messageInput, username: username };
    if (targetUser) {
      console.log(targetUser)
      socket.emit('private_message', newMessage);  // Change 'message' to 'private_message' here
    } else {
      socket.emit('message', newMessage);
    }

    // Add the sent message to the local state to update UI immediately

    setMessageInput('');
  };

  return (
    <div>
      <h1>Chat Room: {room}</h1>
      <div id="chat-box">
        {messages.map((message, index) => (
          <p key={index}>{message}</p>
        ))}
      </div>
      <form onSubmit={sendMessage}>
        <input
          type="text"
          value={messageInput}
          onChange={(e) => setMessageInput(e.target.value)}
          placeholder="Type your message"
        />
        <input
          type="text"
          value={targetUser}
          onChange={(e) => setTargetUser(e.target.value)}
          placeholder="Target user (for private message)"
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default Chat;
