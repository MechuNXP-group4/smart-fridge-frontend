import streamlit as st

def make_icon(icon, size, color, align):
    return f'''
        <div style="font-size:{size}rem; color:{color}; text-align:{align};">
            <i class="mdi mdi-{icon}"></i>
        </div>
    '''

def make_text(text, size, color, align):
    return f'''
        <div style="font-size:{size}rem; color:{color}; text-align:{align};">
            {text}
        </div>
    '''

def make_list_item(icon, label, value):
    return f'''
        <div class="list-item">
            <div class="icon">
                <i class="mdi mdi-{icon}"></i>
            </div>
            <div class="right">
                <div class="label">{label}</div>
                <div class="value">{value}</div>
            </div>
        </div>
    '''

def show_custom(html):
    st.markdown(html, unsafe_allow_html=True)