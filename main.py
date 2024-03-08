import os
from flask import Flask, jsonify, request
from characterai import PyCAI

app = Flask(__name__)

# Accessing environment variables
token = os.environ.get('CHARACTERAI_API_TOKEN')
char = os.environ.get('CHARACTERAI_CHAR')

if not token or not char:
    raise ValueError("Missing CHARACTERAI_TOKEN or CHARACTERAI_CHAR environment variable.")

client = PyCAI(token)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

@app.route('/chat/<string:msg>', methods=['GET'])
def disp(msg):
    chat = client.chat.get_chat(char)
    participants = chat['participants']

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']

    data = client.chat.send_message(chat['external_id'], tgt, msg)

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    return jsonify({'data': text})

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST' and 'msg' in request.json:
        msg = request.json['msg']

        chat = client.chat.get_chat(char)
        participants = chat['participants']

        if not participants[0]['is_human']:
            tgt = participants[0]['user']['username']
        else:
            tgt = participants[1]['user']['username']

        data = client.chat.send_message(chat['external_id'], tgt, msg)

        name = data['src_char']['participant']['name']
        text = data['replies'][0]['text']

        return jsonify({'reply': text})
    else:
        return jsonify({'error': 'Invalid request or missing "msg" in JSON payload'})

if __name__ == '__main__':
    app.run(debug=True)
