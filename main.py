import asyncio
from flask import Flask, jsonify, request
from charaiPY.AsyncPyCAI2 import PyAsyncCAI2

app = Flask(__name__)

owner_id = "edbf12f4a748db6bcadfbd8505cdb8c764351299"
char = "7yDt2WH6Y_OpaAV4GsxKcY5xIQ8QT5M0kgpDQ6VAflI"
chat = "d2cc5852-0e70-417f-93e9-d3119b23d868"
author_id = "486814206"

aut_set ={
    "author_id": "486814206",
    "is_human": True,
    "name": "Are-you-feeling-okay"
}

client = PyAsyncCAI2(owner_id)

async def send_message(message):
    async with client.connect(owner_id) as chat2:
        return await chat2.send_message(char, chat, message, aut_set, Return_name=False)

@app.route('/chat', methods=['POST'])
def post_chat():
    if request.method == 'POST' and 'message' in request.json:
        message = request.json['message']
        response = asyncio.run(send_message(message))
        return jsonify({"response": response})
    else:
        return jsonify({"error": "Invalid request or missing 'message' in JSON payload."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
