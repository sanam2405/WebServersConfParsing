import subprocess
from apacheconfig import *

            
options = {
    'Listen': True
}
    
with make_loader(**options) as loader:
    config = loader.load('myhttpd.conf')



ifModules = dict()

def ifModulesCaller():
        
    for i in range(len(config['IfModule'])):
        for items in config['IfModule'][i]:
            ifModules[items] = config['IfModule'][i][items]
            # print("KEY:")
            # print(items)
            # print("VALUE")
            # print(config['IfModule'][i][items])


def printLine():
    print("---------------------------------------------------------------------------------")

def printAllFields():

    printLine()
    print("ALL THE FIELDS ARE")
    printLine()

    for fields in config:
        print(fields,config[fields])


def getFileAccessibility():
    fileAccessibility  = subprocess.getoutput('ls -l myhttpd.conf')
    print(fileAccessibility)

# printAllFields()
ifModulesCaller()
printLine()
print("REQUIRED FIELDS ARE")
printLine()

print("Listening to PORT : ",config['Listen'])
print("USER : ",ifModules['unixd_module']['User'])
print('GROUP : ',ifModules['unixd_module']['Group'])
print("SERVER NAME : ",config['ServerName'])
print("ERROR LOG DIRECTORY : ",config['ErrorLog'])
print("LOG LEVEL : ", config['LogLevel'])
print("LOG FORMAT : ", ifModules['log_config_module']['LogFormat'])
print("CUSTOM LOG CONFIG : ", ifModules['log_config_module']['CustomLog'])
print("ALIAS WEB PATH X : ",ifModules['alias_module']['ScriptAlias'])
getFileAccessibility()
printLine()