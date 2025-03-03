import threading
from flask import Flask, request, jsonify
from flask_cors import CORS
from tools import *
import json
import re

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    global current_text_chunks, current_thread
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        user_message = data.get('question', '')
        print(user_message)
        response = send_request(user_message)
        status_code, answer, error_message = process_response(response)
        if status_code == 0:
            return jsonify({'answer': answer})
    return jsonify({'answer': '请求方法错误'}), 400

if __name__ == '__main__':
    app.run('127.0.0.1', 3010)
