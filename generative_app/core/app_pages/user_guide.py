import os
import sys
import time
from typing import Dict, Union
import shutil
from pathlib import Path
import streamlit as st
from auth.auth_connection import AuthSingleton
import ui.chat_init as chat_init
from hydralit import HydraHeadApp
from streamlit.delta_generator import DeltaGenerator


class UserGuide(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self) -> None:
        user_guide_tab, demo_tab = st.tabs(["User Guide", "Demonstrations"])
        with user_guide_tab:
            st.write("This page showcase the elements AppifyAi can display. It will help you better interact with the bot by using the correct words it'll understand.")

            with st.expander("Text elements"):
                st.header("This is a header")
                st.subheader("This is a subheader")

            st.info("Section is construction...")

        with demo_tab:
            with st.expander("Camera input demo"):
                # Check if the user is already logged in
                st.video("demo/camera_input_demo.mov")
            with st.expander("Data stats"):
                st.video("demo/complex_example.mov")