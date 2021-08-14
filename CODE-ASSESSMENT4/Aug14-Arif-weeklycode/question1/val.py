import re
def validate(name,mobileNumber,emailId,pincode):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        mobileNumber1=re.search("^(\+91)[6-9]\d{9}$",mobileNumber)
        print(mobileNumber1)
        emailId1=re.search( "[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailId)
        print(emailId1)  
        pincode1=re.search("^[1-9]{1}[0-9]{2}\\s{0, 1}[0-9]{3}$",pincode)
        if name1 and  mobileNumber1 and emailId1 and pincode:
            return True
        else:
            return False  