import subprocess
from apacheconfig import *

            
options = {
    'Listen': True
}
    
with make_loader(**options) as loader:
    config = loader.load('myhttpd.conf')



ifModules = dict()
fields = dict()

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
    fields['file_accessibility'] = fileAccessibility


# printAllFields()
ifModulesCaller()
getFileAccessibility()


fields['listening_port'] = config['Listen']
fields['user'] = ifModules['unixd_module']['User']
fields['group'] = ifModules['unixd_module']['Group']
fields['server_name'] = config['ServerName']
fields['error_log_directory'] = config['ErrorLog']
fields['log_level'] = config['LogLevel']
fields['log_format'] = ifModules['log_config_module']['LogFormat']
fields['custom_log_config'] = ifModules['log_config_module']['CustomLog']
fields['alias_web_path'] = ifModules['alias_module']['ScriptAlias']

printLine()
print("REQUIRED FIELDS ARE")
printLine()
for items in fields:
        print("KEY : ",items)
        print("VALUE : ",fields[items])
        printLine()
