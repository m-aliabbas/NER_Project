from WordProcessor import WordProcessor
from GPTInfoExtractor import GPTInfoExtractor
import os
import glob
import pandas as pd
from utils.const import API_KEY
from utils.utils import get_random_string

class FilesDB:
    def __init__(self) -> None:
        self.files_paths = []
        self.attributes = {}
        self.word_processor = WordProcessor()
        self.info_extractor = GPTInfoExtractor(api_key=API_KEY)
        self.in_text = ''
        self.df = None
        
    def __get_data(self, file_path):
        file_name = os.path.basename(file_path)[:-5]
        self.file_name = file_name
        text = self.word_processor.get_text(path=file_path)
        self.in_text = text
        attributes = self.info_extractor.get_attributes(text=text)
        # print('Here attributes will go : \n',attributes)
        attributes['file_name'] = os.path.basename(file_path)
        return file_name, attributes

    def process_files(self,file_paths,outpath=''):
        temp_data = []
        self.files_paths = glob.glob(file_paths+'*.*')
        for file_path in self.files_paths:
            key, values = self.__get_data(file_path=file_path)
            temp_data += [values]
            self.attributes[key] = values
        return self.make_csv(data=temp_data)
        

    def process_file(self,file_path,outpath=''):
        temp_data = []
        key, values = self.__get_data(file_path=file_path)
        temp_data += [values]
        self.attributes[key] = values

        return self.make_csv(data=temp_data)
    
    def make_csv(self,data=None,outpath=''):
        df = pd.DataFrame(data)
        self.df = df
        if not os.path.exists('csv_data'):
            os.mkdir('csv_data')
        outpath = 'csv_data/'+self.file_name+get_random_string()+'.csv'
        df.to_csv(outpath)
        return outpath
    


    
    
    
