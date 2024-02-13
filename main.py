from flask import Flask, jsonify, request
from characterai import PyCAI

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return get_chat()
    elif request.method == 'POST':
        return send_message()

def get_chat():
    try:
        token = "34f5788ba1f0cfcb8b8f03437c732bad6e0abd2a"
        client = PyCAI(token)

        char = "cce81c57a2260bdbb1c89782e9a78b544d66e651"

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
        return jsonify({'error': str(e)})

def send_message():
    if 'msg' in request.json:
        try:
            msg = request.json['msg']
            token = "34f5788ba1f0cfcb8b8f03437c732bad6e0abd2a"
            client = PyCAI(token)

            char = "cce81c57a2260bdbb1c89782e9a78b544d66e651"

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
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Invalid request or missing "msg" in JSON payload'})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
