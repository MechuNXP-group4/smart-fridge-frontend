from datetime import datetime, timedelta
import requests

import streamlit as st

import aiohttp
import asyncio

from items import item_name, item_images, item_durability
from custom import *

base_url = '127.0.0.1:5000'

st.set_page_config(
    page_title='2022 梅竹黑客松 - 機智博士',
    layout='wide'
)

st.markdown(
    f'<link href="https://cdn.jsdelivr.net/npm/@mdi/font@6.9.96/css/materialdesignicons.min.css" rel="stylesheet" />',
    unsafe_allow_html=True
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('冰箱內的物品')

def on_mode_change():
    requests.get(f'http://{base_url}/switch')
removing_mode = st.checkbox('Removing Mode', on_change=on_mode_change)

def display_item(item):
    item_id = int(item['item_id'])
    image = item_images[item_id]
    name = item_name[item_id]
    count = item['count']
    exp_time = datetime.strptime(item['timestamps'][0], '%Y-%m-%d %H:%M:%S') + \
        timedelta(seconds=item_durability[item_id])

    st.image(image)
    st.subheader(name)
    show_custom(make_list_item('pound-box', '庫存數量', count))

    now = datetime.now()
    exp_time_str = str(exp_time)
    if now > exp_time:
        exp_time_str = f'<span style="color: red;">{exp_time_str}</span>'
    show_custom(make_list_item('clock', '最早的過期時間', exp_time_str))

WS_CONN = f'ws://{base_url}/get'

placeholder = st.empty()

async def get_stream_data():
    async with aiohttp.ClientSession(trust_env = True) as session:
        async with session.ws_connect(WS_CONN) as websocket:
            async for msg in websocket:
                data = msg.json()
                if data['error'] == 1:
                    with placeholder.container():
                        show_custom(make_text('Backend Error', 1.2, 'red', 'center'))
                    continue

                items = data['data']
                if len(items) == 0:
                    with placeholder.container():
                        icon = make_icon(
                            'fridge-industrial-off-outline',
                            8, '#599cff', 'center'
                        )
                        text = make_text('冰箱空空的，買點食材餵飽它吧～', 1.2, '#599cff', 'center')
                        show_custom(icon + text)
                else:
                    with placeholder.container():
                        cols = st.columns(4)
                        for i in range(4):
                            if i < len(items):
                                with cols[i].container():
                                    display_item(items[i])
                            else:
                                cols[i].empty()

asyncio.run(get_stream_data())