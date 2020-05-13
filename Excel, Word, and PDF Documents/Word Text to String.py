import docx

#get all text from word document in string

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('/Users/rahul/Documents/Programming/Automating the Boring Stuff with Python /excel, word, and pdf documents/demo.docx'))
