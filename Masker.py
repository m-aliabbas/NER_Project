import pandas as pd
import os
from FillesDB import FilesDB
from WordProcessor import WordProcessor

class Masker(object):
    
    def __init__(self) -> None:
        self.attributes_csv = ''
        self.input_file = ''
        self.output_file = ''
        self.attributes_df = None
        self.input_txt = ''
        self.output_txt = ''
        self.enum_db = {}
        self.masking_text = ""
        self.word_processor = WordProcessor()
        self.columns = []
    def enumerate_attr(self):
        self.columns = list(self.attributes_df.columns)
        self.enum_db = {j:i for i, j in enumerate(self.columns)}
        self.enum_db_path = self.attributes_csv[:-4]+'_enums.csv'
        self.enum_df = pd.DataFrame([self.enum_db])
        self.enum_df.to_csv(self.enum_db_path)
    
    def read_files(self):
        self.attributes_df = pd.read_csv(self.attributes_csv)
        self.input_txt = self.word_processor.get_text(self.input_file)
    
    def mask_file(self,masking_text,input_file='',output_file='',attributes_csv=''):
        self.input_file = input_file
        self.output_file = output_file
        self.attributes_csv = attributes_csv
        self.masking_text = masking_text
        self.read_files()
        self.enumerate_attr()
        self.__get_mask()
        self.word_processor.write_text(text=self.output_txt,path=self.output_file)

    def __find_row(self):
        file_name = os.path.basename(self.input_file)
        for i,j in enumerate(self.attributes_df['file_name']):
            if j==file_name:
                return i
            else:
                return -1
            
    def __get_mask(self):
        text = self.input_txt
        row_index = self.__find_row()
        for attbr in self.columns:
            value = str(self.attributes_df[attbr][row_index])
            if 'Name' in attbr:
                enum = self.enum_db[attbr]
                temp_mask = self.masking_text+':'+str(enum)
                text = text.replace(value,temp_mask)
            if attbr in self.input_txt:
                enum = self.enum_db[attbr]
                temp_mask = self.masking_text+':'+str(enum)
                text = text.replace(value,temp_mask)
        self.output_txt = text
       

