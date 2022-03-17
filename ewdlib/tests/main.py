import sys

sys.path.insert(0, '')

from ewdlib import ewdlib

#We create a new prj folder
ewdlib.new(foldername='test folder')

#We Create a new file
ewdlib.create(filename="index.html", page_title="Hello World")

#We Create 