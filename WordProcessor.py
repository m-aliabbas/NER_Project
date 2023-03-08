import docx2txt
import docx
class WordProcessor:
    def __init__(self) -> None:
        self.file_path = ""
        self.text = ""
    def get_text(self,path):
        self.text = docx2txt.process(path)
        self.lines = len(self.text.split('\n'))
        return self.text

    def write_text(self,text,path):

        doc = docx.Document()
        # add each line of the text string to the document
        
        doc.add_paragraph(text)
        
        # save the document to the specified output file path
        doc.save(path)
