import requests
Personal_Access_Token = ''
Bot_ID = ''
import os
import json

#与coze交互的智能体
#Bot_ID 填botid
#Personal_Access_Token 填秘钥

# 基础信息
url = "https://api.coze.cn/v3/chat"
headers = {
    "Authorization": f"Bearer {Personal_Access_Token}",
    "Content-Type": "application/json"
}

def send_request(problem):
    # 请求体
    data = {
        "bot_id": Bot_ID ,
        "user_id": "unique_user_id_123",
        "additional_messages": [
            {
                "role": "user",
                "content": problem,
                "content_type": "text"
            }
        ],
        "stream": True,
        "auto_save_history": True
    }

    # 发送请求
    response = requests.post(url, headers=headers, json=data)
    return response

def process_response(response):
    full_response = ""
    error_message = ""
    status_code = -1

    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            if 'data:' in decoded_line:
                data_json = decoded_line.split('data:', 1)[1].strip()
                try:
                    data_dict = json.loads(data_json)
                    if isinstance(data_dict, dict):
                        status_code = data_dict.get('last_error', {}).get('code', -1)
                        if data_dict.get('type') == 'answer' and 'content' in data_dict:
                            full_response = data_dict['content']
                        error_message = data_dict.get('last_error', {}).get('msg', '')
                    # print("数据:", data_dict)
                except json.JSONDecodeError:
                    print("无法解析的数据:", data_json)
    return status_code, full_response, error_message