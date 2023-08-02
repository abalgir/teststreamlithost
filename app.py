__author__ = "abalgir"
import streamlit as st
from dotenv.main import load_dotenv
import os
load_dotenv()
st.title("BardAPI for Python")


_BARD_API_KEY=st.secrets['_BARD_API_KEY']
#_BARD_API_KEY=os.environ['_BARD_API_KEY']
#import os
from bardapi import Bard

with st.container () :

    with st.spinner ( 'Wait till Bard gets the answers...' ) :
        input_text = "What is the largest state in the USA?"

        try :
            bard = Bard ( token = _BARD_API_KEY, timeout = 20 )
            response = (bard.get_answer ( input_text ) [ 'content' ])
            st.write ( response )
        except :
            st.error ( 'Please check if you have set the Cookie ' )


