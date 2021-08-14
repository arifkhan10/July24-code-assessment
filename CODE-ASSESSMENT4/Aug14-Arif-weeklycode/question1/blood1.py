import pymongo,time,smtplib,val
client = pymongo.MongoClient("mongodb://localhost:27017/")

mydatabase= client["bloodDb"]
Collection_name =mydatabase["blood1"]
blist=[]
#listemail=[]
class Blood:
    def addDonors(self,name,address,bloodgroup,pincode,mobileNumber,last_donated_date,emailId,place):
        self.name=name
        self.address=address
        self.bloodgroup=bloodgroup
        self.pincode=pincode
        self.mobileNumber=mobileNumber
        self.last_donated_date=last_donated_date
        self.emailId=emailId
        self.place=place
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        #listemail.append(email)
        dict1={"name":name,"address":address,"bloodgroup":bloodgroup,"pincode":pincode,"mobileNumber":mobileNumber,"last_donated_date":last_donated_date,"emailId":emailId,"place":place,"AddOn":current_time}
        blist.append(dict1)
obj1=Blood()
while(True):
    print("1.Add donors:")
    print("2.Search donors based on blood group:")
    print("3.Search donors based on blood group and place:")
    print("4.Update all donor details with their mobile number: ")
    print("5.delete the donor using mobile number:")
    print("6.Display the total number of donors on each blood group:")
    print("7.Immediately notification via email:")
    print("8.EXIT:")
    choice=int(input("Enter your choice :"))
    if choice==1:
        name = input("Enter the name of donor:")
        address=input("enter the address of donor:")
        bloodgroup=input("enter the bloodgroup:")
        pincode=input("enter the pincode:")
        mobileNumber=input("Enter the mobilenumber:")
        last_donated_date=input("enter the last_donated_date:")
        emailId=input("Enter the email:")
        if val.validate(name,mobileNumber,emailId,pincode):
            place=input("enter the place:")
            obj1.addDonors(name,address,bloodgroup,pincode,mobileNumber,last_donated_date,emailId,place)
            result=Collection_name.insert_many(blist)
            print(result.inserted_ids)
    if choice==2:
        b=input("enter the blood group to  search donor:")
        result=Collection_name.find({"bloodgroup":b},{"_id":0})
        for i in result:
            print(i)
    if choice==3:
        p=input("enter the blood group:")
        q=input("enter the place:")
        result=Collection_name.find({"$and":[{"bloodgroup":p},{"place":q}]},{"delflag":0})
        for i in result:
            print(i)
        blist.clear()
    if choice==4:
        p=input("enter the donor mobile no:")
        q=input("enter the donor name to be updated:")
        r=input("enter the address u want to be updated:")
        s=input("enter the pincode u want to be updated:")
        t=input("enter the place u want to be updated:")
        #result=Collection_name.update_many({"mobileNumber":p},{"delflag":0},{"$set":[{"name":q},{"address":r},{"pincode":s},{"place":t}]})
        #for i in result:
        #    print(i)
        res=Collection_name.update_one({"mobileNumber":p},{"$set":{"name":q,"address":r,"pincode":s,"place":t,"delflag":0}})
        print(res)
    if choice==5:
        p=input("enter the mobile number u want to be delete:")
        q=input("enter the blood group u want to be deleted:")
        #result=Collection_name.update_one({"mobileNumber":p},{"$set":{"delflag":1}})
        #print(result)
        res=Collection_name.update_one({"$and":[{"mobileNumber":p},{"bloodgroup":q}]},{"$set":{"delflag":1}})
        print(res)
        b=Collection_name.find({"delflag":1})
        for i in b:
            print(i)


    if choice==6:
        p=input("enter the blood group to know the count:")
        result=Collection_name.count_documents({"bloodgroup":p,"delflag":0})
        print(result)

    if choice==7:
        a=input("enter the blood group to send mail to donor:")
        result=Collection_name.find({"delflag":0},{"_id"})
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
        for i in result:
            msg="Hi,donor need for" + a + "blood group"
            #connection=smtplib.SMTP("smtp.gmail.com",587)
            #connection.starttls()
            #connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
            connection.sendmail("Arifkhanstar0786@gmail.com",i["emailId"],msg)
        connection.quit()
        print("Mail sent successfully")
        #message=input("Enter a message to all donors: ")
        #connection=smtplib.SMTP("smtp.gmail.com",587)
        #connection.starttls()
        #connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
        #connection.sendmail("Arifkhanstar0786@gmail.com",listemail,message)
        #print("!!! Email Sent !!!")
        #connection.quit()
    
    if choice==8:
        break
