import docx2txt
class WordProcessor:
    def __init__(self) -> None:
        self.file_path = ""
        self.text = ""
    def get_text(self,path):
        self.text = docx2txt.process(path)
        self.lines = len(self.text.split('\n'))
        return self.text
