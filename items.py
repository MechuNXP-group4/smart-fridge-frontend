import io
import json
import requests
from PIL import Image
import base64

base_url = 'http://127.0.0.1:5000'

item_name = [
    '蘋果',
    '高麗菜',
    '小黃瓜',
    '馬鈴薯'
]

def img_to_data_url(path):
    img = Image.open(path)
    buffered = io.BytesIO()
    img.save(buffered, format='JPEG')
    b64_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return f'data:image/jpeg;base64,{b64_str}'

item_images = [
    img_to_data_url('assets/apple.jpg'),
    img_to_data_url('assets/cabbage.jpg'),
    img_to_data_url('assets/cucumber.jpg'),
    img_to_data_url('assets/potato.jpg')
]

item_durability = [
    30,
    25,
    40,
    50,
]

def get_items():
    res = requests.get(f'{base_url}/get')
    return json.loads(res.text)['data']