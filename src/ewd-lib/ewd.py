#EWD-Lib dev by. INovomiast

#License: GNU 3.0 General Public License

#Imports:
from operator import index
from os import *
from sys import *

#Package Starts Here!:

#Build: Compiles and Builds all the code
def Build(include_server):
    if include_server == True:
        
    

#Create: Initializes the process
def Create(prj_name, folder_n, create_conf_file):
    if not path.exists('./'+prj_name):
        mkdir(prj_name)
        print("Folder Created!")
        index_file = open('index.html', 'w', path='./build/')
        os.write(index_file, ma)
    