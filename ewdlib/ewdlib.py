from msilib.schema import Error
from os import *
import os


def new(foldername):
    if not path.exists(foldername):
        mkdir(foldername)
        return foldername
    else:
        raise ValueError(foldername + ' Is an existing DIR')


def create(filename, page_title):
    if not path.exists('/index.html'):
        file = os.open(filename + '.html', 'w')
        os.write(file, "<!DOCTYPE html>\n")
        os.write(file, "<html>\n")
        os.write(file, '<head>\n')
        os.write(file, '<title>' + page_title + '</title>')
        os.write(file, '</head>')
        os.write(file, "</html>\n")
    else:
        raise Error(filename + 'is existing!')
    
