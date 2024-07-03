# Chat Application

This repository contains a simple multi-client chat application implemented using Python's socket and threading modules. The application supports multiple commands for enhanced user interaction.

## Features

- **Broadcast Messages:** All connected clients can send and receive messages from everyone in the chat room.
- **Nickname Management:** Users can choose their nicknames and change them anytime with the `/nick <new_nickname>` command.
- **Client List:** Users can see a list of connected clients using the `/list` command.
- **Help Command:** Provides a list of available commands using `/help`.

## Server

The server handles incoming connections and client management, including broadcasting messages to all clients and handling specific commands like listing clients and nickname changes.

## Client

The client connects to the server, allows users to send and receive messages, and execute commands to interact with the chat room.

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

## Commands

- `/list` - List all connected clients
- `/nick <new_nickname>` - Change your nickname
- `/help` - Show available commands

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to contribute to this project by opening issues or submitting pull requests.
