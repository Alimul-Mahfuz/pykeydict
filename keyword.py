


genrickey=[
    {'keyword':'for','desc':'for is used for iterate over the iterable. Smple code \n for i in print(i):print(x)'},
    {'keyword':'while','desc':'while is used for iterate over the iterable. Smple code \n while(i>5):'},
    {'keyword':'class','desc':'class is used declear a class. Smple code \n class A:'},
    {'keyword':'def','desc':'def is used for declear a function. Smaple code \n def myFunction():'},
    {'keyword':'if','desc':'if is used for check condition. Smple code \n if a>b:'},
    {'keyword':'else','desc':'elif is used for check condition. Smple code \n elif a>b:'}
]

customlist=[]
COUNTENTITY=0
class customkey:
    def __init__(self,key,desc):
        self.keydict={}
        self.keydict['key']=key
        self.keydict['desc']=desc

def UpdateDetails(sl):
    global COUNTENTITY
    sl=sl-1
    if(int(sl) not in range(0,COUNTENTITY)):
        print("SL not exist in custom keylist")
        pass
    else:
        print("1. Update keyword: ")
        print("2. Update Descripton: ")
        print("3. q to exit ")
        exit=input("Enter choice: ")
        if(exit=='q'):
            pass
        elif(int(exit)==1):
            customlist[sl].keydict['key']=input("Enter new keyword: ")
            pass
        elif(int(exit)==2):
            customlist[sl].keydict['desc']=input("Enter new description: ")
            pass

def PrintPromt():
    print('\n')
    print("==============WELCOME TO PTHON KEYWORD DICTIONARY==============")
    print("1. Add a new custom keyword")
    print("2. View keyword List")
    print("3. Update exixting keyword list")
    print("4. Search")
    print("5. Delete")
    print("6. Print your keyword List")
    a=input("Enter your choice or press q to exit:  ")
    return a
a=PrintPromt()

def Search():
    found=False
    index=0
    name=input("Enter keyword name to search: ")
    for x in genrickey:
        index=index+1
        if x['keyword']==name:
            print("keyword found on generic list")
            found=True
            print("Details of the {} found on generic list".format(name))
            print("Name: {}".format(x['keyword']))
            print("Description: {}".format(x['desc']))
            found==True
            pass
    index=0
    for x in customlist:
        index=index+1
        if x.keydict['key']==name:
            print("Keyword found on custom list")
            found=True
            print("Details of the keyword")
            print("Key name: {}".format(x.keydict['key']))
            print("Description: {}".format(x.keydict['desc']))
            ch=input("Want to update the keywordlist y/n: ")
            if(ch=='y' or ch=='Y'):
                UpdateDetails(index)
            if(ch=='n' or ch=='N'):
                print('Okay Thanks you')
            pass
    if(found==False):
        print("task doesn't exists in keyword list")

def DeleteKey():
    sl=int(input("Enter the sl to delete: "))
    sl=sl-1
    if(int(sl) not in range(0,COUNTENTITY)):
        print("SL not exist custom keylist")
        pass
    del(customlist[sl])
    print("Custom keyword Deleted Successfully")

def PrintDetails():
    ch=int(input("Enter 1 to view generic keyword 2 for custom keywrod"))
    if(ch==2):
        for i in range(len(customlist)):
            print('\n')
            print('#SL{}----------------------'.format(i+1))
            print("Keyword name: {}".format(customlist[i].keydict['key']))
            print("description: {}".format(customlist[i].keydict['desc']))
    elif(ch==1):
        for i in range(len(genrickey)):
            print('\n')
            print('#SL{}----------------------'.format(i+1))
            print("Keyword name: {}".format(genrickey[i]['keyword']))
            print("description: {}".format(genrickey[i]['desc']))

def Print():
    fname="./pythonProject/KeywordDict/data.txt"
    with open(fname,'w') as file_obj:
        for i in range(len(genrickey)):
            file_obj.writelines('\n')
            file_obj.writelines('\n#SL{}----------------------'.format(i+1))
            file_obj.writelines("\neyword name: {}".format(genrickey[i]['keyword']))
            file_obj.writelines("\nescription: {}".format(genrickey[i]['desc']))
        for i in range(len(customlist)):
            file_obj.writelines('\n')
            file_obj.writelines('\n#SL{}----------------------'.format(i+1))
            file_obj.writelines("\nKeyword name: {}".format(customlist[i].keydict['key']))
            file_obj.writelines("\ndescription: {}".format(customlist[i].keydict['desc']))


def AddCusKey():
    name=input("Enter key Name: ")
    desc=input("Enter description: ")
    myObj=customkey(name,desc)
    customlist.append(myObj)
    global COUNTENTITY
    COUNTENTITY=COUNTENTITY+1

while(a!='q'):
        
#View all the saved contacts
    if int(a)==1:
        AddCusKey()
        a=PrintPromt()
    elif int(a)==2:
        if(len(customlist)==0):
            print("Custom Keyword List is empty")
            print("Available generic keys: ")
            for i in range(len(genrickey)):
                print('\n')
                print('#SL{}----------------------'.format(i+1))
                print("Keyword name: {}".format(genrickey[i]['keyword']))
                print("description: {}".format(genrickey[i]['desc']))
        else:
            PrintDetails()       
        a=PrintPromt()
    elif int(a)==3:
        sl=int(input("Enter SL of the task: "))
        UpdateDetails(sl)
        a=PrintPromt()
    elif int(a)==4:
        Search()
        a=PrintPromt()
    elif int(a)==5:
        DeleteKey()
        a=PrintPromt()
    elif int(a)==6:
        Print()
        a=PrintPromt()


        