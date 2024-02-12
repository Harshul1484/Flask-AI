from flask import Flask, jsonify, request
from characterai import PyCAI

app = Flask(__name__)

@app.route('/abc', methods=['POST'])
def chat():
    if request.method == 'POST' and 'msg' in request.json:
        msg = request.json['msg']
        token = 'cce81c57a2260bdbb1c89782e9a78b544d66e651'
        client = PyCAI(token)

        char = '4WOVrCApi4JYwfYwU2e5eDeFalLOkGBw6IfUZPX1XVQ'

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
    app.run(debug=False,host='0.0.0.0')

