import os
from flask import Flask, jsonify, request
from characterai import PyCAI

app = Flask(__name__)

# Retrieve the API token and char from environment variables
token = os.environ.get('CHARACTERAI_API_TOKEN')
char = os.environ.get('CHARACTERAI_CHAR')

if not token or not char:
    raise ValueError("Please set the CHARACTERAI_API_TOKEN and CHARACTERAI_CHAR environment variables")

client = PyCAI(token)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

@app.route('/chat/<string:msg>', methods=['GET'])
def disp(msg):
    try:
        chat = client.chat.get_chat(char)
        participants = chat.get('participants', [])
        for participant in participants:
            if not participant['is_human']:
                tgt = participant['user']['username']
                break
        else:
            tgt = None

        if tgt:
            data = client.chat.send_message(chat['external_id'], tgt, msg)
            name = data['src_char']['participant']['name']
            text = data['replies'][0]['text']
            return jsonify({'data': text})
        else:
            return jsonify({'error': 'No non-human participant found in the chat'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        if request.method == 'POST' and 'msg' in request.json:
            msg = request.json['msg']
            chat = client.chat.get_chat(char)
            participants = chat.get('participants', [])
            for participant in participants:
                if not participant['is_human']:
                    tgt = participant['user']['username']
                    break
            else:
                tgt = None

            if tgt:
                data = client.chat.send_message(chat['external_id'], tgt, msg)
                name = data['src_char']['participant']['name']
                text = data['replies'][0]['text']
                return jsonify({'reply': text})
            else:
                return jsonify({'error': 'No non-human participant found in the chat'})
        else:
            return jsonify({'error': 'Invalid request or missing "msg" in JSON payload'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
