import streamlit as st

with st.form(key='profile_form'):
    #テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    #セレクトボックス
    age_categoiry = st.selectbox('年齢', ['10代', '20代', '30代', '40代', '50代'])

    #複数選択
    hobby = st.multiselect('趣味', ['野球', 'サッカー', 'テニス', 'バスケットボール'])

    #年月日
    # start_date = st.date_input('開始日',datetime.date(2025,1,1))

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'{name}さん、こんにちは！{address}にお住まいですね！')
        st.text(f'年齢：{age_categoiry}')
        st.text(f'趣味：{",".join(hobby)}')