from items import get_items, item_name, item_images, item_durability
from streamlit_elements import elements, mui
import streamlit as st
from datetime import datetime, timedelta

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
    exp_time = datetime.strptime(item['timestamps'][0], '%a, %d %b %Y %H:%M:%S %Z') + \
        timedelta(seconds=item_durability[item_id])

    with mui.Grid(
        item=True,
        xs=12, md=3
    ):
        with mui.Card():
            mui.CardMedia(
                component='img',
                height=250,
                src=image
            )
            with mui.CardContent():
                mui.Typography(name, variant='h4')
                with mui.List():
                    with mui.ListItem():
                        with mui.ListItemAvatar():
                            with mui.Avatar():
                                mui.icon.Tag()
                        mui.ListItemText(
                            primary='庫存數量',
                            secondary=count
                        )
                    with mui.ListItem():
                        with mui.ListItemAvatar():
                            with mui.Avatar():
                                mui.icon.AccessTime()
                        now = datetime.now()
                        color = 'red' if now > exp_time else 'rgba(0, 0, 0, 0.6)'
                        mui.ListItemText(
                            primary='最早的過期時間',
                            secondary=str(exp_time),
                            secondaryTypographyProps={
                                'color': color
                            },
                        )

with elements('content'):
    items = get_items()
    if len(items) == 0:
        mui.Typography('目前沒有東西喔')
    else:
        with mui.Grid(
            container=True,
            spacing=2,
        ):
            for item in items:
                display_item(item)
