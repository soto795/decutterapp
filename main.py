import yt_dlp, time
import streamlit as st
import glob, os
import streamlit.components.v1 as components


def downloadvideo(url2,q2):
    ydl_opts = {'format':q2, 'outtmpl': r'%(uploader)s - %(title)s - [%(id)s].%(ext)s', 'restrictfilenames':True, 'forcefilename':True, 'nopart': False,'proxy': 'socks5://127.0.0.1:10808',}


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url2, download=True)
        main_uploader = info_dict['uploader']
        main_title = info_dict['title']
        main_id = info_dict['id']
        filename = ydl.prepare_filename(info_dict)
        video_name = filename 
        return video_name
		

if __name__ == '__main__':
    st.subheader('Hello')
    url = st.text_input('Enter the URL')
    url = url.replace(" ", "")
    q = '140+bv*[ext=mp4][height<=1000][protocol^=http]'
    m4a = st.checkbox("m4a")
    if m4a:
        q = '140'
    st.text( q )
    vname = downloadvideo(url,q)
    st.write(vname)
    st.video(f"./{vname}")
