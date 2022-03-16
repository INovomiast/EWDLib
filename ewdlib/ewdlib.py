from msilib.schema import Error
from os import *
import os


def new(foldername):
    if not path.exists(foldername):
        mkdir(foldername)
        return foldername
    else:
        raise ValueError(foldername + ' Is an existing DIR')


def create(filename, page_title, ):
    if not path.exists( foldername + '/index.html'):
        html = os.open(filename, os.O_RDWR | os.O_CREAT, path=)
        os.write(html, '<html>\n')
        os.write(html, '<head>\n')
        os.write(html, '<title>' + page_title + '</title>')
        os.write(html, '</head>')
        os.write(html, '</html>')
    else:
        raise Error(filename + 'is existing!')