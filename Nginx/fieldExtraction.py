import crossplane
import subprocess 

payload = crossplane.parse('nginx.conf')
fields = dict()

def printLine():
    print("---------------------------------------------------------------------------------")


def printAllFields():

    printLine()
    print("ALL THE FIELDS ARE")
    printLine()
    for fields in payload:
        print("KEY : ",fields)
        printLine()
        print("VALUE : ",payload[fields])
        printLine()

def getFileAccessibility():
    fileAccessibility  = subprocess.getoutput('ls -l nginx.conf')
    print(fileAccessibility)
    # tokens = fileAccessibility.split(' ')
    # if(tokens[0]==)

printLine()
printAllFields()
printLine()

fields['file'] = payload['config'][0]['file']

# for items in payload['config'][0]['parsed']:
#     print(items)

for items in payload['config'][0]['parsed']:
    # print(items)

    if items['directive'] != 'events' and items['directive'] != 'http':
        fields[items['directive']] = items['args'] 
    else:
        for innerItems in items['block']:
            if innerItems['directive'] != 'server':
                fields[innerItems['directive']] = innerItems['args']
            else:
                for innerInnerItems in innerItems['block']:
                    fields[innerInnerItems['directive']] = innerInnerItems['args']


print("THE REQUIRED FIELDS ARE : ")
printLine()
for items in fields:
        print("KEY : ",items)
        printLine()
        print("VALUE : ",fields[items])
        printLine()

getFileAccessibility()
printLine()