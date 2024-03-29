# Python Flask Example

This is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app that serves a simple JSON response.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/zUcpux)

## ✨ Features

- Python
- Flask

## 💁‍♀️ How to use

- Install Python requirements `pip install -r requirements.txt`
- Start the server for development `python3 main.py`

## 🚀 Endpoints

### Home

- **URL:** /
- **Method:** GET
- **Description:** Returns a simple JSON response with a "data" key containing the string "hello world".

### Chat Display

- **URL:** /chat/{msg}
- **Method:** GET
- **Description:** Sends the provided message to the chat and returns the response from the chat as JSON.

### Chat

- **URL:** /chat
- **Method:** POST
- **Description:** Sends a message provided in the request payload to the chat and returns the response from the chat as JSON.
