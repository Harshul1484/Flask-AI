# from flask import Flask, jsonify, request
# from characterai import PyCAI

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'GET':
#         data = "hello world"
#         return jsonify({'data': data})

# @app.route('/chat/<string:msg>', methods=['GET'])
# def disp(msg):
#     token = "34f5788ba1f0cfcb8b8f03437c732bad6e0abd2a"
#     client = PyCAI(token)

#     char = "AbuIXFqY7EsLrOjUDLR0bDNYwqU6MDQyAKtzGIMeLI4"

#     chat = client.chat.get_chat(char)
#     participants = chat['participants']

#     if not participants[0]['is_human']:
#         tgt = participants[0]['user']['username']
#     else:
#         tgt = participants[1]['user']['username']

#     data = client.chat.send_message(chat['external_id'], tgt, msg)

#     name = data['src_char']['participant']['name']
#     text = data['replies'][0]['text']

#     return jsonify({'data': text})

# @app.route('/chat', methods=['POST'])
# def chat():
#     if request.method == 'POST' and 'msg' in request.json:
#         msg = request.json['msg']
#         token = "34f5788ba1f0cfcb8b8f03437c732bad6e0abd2a"
#         client = PyCAI(token)

#         char = "AbuIXFqY7EsLrOjUDLR0bDNYwqU6MDQyAKtzGIMeLI4"

#         chat = client.chat.get_chat(char)
#         participants = chat['participants']

#         if not participants[0]['is_human']:
#             tgt = participants[0]['user']['username']
#         else:
#             tgt = participants[1]['user']['username']

#         data = client.chat.send_message(chat['external_id'], tgt, msg)

#         name = data['src_char']['participant']['name']
#         text = data['replies'][0]['text']

#         return jsonify({'reply': text})
#     else:
#         return jsonify({'error': 'Invalid request or missing "msg" in JSON payload'})

# if __name__ == '__main__':
#     app.run(debug=False,host='0.0.0.0')



# New Code
from flask import Flask, jsonify, request
from characterai import PyAsyncCAI
import asyncio

app = Flask(__name__)

async def main():
    client = PyAsyncCAI('34f5788ba1f0cfcb8b8f03437c732bad6e0abd2a')

    # Get chat information
    char = "AbuIXFqY7EsLrOjUDLR0bDNYwqU6MDQyAKtzGIMeLI4"
    chat = await client.chat.get_chat(char)
    participants = chat['participants']

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']

    # Chat loop
    while True:
        message = input('You: ')

        data = await client.chat.send_message(chat['external_id'], tgt, message)

        name = data['src_char']['participant']['name']
        text = data['replies'][0]['text']

        print(f"{name}: {text}")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

@app.route('/chat', methods=['POST'])
async def chat():
    if request.method == 'POST' and 'msg' in request.json:
        msg = request.json['msg']
        client = PyAsyncCAI('YOUR_TOKEN')

        char = "AbuIXFqY7EsLrOjUDLR0bDNYwqU6MDQyAKtzGIMeLI4"

        chat = await client.chat.get_chat(char)
        participants = chat['participants']

        if not participants[0]['is_human']:
            tgt = participants[0]['user']['username']
        else:
            tgt = participants[1]['user']['username']

        data = await client.chat.send_message(chat['external_id'], tgt, msg)

        name = data['src_char']['participant']['name']
        text = data['replies'][0]['text']

        return jsonify({'reply': text})
    else:
        return jsonify({'error': 'Invalid request or missing "msg" in JSON payload'})

if __name__ == '__main__':
    asyncio.run(main())
    app.run(debug=False, host='0.0.0.0')
