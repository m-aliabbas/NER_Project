import docx2txt
import pandas as pd
import openai

class GPTInfoExtractor(object):
    """
    This is GPT Based Infor Extractor for Human text in word docs
    """
    def __init__(self,api_key) -> None:
        self.text_doc = ""
        self.prompt = f" {self.text_doc} Please extract all attributes related to human from above text and return Python dictionary"
        self.attributes = []
        self.attribute_db = {}
        self.api_key = api_key
        openai.api_key = api_key
        
    def __extract_attribute(self, text):
        self.text_doc = text
        self.attribute_db = {}
        self.prompt = f" {self.text_doc} Please extract all attributes related to human from above text and return Python dictionary"
        try:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{self.prompt}"}])
            content = completion.choices[0].message.content
            self.attribute_db = eval(content)
        except Exception as e:
            print(f'Following Error Occured:\n {e}')
            pass
    
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
            self.attribute_db['First Name'] = first_name
            self.attribute_db['Last Name'] = last_name

    def __del_gpt_full_name(self):
        try:
            del self.attribute_db['Name']
        except:
            pass

    def get_attributes(self, text):

        """
        Split input text into lines and extract attributes and names from each line.
        Return a dictionary containing extracted attributes.
        """
        self.__extract_attribute(text)
        self.text_lines = text.split('\n')
        for index, text_line in enumerate(self.text_lines):
            if index < 3:
                self.__extract_name(text=text_line)
        self.__del_gpt_full_name()
        return self.attribute_db
    


# info_extractor = GPTInfoExtractor(api_key="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")
# text = docx2txt.process("/home/ali/Desktop/waspak_co/NER_Project/test/Marg Grasmick.docx")
# attr=info_extractor.get_attributes(text=text)
# info_extractor.save_csv('/home/ali/Desktop/waspak_co/NER_Project/output/Marg Grasmick.csv')
# print(attr)
