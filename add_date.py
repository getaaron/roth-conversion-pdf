import os
import subprocess
import datetime
import yaml
import tempfile

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)
    rect = config['rect']
    date_page = config['date_page']
    print_range = config['print_range']

now = datetime.datetime.now()
output_file = "output-" + now.strftime("%Y-%m-%d") + ".pdf"

pdfMark = f"""[
/Subtype /FreeText
/SrcPg {date_page}
/Rect [{config["rect"]}]
/Border [0 0 0]
/DA (/HeBo 10 Tf)
/Contents ({now.strftime("%m/%d/%Y")})
/F 68
/ANN pdfmark
"""

pdfMarkFile = tempfile.NamedTemporaryFile()
with open(pdfMarkFile.name, 'w') as f:
  f.write(pdfMark)

with tempfile.NamedTemporaryFile(suffix='.pdf') as tempPdf:
  subprocess.run(['gs', '-dBATCH', '-dNOPAUSE', '-dQUIET', '-sDEVICE=pdfwrite', f'-sOutputFile={tempPdf.name}',  pdfMarkFile.name, 'input.pdf'])
  subprocess.run(['gs', '-dBATCH', '-dNOPAUSE', '-dQUIET', '-sDEVICE=pdfwrite', '-dPDFSETTINGS=/prepress', '-dPreserveAnnots=false', '-dCompatibilityLevel=1.4', f'-sOutputFile={output_file}', tempPdf.name])

#subprocess.run(['lp', f'-o page-ranges={print_range}', f'-o media=A4', '-o fit-to-page', output_file])

