# Chat Application

This repository contains a simple multi-client chat application implemented using Python's socket and threading modules. The application supports multiple commands for enhanced user interaction, including video recording capabilities.

## Features

- **Broadcast Messages:** All connected clients can send and receive messages from everyone in the chat room.
- **Nickname Management:** Users can choose their nicknames and change them anytime with the `/nick <new_nickname>` command.
- **Client List:** Users can see a list of connected clients using the `/list` command.
- **Private Messaging:** Send private messages to specific users with the `/whisper <nickname> <message>` command.
- **Admin Commands:** Admins can kick or ban users using `/kick <nickname>` and `/ban <nickname>`.
- **Help Command:** Provides a list of available commands using `/help`.
- **Video Recording:** Clients can start video recording using the `/camera` command.

## Server

The server handles incoming connections and client management, including broadcasting messages to all clients and handling specific commands like listing clients, nickname changes, and administrative actions.

## Client

The client connects to the server, allows users to send and receive messages, and execute commands to interact with the chat room. Additionally, the client can start and stop video recording on command.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/chat-application.git
    cd chat-application
    ```

2. **Run the server:**
    ```bash
    python server.py
    ```

3. **Run the client:**
    ```bash
    python client.py
    ```

4. **Set up camera recording (optional):**
    Ensure OpenCV is installed on your system. If not, install it using:
    ```bash
    pip install opencv-python
    ```
    The camera recording script will be triggered by the `/camera` command from the server.

## Commands

- `/list` - List all connected clients
- `/nick <new_nickname>` - Change your nickname
- `/whisper <nickname> <message>` - Send a private message to a specific user
- `/kick <nickname>` - Kick a user from the server (admin only)
- `/ban <nickname>` - Ban a user from the server (admin only)
- `/help` - Show available commands
- `/camera` - Start camera recording. Press 'r' to toggle recording, 'q' to quit


