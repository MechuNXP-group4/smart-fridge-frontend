from datetime import datetime, timedelta

import streamlit as st

import aiohttp
import asyncio

from items import *
from custom import *

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

def display_item(item, expired):
    item_id = int(item['item_id'])
    image = item_images[item_id]
    name = item_name[item_id]
    count = item['count']
    exp_time = str(datetime.strptime(item['timestamps'][0], '%Y-%m-%d %H:%M:%S') + \
        timedelta(seconds=item_durability[item_id]))

    st.image(image)
    st.subheader(name)
    show_custom(make_list_item('pound-box', '庫存數量', count))

    if expired:
        exp_time = f'<span style="color: red;">{exp_time}</span>'
    show_custom(make_list_item('clock', '最早的過期時間', exp_time))

WS_CONN = 'ws://127.0.0.1:5000/get'

error_placeholder = st.empty()
info_placeholder = st.empty()
placeholder = st.empty()

async def get_stream_data():
    async with aiohttp.ClientSession(trust_env = True) as session:
        async with session.ws_connect(WS_CONN) as websocket:
            async for msg in websocket:
                data = msg.json()
                if data['error'] == 1:
                    error_placeholder.empty()
                    info_placeholder.empty()
                    with placeholder.container():
                        show_custom(make_text('Backend Error', 1.2, 'red', 'center'))
                    continue

                items = data['data']
                if len(items) == 0:
                    error_placeholder.empty()
                    info_placeholder.empty()
                    with placeholder.container():
                        icon = make_icon(
                            'fridge-industrial-off-outline',
                            8, '#599cff', 'center'
                        )
                        text = make_text('冰箱空空的，買點食材餵飽它吧～', 1.2, '#599cff', 'center')
                        show_custom(icon + text)
                else:
                    has_expired_item = [ False ] * 4
                    has_fresh_item = [ False ] * 4
                    has_any_expired = False
                    has_any_fresh = False
                    for item in items:
                        item_id = int(item['item_id'])
                        now = datetime.now()
                        first_exp_time = datetime.strptime(item['timestamps'][0], '%Y-%m-%d %H:%M:%S') + \
                            timedelta(seconds=item_durability[item_id])
                        last_exp_time = datetime.strptime(item['timestamps'][-1], '%Y-%m-%d %H:%M:%S') + \
                            timedelta(seconds=item_durability[item_id])
                        if now > first_exp_time:
                            has_expired_item[item_id] = True
                            has_any_expired = True
                        if now <= last_exp_time:
                            has_fresh_item[item_id] = True
                            has_any_fresh = True

                    if has_any_expired:
                        with error_placeholder.container():
                            for i in range(4):
                                if has_expired_item[i]:
                                    st.error(
                                        f'冰箱裡有{item_name[i]}過期了，為了您的健康並愛護環境，建議您可以{item_handle[i]}',
                                        icon='🚨'
                                    )
                    else:
                        error_placeholder.empty()
                    if has_any_fresh:
                        with info_placeholder.container():
                            for i in range(4):
                                if has_fresh_item[i]:
                                    st.info(
                                        f'冰箱裡還有新鮮的{item_name[i]}，要不要試試看{item_cuisines[i]}',
                                        icon='ℹ️'
                                    )
                    else:
                        info_placeholder.empty()

                    with placeholder.container():
                        cols = st.columns(4)
                        for i in range(4):
                            if i < len(items):
                                with cols[i].container():
                                    display_item(items[i], has_expired_item[i])
                            else:
                                cols[i].empty()
                                has_fresh_item[i] = False

asyncio.run(get_stream_data())