from InfoExtractor import InfoExtractor
from WordProcessor import WordProcessor
import os

class FilesDB:
    def __init__(self) -> None:
        self.files_paths = []
        self.attributes = []
        self.word_processor = WordProcessor()
        self.info_extractor = InfoExtractor()

    def __get_data(self,file_path):
        file_name = os.path.basename(file_path)[:-5]
        text = self.word_processor.get_text(path=file_path)
        attributes = self.info_extractor.get_attributes(text=text)
        return file_name,attributes
    def process_files(self):
        for file_path in self.files_paths:
            key,values = self.__get_data(file_path=file_path)
            self.attributes[key] = values
        


    