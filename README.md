# Chat Application

This repository contains a simple multi-client chat application implemented using Python's socket and threading modules. The application supports multiple commands for enhanced user interaction, including video recording and voice-to-text capabilities, as well as a mini-game feature.

## Features

- **Broadcast Messages:** All connected clients can send and receive messages from everyone in the chat room.
- **Nickname Management:** Users can choose their nicknames and change them anytime with the `/nick <new_nickname>` command.
- **Client List:** Users can see a list of connected clients using the `/list` command.
- **Private Messaging:** Send private messages to specific users with the `/whisper <nickname> <message>` command.
- **Admin Commands:** Admins can kick or ban users using `/kick <nickname>` and `/ban <nickname>`.
- **Help Command:** Provides a list of available commands using `/help`.
- **Video Recording:** Clients can start video recording using the `/camera` command.
- **Voice-to-Text:** Clients can start and stop voice-to-text using the `/voice_start` and `/voice_stop` commands.
- **Mini-Game:** Clients can start mini-games using the `/snake_minigame` and `/ball_minigame` commands and view the scoreboard using `/scoreboard`.

## Server

The server handles incoming connections and client management, including broadcasting messages to all clients and handling specific commands like listing clients, nickname changes, and administrative actions.

## Client

The client connects to the server, allows users to send and receive messages, and execute commands to interact with the chat room. Additionally, the client can start and stop video recording, and voice-to-text, and play a mini-game on command.

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Bartek-Mal/Python_cmd_chat.git
    cd into cloned repository
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
- `/voice_start` - Start voice-to-text
- `/voice_stop` - Stop voice-to-text
- `/snake_minigame` - Start a snake mini-game
- `/ball_minigame` - Start a shooting mini-game 
- `/scoreboard` - Show the scoreboard for the mini-game
- `/group <group_name>` - Create a group
- `/invite_to_group <group_name> <nickname>` - Invite a user to a group
- `/accept_group <group_name>` - Accept an invite to a group

## Additional Setup

- **Voice Recognition:** Ensure `speech_recognition` and `pyttsx3` libraries are installed. Install them using:
    ```bash
    pip install SpeechRecognition pyttsx3
    ```

- **Mini-Game Integration:** Place the `minigame` module inside a `usable` directory. Ensure any dependencies for the mini-game are met.

## Creating an Executable for Camera Recording

To create an executable file for `camera_recording.py` using `auto-py-to-exe`, follow these steps:

1. **Install auto-py-to-exe:**
    ```bash
    pip install auto-py-to-exe
    ```

2. **Run auto-py-to-exe:**
    ```bash
    auto-py-to-exe
    ```

3. **Configure auto-py-to-exe:**
    - In the auto-py-to-exe interface, select `camera_recording.py` as the script to convert.
    - Choose `One File` and `Window Based` options.
    - Click on the `Convert .py to .exe` button.

4. **Move the executable:**
    - After the conversion is complete, move the generated `camera_recording.exe` file to the `usable` directory.

By following these steps, you will have a fully functional chat application with advanced features like video recording, voice-to-text, and mini-games.
