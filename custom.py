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

def show_custom(html):
    st.markdown(html, unsafe_allow_html=True)