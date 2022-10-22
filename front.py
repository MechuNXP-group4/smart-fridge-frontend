from datetime import datetime, timedelta

import streamlit as st

import aiohttp
import asyncio

from items import item_name, item_images, item_durability

st.set_page_config(
    page_title='2022 梅竹黑客松 - 機智博士',
    layout='wide'
)

st.title('冰箱內的物品')

def display_item(item):
    item_id = int(item['item_id'])
    image = item_images[item_id]
    name = item_name[item_id]
    count = item['count']
    exp_time = datetime.strptime(item['timestamps'][0], '%Y-%m-%d %H:%M:%S') + \
        timedelta(seconds=item_durability[item_id])

    st.image(image)
    st.subheader(name)
    st.write(f'#️⃣庫存數量：{count}')

    now = datetime.now()
    emo = '⚠ ' if now > exp_time else ''
    st.write(f'🕒最早的過期時間：{emo}{exp_time}')

WS_CONN = 'ws://127.0.0.1:5000/get'

placeholder = st.empty()

async def get_stream_data():
    async with aiohttp.ClientSession(trust_env = True) as session:
        async with session.ws_connect(WS_CONN) as websocket:
            async for msg in websocket:
                data = msg.json()
                if data['error'] == 1:
                    continue
                items = data['data']
                if len(items) == 0:
                    placeholder.write('目前沒有東西喔')
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