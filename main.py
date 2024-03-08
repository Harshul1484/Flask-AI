import os
from flask import Flask, jsonify, request
from characterai import PyCAI

app = Flask(__name__)

# Retrieve the API token and char from environment variables
token = os.environ.get('CHARACTERAI_API_TOKEN')
char = os.environ.get('CHARACTERAI_CHAR_ID')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

@app.route('/chat/<string:msg>', methods=['GET'])
def disp(msg):
    client = PyCAI(token)

    try:
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

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST' and 'msg' in request.json:
        msg = request.json['msg']
        client = PyCAI(token)

        try:
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

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    else:
        return jsonify({'error': 'Invalid request or missing "msg" in JSON payload'}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
