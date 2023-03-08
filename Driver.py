from FillesDB import FilesDB
from Masker import Masker
from glob import glob
import os

class Driver(object):
    def __init__(self) -> None:
        self.file_db=FilesDB()
        self.masker = Masker()
        self.reterived_file = ''
        self.input_file = ''
        self.output_file = ''
        self.file_contents = ''
        self.mask_contents = ''
        self.attr_df = ''

    def process(self,input_file,output_file,mask_text):
        try:
            self.reterived_file = self.file_db.process_file(file_path=input_file)
            self.file_contents = self.file_db.in_text
            self.attr_df = self.file_db.df
            self.masker.mask_file(mask_text,input_file,output_file=output_file,attributes_csv=self.reterived_file)
            self.mask_contents = self.masker.output_txt
        except Exception as e:
            print('[-] Something Went Wrong', e)
    def process_directory(self,input_dir,output_dir,mask_list):
        try:
            self.reterived_file = self.file_db.process_files(file_paths=input_dir)
            input_files = glob(input_dir+'*.docx')
            for i,input_file in enumerate(input_files):
                output_file = output_dir+'/'+os.path.basename(input_file)
                self.masker.mask_file(mask_list[i],input_file,output_file=output_file,attributes_csv=self.reterived_file)
        except Exception as e:
            print('[-] Something Went Wrong', e)


