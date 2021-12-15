contacts = ["abi","lavanya","rithu","priya"]
class Phonecontacts:
    def __init__(self,n,m):
        self.__name = n
        self.__mobileno = m
    def conname(self):
        self.Mobileno = input("Mobile number")
        if type(self.Mobileno) == str:
           if (len(str(self.Mobileno))==10 and len(str(self.Mobileno))!= None):
               print("saved")
           else:
                raise ValueError("must be 10 charactes")
    def contactname(self):
        self.contactname = input("Name")
        if type(self.contactname) == str:
            if(len(str(self.contactname != None))):
                    print("saved")
            else:
                    raise ValueError("Enter name")
    def addcon(self):            
                contacts.append(self.contactname)
                print (contacts)
                print ("contact added")
    def delete(self):
        self.i = input()
        for j in contacts:
            if(self.i == j):
                contacts.remove(j)
                print("Contact Deleted")
                print(contacts)
obj = Phonecontacts("Dhanvarshini","9839753086")
obj.conname()
obj.contactname()
obj.addcon()
obj.delete()
