import pypdf
import re

def extract_outline(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    text = '\n'.join([page.extract_text() for page in reader.pages])
    
    # Simple regex to catch Roman Numeral titles (e.g. I. INTRODUCTION) and alphabet subtitles (e.g. A. Model Selection)
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if re.match(r'^[IVX]+\.\s+[A-Z\s]+$', line) or re.match(r'^[A-Z]\.\s+[A-Z][a-zA-Z\s]+', line):
            lines.append(line)
    return lines

ref_lines = extract_outline('/Users/krittinsetdhavanich/Documents/spoton/JubJones-SRS/JCSSE PAPER/Real Thai National ID Detection.pdf')
with open('ref_toc.txt', 'w') as f:
    f.write('\n'.join(ref_lines))

my_lines = extract_outline('/Users/krittinsetdhavanich/Documents/spoton/JubJones-SRS/JCSSE PAPER/conference_101719.pdf')
with open('current_toc.txt', 'w') as f:
    f.write('\n'.join(my_lines))
