import re
import docx2txt
import pandas as pd


class InfoExtractor:
    """
    This class extracts information from text input using regular expressions.
    """

    def __init__(self):
        """
        Initialize the InfoExtractor object with a regular expression pattern and empty lists/dictionaries.
        """
        self.pattern = r"([a-zA-Z\s]+):\s*([0-9a-zA-Z\- @.]+)+"  # regular expression pattern
        self.attributes = []  # list of extracted attributes
        self.text_lines = []  # list of input text lines
        self.attributes_db = {}  # dictionary containing extracted attributes

    def __extract_attribute(self, text):
        """
        Extract attribute and value pairs from text using regular expression pattern and append to attributes list.
        """
        matches = re.findall(self.pattern, text)
        if matches:
            self.attributes.append(matches[0])

    def __extract_name(self, text):
        """
        Extract first and last name from text and append to attributes list.
        """

        text1 = text.lower()
        if ('hey' in text1) or ('hi' in text1) or ('hello' in text1):
            text = text.split(" ")
            try:
                first_name = text[1]
                last_name = text[-1]
            except IndexError:
                first_name, last_name = text[-1], text[-1]
            self.attributes.append(('First Name', first_name))
            self.attributes.append(('Last Name', last_name))

    def get_attributes(self, text):
        """
        Split input text into lines and extract attributes and names from each line.
        Return a dictionary containing extracted attributes.
        """
        self.text_lines = text.split('\n')
        for index, text_line in enumerate(self.text_lines):
            if index < 3:
                self.__extract_name(text=text_line)
            else:
                self.__extract_attribute(text=text_line)

        return self.__get_dict_database()

    def __get_dict_database(self):
        """
        Convert list of attributes to a dictionary.
        """
        for attribute in self.attributes:
            self.attributes_db[attribute[0]] = attribute[1]
        return self.attributes_db

    def save_csv(self,path):

        df = pd.DataFrame(self.attributes_db,index=[0])
        df.to_csv(path)
    



info_extractor = InfoExtractor()
text = docx2txt.process("/home/ali/Desktop/waspak.co/NER_Project/test/Marg Grasmick.docx")
attr=info_extractor.get_attributes(text=text)
info_extractor.save_csv('/home/ali/Desktop/waspak.co/NER_Project/output/Marg Grasmick.csv')
print(attr)
