# Chat Application

This repository contains a simple multi-client chat application implemented using Python's socket and threading modules. The application supports multiple commands for enhanced user interaction.

## Features

- **Broadcast Messages:** All connected clients can send and receive messages from everyone in the chat room.
- **Nickname Management:** Users can choose their nicknames and change them anytime with the `/nick <new_nickname>` command.
- **Client List:** Users can see a list of connected clients using the `/list` command.
- **Help Command:** Provides a list of available commands using `/help`.
- **Private Messages:** Send private messages to specific users using the `/whisper <nickname> <message>` command.
- **Admin Commands:** Admin can kick or ban users with the `/kick <nickname>` and `/ban <nickname>` commands.
- **Camera Recording:** Start and stop camera recording using the `/camera` command.
- **Voice Commands:** Start and stop voice-to-text using the `/voice_start` and `/voice_stop` commands.

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
- `/whisper <nickname> <message>` - Send a private message to a specific user
- `/kick <nickname>` - Kick a user (admin only)
- `/ban <nickname>` - Ban a user (admin only)
- `/camera` - Start and stop camera recording, press 'r' to toggle recording, press 'q' to quit
- `/voice_start` - Start voice-to-text
- `/voice_stop` - Stop voice-to-text

## Using the `/camera` Command

To use the `/camera` command, you need to create an executable from the `camera_recording.py` script. Follow these steps to set it up:

1. **Install `auto-py-to-exe`:**
    ```bash
    pip install auto-py-to-exe
    ```

2. **Convert `camera_recording.py` to an executable:**
    - Run `auto-py-to-exe` in your terminal:
        ```bash
        auto-py-to-exe
        ```
    - In the interface:
        - Select `camera_recording.py` as the script to convert.
        - Choose "One File" in the "Output" section.
        - Click "Convert .py to .exe".

3. **Place the executable in the `usable` folder:**
    - After conversion, move the generated `camera_recording.exe` to the `usable` folder within your project directory.

4. **Ensure all necessary dependencies are installed:**
    - The `camera_recording.py` script requires the following libraries:
        ```bash
        pip install opencv-python pyaudio wave moviepy
        ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to contribute to this project by opening issues or submitting pull requests.
