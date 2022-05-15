import random

class User:

  
   #3.1.1 parameterized constructor
   def __init__(self, user_id=None, username=None, password=None):
      self.user_id = user_id if user_id is not None else -1
      self.username = username if username is not None else ""
      self.password = password if password is not None else ""



   #3.1.2 generate unique user id
   def generate_unique_user_id(self):
      uni_id = 0
      while True:
         uni_id =  random.randint(1000000000,9999999999)
         
         user_admin = open('./data/result/user_admin.txt','a+')
         user_admin.seek(0)
         user_admin_data = user_admin.read()

         user_instructor = open('./data/result/user_instructor.txt','a+')
         user_instructor.seek(0)
         user_instructor_data = user_instructor.read()
         
         user_student = open('./data/result/user_student.txt','a+')
         user_student.seek(0)
         user_student_data = user_instructor.read()
        
         if str(uni_id) not in user_admin_data and user_instructor_data and user_student_data:
            break
      
      return uni_id



   #3.1.3 encryption (reuse A1 algorithm)
   def encryption(self, input_password):
      all_punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

      firstchar = all_punctuation[len(input_password)% len(all_punctuation)]
      secondchar = all_punctuation[len(input_password)%5]
      thirdchar = all_punctuation[len(input_password)%10]
      i = 1
      encryptedpass = ''
    
      for char in input_password:
         if i == 1:
            encryptedpass = encryptedpass + firstchar + char + firstchar
            i = i + 1
            continue
         if i == 2:
            encryptedpass = encryptedpass + secondchar*2 + char + secondchar*2
            i = i + 1
            continue
         if i == 3:
            encryptedpass = encryptedpass + thirdchar*3 + char + thirdchar*3
            i = 1
            continue
      encryptedpass = '^^^' +  encryptedpass + '$$$'
    
      return encryptedpass 



   #3.1.4 login
   def login(self):
      encryptedpass = self.encryption(self.password)

      user_admin = open('./data/result/user_admin.txt','a+')
      user_admin.seek(0)
      user_instructor = open('./data/result/user_instructor.txt','a+')
      user_instructor.seek(0)
      user_student = open('./data/result/user_student.txt','a+')
      user_student.seek(0)

      #check username and password
      info = self.username+';;;'+encryptedpass

      login_result = False
      login_user_role = ''
      login_user_info = 0 #use to create different types of user object 

      if info in user_admin.read() :
         login_result = True
         login_user_role = 'Admin'
         login_user_info = [self.user_id,self.username, encryptedpass]
      if info in user_instructor.read():
         login_result = True
         login_user_role = 'Instructor'
         login_user_info = [self.user_id,self.username, encryptedpass]
      if info in user_student.read():
         login_result = True
         login_user_role = 'Student'
         login_user_info = [self.user_id,self.username, encryptedpass]

      tupleresult = (login_result,login_user_role,login_user_info)
      return tupleresult
   


   #3.1.5 extract_info()
   def extract_info(self):
      print("You have no permission to extract information")



   #3.1.6 view_courses()
   def view_courses(args=[]):
      print("You have no permission to view courses")



   #3.1.7 view_users()
   def view_users(self):
      print("You have no permission to view users")



   #3.1.8 view_reviews()
   def view_reviews(args=[]):
      print("You have no permission to view reviews")



   #3.1.9 remove_data()
   def remove_data(self):
      print("You have no permission to remove data")

   

   #3.1.10 __str__()
   def __str__(self):
      encryptedpass = self.encryption(self.password)
      return str(self.user_id) + ";;;" + self.username + ";;;" + encryptedpass + '\n'
