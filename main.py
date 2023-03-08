import streamlit as st
from Driver import Driver
import os
from utils.const import INPUT_PATH
from utils.utils import get_random_text

header = st.container()
main = st.container()
footer = st.container()

class GUI(object):
    def __init__(self) -> None:

        if 'file_name' not in st.session_state:
            st.session_state['file_name'] = ''
        if 'out_file_name' not in st.session_state:
            st.session_state['out_file_name'] = ''
        if 'attr_df' not in st.session_state:
            st.session_state['attr_df'] = ''
        if 'mask_txt' not in st.session_state:
            st.session_state['mask_txt']=''
        self.driver = Driver()
        
        self.df = None
    def make_header(self):
        with header:
            _,c=st.columns((3,1))
            with _:
                st.title('AI based DataExtraction and Encryption')
            with c:
                st.image('waspak.jpg',width=200)
    def mask_contents(self):
        msk_txt = st.text_input(label='Please Enter Masking Text')
        if not msk_txt:
            msk_txt = get_random_text()
        st.session_state.mask_txt=msk_txt
    def make_body(self):
        
        self.mask_contents()
        btn = st.button('Extract Data and Mask')
        tab1, tab2 , tab3= st.tabs(["Attributes", "Contents","Mask Contents"])
        if btn:
            self.driver.process(input_file=st.session_state.file_name,
                                            output_file=st.session_state.out_file_name,
                                            mask_text=st.session_state.mask_txt)
            
            with tab1:
                df = self.driver.attr_df
                st.session_state.attr_df = df
                st.dataframe(st.session_state.attr_df)
            with tab2:
                st.text(self.driver.file_contents)
            with tab3:
                st.text(self.driver.mask_contents)
        
    def make_main(self):
        uploaded_file = st.file_uploader("Choose a file",type=["docx"])
        if uploaded_file:
            
            st.session_state.file_name = INPUT_PATH+uploaded_file.name
            if not os.path.exists('output'):
                os.mkdir('output')
            st.session_state.out_file_name = 'output/'+uploaded_file.name

            self.make_body()

    def run(self):
        self.make_header()
        self.make_main()
            
                
if __name__ == "__main__":
    app = GUI()
    app.run()
        