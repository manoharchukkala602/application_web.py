import json
import random
import string
dic ={
    "age":18,
    "marks":"pass",
    "date of birth":18,
    "skill":"python",
}
data =[]
FILE_NAME ="job.json"
def load_data():
    try:
       with open(FILE_NAME,"r") as f:
          data= json.load(f)
    except FileNotFoundError:
       print("invalid")

def save_data():
   with open(FILE_NAME,"w") as f:
      json.dump(data,f,indent =4)
      print("your data saved successfully")
def registrition():
   number=int(input("Enter your mobile number or email:"))
   re =random.randint(9999,10000)
   print("your otp:",re)
   otp =int(input("Enter your otp:"))
   if otp ==re:
      print("your registrition is completed")
   else:
      print("please Enter valid otp")
      
   rep =''.join(random.choices(string.ascii_uppercase+string.digits,k=8))
   print("your id:",rep)
   #sign ={
      #"number":number,
      #"re":re,
      #"otp":otp,
      #"rep":rep,
   #}
   #data.append(sign)
   #print("data stored successfully")
   save_data()
def apply():
   name =input("Enter your  name:")
   name.upper()
   age =int(input("enter your age:"))
   adher =int(input("Enter your adher number:"))
   email =input("Enter your email:")
   father =input("Enter your father name:")
   father.upper()
   mother =input("Enter your mother name:")
   mother.upper()
   skill =input("Enter your skill:")
   

   
       
   
   job ={
       "name":name,
       "age":age,
       "adhar":adher,
       "email":email,
       "father name":father,
       "mother name":mother,
       "skill":skill,
    }
   data.append(job)
   save_data()
   d =input("Enter your id:")
   #for i in data:
      #if id ==i.get["rep"]:
         #print("your successfully enter")
      #else:
        # print("enter valid id")

def check():
   for i in data:
      if i["age"] ==dic["age"] and i["skill"]==dic["skill"]:
         print("your application is ready and your selected  and you lets catch interview at tommorrow")
      else:
         print("your not selected")
save_data()
def view_application():
   for i in data:
      print("name:",i["name"],"age:",i["age"],"adhar:",i["adhar"],"email:",i["email"],"father name:",i["father name"],"mother name:",i["mother name"],"skill:",i["skill"])

load_data()
while True:
   print("selected your process")
   print("1.registrition")
   print("2.apply")
   print("3.checked")
   print("4.view application")
   choice =input("Enter your choice:")
   if choice =="1":
      registrition()
   elif choice =="2":
      apply()
   elif choice =="3":
      check()
   elif choice =="4":
      view_application()
      break
   else:
      print("thankyou")


    

      



   
      




