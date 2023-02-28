import docx2txt
import re 
text = docx2txt.process("/home/ali/Desktop/waspak.co/NER_Project/Aleshia Tomkiewicz.docx")
text1 = text.lower()
lines = text1.split('\n')
orignal_lines = text.split('\n')
pattern = r"(?<=check it\s).*"
match = re.search(pattern, text)

# text_to_search = match.group(0)
pattern = r"([a-zA-Z\s]+):\s*([0-9a-zA-Z\-]+)"
print(text)
matches = re.findall(pattern, text_to_search)
print(matches)
# account_number = re.findall(r"\b\d{8}\b(?!\d)", text)
# for j,l in enumerate(lines):
#     if ('hey' in l ) or ('hi' in l ) or ('hello' in l ):
#         l=l.split(' ')
#         first_name=l[1]
#         last_name =l[-1]
    
    
