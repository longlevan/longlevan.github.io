#%%
import os, platform, shutil
import string
from os.path import expanduser
import hashlib
import subprocess

# Current working directory
cwd = os.getcwd()

# Home director
osystem = platform.system()

if osystem.lower() == 'linux':
    home  = expanduser("~")
    zen_home = os.path.join(home,"zenobe")
    mendeley = r'/home/vlle/.local/share/data/Mendeley Ltd./Mendeley Desktop/Downloaded/'
elif osystem.lower() == 'windows':
    home  = "Z:\\"
    zen_home = "Y:\\"

Downloads = os.path.join(home,"Downloads")
Projects  = os.path.join(home,"Projects")

ZenDowloads = os.path.join(zen_home,"Downloads")
ZenProjects = os.path.join(zen_home,"Projects")

## FDDCNP projects
FDDCNP_YAC =  os.path.join(ZenProjects,"2018050_FDDCNP_YAC")
BiblioFDD = os.path.join(FDDCNP_YAC,"Biblio")
BiblioFDD_Building = os.path.join(BiblioFDD,"Building")
BiblioFDD_Calibration = os.path.join(BiblioFDD,"Calibration")

PEPSE = os.path.join(Projects,"pepse")
biblioPEPSE = os.path.join(PEPSE,"wp_3_2","docs","biblio")

PCC80 = os.path.join(Projects,"PCC80")
BiblioPCC80 = os.path.join(PCC80,"Biblio")



#%% 
# Downloads = r'C:\TRNSYS18\SourceCode\Types'

for (dirname, dirs, files) in os.walk(FDDCNP_YAC):
    for filename in files:
        if "type9." in filename.lower():
            subprocess.Popen(["code.cmd",os.path.join(dirname,filename)])

        if filename.endswith(".f90"):
            #print(filename)
            with open(os.path.join(dirname,filename),'r') as f:
                if "trnout" in f.read().lower():
                    print(os.path.join(dirname,filename))
                    subprocess.Popen(["code.cmd",os.path.join(dirname,filename)])
            # subprocess.Popen(["xdg-open", os.path.join(dirname,filename)])
            # shutil.move(os.path.join(dirname,filename),BiblioFDD_Calibration)

#%%
for (dirname, dirs, files) in os.walk(BiblioFDD):
    for filename in files:
        with open(os.path.join(dirname,filename)) as f:
            lines = f.readlines()
            for line in lines:
                if "energyplus" in line.lower():
                    print(os.path.join(dirname,filename))
                    # subprocess.Popen(['xdg-open',os.path.join(dirname,filename)])
                # print(f.readline())

#%%
# Find duplicate file
def chunk_reader(fobj, chunk_size = 1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def  check_for_duplicate(paths, hash = hashlib.sha1):
    hashes = {} # dictionary
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()
                for chunk in chunk_reader(open(full_path,'rb')):
                    hashobj.update(chunk)
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
                if duplicate:
                    print("Duplicate found: %s and %s" % (full_path, duplicate))
                else:
                    hashes[file_id] = full_path

def file_path2list(path):
    file_path_list = []
    for (dirname, dirs, files) in os.walk(path):
        for filename in files:
            file_path_list.append(os.path.join(dirname,filename))
    return file_path_list


# 
from PyPDF2 import PdfFileReader
def doc_overview(pdf_path):
    with open(pdf_path,'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        txt = f"""
        Information about {pdf_path}:
        Author : {information.author}
        Creator: {information.creator}
        Producer: {information.producer}
        Subject: {information.subject}
        Title: {information.title}
        Number of pages : {number_of_pages}
        """
        print(txt)
        return information


def doc_classifier(path):
    with open(path,'rb') as f:
        pass

