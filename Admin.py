import re
import os

from User import User
from Course import Course
from Review import Review


class Admin(User):
    
    #3.2.1 parameterized constructor
    def __init__(self,user_id=None, username=None, password=None):
        super().__init__(user_id, username, password)

    
    #3.2.2 register admin
    def register_admin(self):
        user_admin = open('./data/result/user_admin.txt','a+')
        user_admin.seek(0)
        data_user_admin = user_admin.read()

        #check username not exist in file, register admin
        if self.username not in data_user_admin:
            newAdmin = self.__str__()
            user_admin.write(newAdmin)
        user_admin.close()



    #3.2.3 extract course info
    def extract_course_info(self):
        rawfile = open('./data/course_data/raw_data.txt','r')
        rawfile.seek(0)
        raw_data = rawfile.read()
        rawfile.close()

        # find keyword  ("course","id":) extract (any before commna)
        re_pattern_id = r'"course","id":[^,]*'
        extracted_ids  = re.findall(re_pattern_id,raw_data)
        listcourseid = []
        for txt in extracted_ids:
            id = txt.split(':')[-1]
            listcourseid.append(id)
        #find keyword ("course","id":)- (any to comma) - ("title":) extract (any before comma)
        re_pattern_title = r'"course","id":[^,]*,"title":[^,]*'
        extracted_titles  = re.findall(re_pattern_title,raw_data)
        listcoursetitle = []
        for txt in extracted_titles:
            title = txt.split('\":\"')[-1][:-1]
            listcoursetitle.append(title)
        #find keywowd ("image_50x50")- any -(,"image_100x100":), extract any until "image_304x171"
        re_pattern_image = r'"image_50x50":[^,]*,"image_100x100":[^,]*,"image_304x171"'
        extracted_images  = re.findall(re_pattern_image,raw_data)
        listcourseimage = []
        for txt in extracted_images:
            image = txt.split('\":\"')[-1].split('\"')[0]
            listcourseimage.append(image)
        # find keyword ("tracking_id":)-(any)-("headline:")- extract any to comma
        re_pattern_headline = r'"tracking_id":[^,]*,"headline":[^,]*'
        extracted_headlines  = re.findall(re_pattern_headline,raw_data)
        listcourseheadline = []
        for txt in extracted_headlines:
            headline = txt.split('\":\"')[-1]
            listcourseheadline.append(headline)
        # find key word ("num_subscribers")- extract until comma
        re_pattern_subscribers = r'"num_subscribers":[^,]*'
        extracted_subscribers  = re.findall(re_pattern_subscribers,raw_data)
        listcoursesubscriber = []
        for txt in extracted_subscribers:
            subscriber = txt.split('\":')[-1]
            listcoursesubscriber.append(subscriber)
        # find key word ("avg_rating")- extract until comma
        re_pattern_avgrating = r'"avg_rating":[^,]*'
        extracted_avgrating  = re.findall(re_pattern_avgrating,raw_data)
        listcourseavgrating = []
        for txt in extracted_avgrating:
            avgrating = txt.split('\":')[-1]
            listcourseavgrating.append(avgrating)
        # find key word (""content_info_short":")- extract until comma
        re_pattern_contentlen = r'"content_info_short":[^,]*'
        extracted_contentlen  = re.findall(re_pattern_contentlen,raw_data)
        listcoursecontentlen = []
        for txt in extracted_contentlen:
            contentlen = txt.split('\":\"')[-1].split(' ')[0]
            listcoursecontentlen.append(contentlen)
        # add course data to course.text
        course = open('./data/result/course.txt','a+')
        course.seek(0)

        for i in range(len(listcourseid)):
            coursedata = listcourseid[i]+';;;'+listcoursetitle[i]+';;;'+listcourseimage[i]+';;;'+listcourseheadline[i]+';;;'+listcoursesubscriber[i]+';;;'+listcourseavgrating[i]+';;;'+listcoursecontentlen[i]+'\n'
            course.write(coursedata)
        
        course.close()



    #3.2.3 extract review info
    def extract_review_info(self):
        # extract all course id
        rawfile = open('./data/course_data/raw_data.txt','r')
        rawfile.seek(0)
        raw_data = rawfile.read()
        rawfile.close()

        review_txt = open('./data/result/review.txt','a+')
        review_txt.seek(0)

        re_pattern_id = r'"course","id":[^,]*'
        extracted_courseids  = re.findall(re_pattern_id,raw_data)
        listcourseid = []

        for txt in extracted_courseids:
            courseid = txt.split(':')[-1]
            if courseid not in listcourseid:
                listcourseid.append(courseid)

        # check file with courseid name exist in review.txt folder
        for courseid in listcourseid:
            if os.path.exists('./data/review_data/'+courseid+'.json'):
                review_json_file = open('./data/review_data/'+courseid+'.json','r')
                review_json_file.seek(0)
                review_json = review_json_file.read()
                review_json_file.close()

                #extract review id
                re_pattern_id = r'course_review", "id":[^,]*'
                extracted_ids  = re.findall(re_pattern_id,review_json)
                listreviewid = []
                for txt in extracted_ids:
                    id = txt.split(': ')[-1]
                    listreviewid.append(id)
                #extract review content
                re_pattern_content = r'"course_review"[^content]*"content":[^,]*'
                extracted_content  = re.findall(re_pattern_content,review_json)
                listreviewcontent = []
                for txt in extracted_content:
                    content = txt.split(': \"')[-1][:-1]
                    listreviewcontent.append(content)
                #extract review rating
                re_pattern_rating = r'"rating":[^,]*'
                extracted_rating  = re.findall(re_pattern_rating,review_json)
                listreviewrating = []
                for txt in extracted_rating:
                    rating = txt.split(': ')[-1]
                    listreviewrating.append(rating)
                
                
                for i in range(len(listreviewid)):
                    reviewdata = listreviewid[i]+';;;'+listreviewcontent[i]+';;;'+listreviewrating[i]+';;;'+courseid+'\n'
                    review_txt.write(reviewdata)
                
        review_txt.close()



    #3.2.5 extract_students_info()
    def extract_students_info(self):
        rawfile = open('./data/course_data/raw_data.txt','r')
        rawfile.seek(0)
        raw_data = rawfile.read()
        rawfile.close()

        user_student = open('./data/result/user_student.txt','a+')
        user_student.seek(0)
        
        re_pattern_id = r'"course","id":[^,]*'
        extracted_ids  = re.findall(re_pattern_id,raw_data)
        listcourseid = []
        for txt in extracted_ids:
            id = txt.split(':')[-1]
            listcourseid.append(id)
        # check file with courseid name exist in review.txt folder
        for courseid in listcourseid:
            if os.path.exists('./data/review_data/'+courseid+'.json'):
                review_json_file = open('./data/review_data/'+courseid+'.json','r')
                review_json_file.seek(0)
                review_json_data = review_json_file.read()
                review_json_file.close()

                listuserid = []
                listusername = []
                listpass = []
                listtitle = []
                listimage = []
                listinitial = []
                listreviewid = []

                #extract review id
                re_pattern_id = r'course_review", "id":[^,]*'
                extracted_ids  = re.findall(re_pattern_id,review_json_data)
                listreviewid = []
                for txt in extracted_ids:
                    id = txt.split(': ')[-1]
                    listreviewid.append(id)
                
                #extract review id
                re_pattern_userinfo = r'"user_modified":[^,]*, "user": {"_class": "user",[^}]*'
                extracted_info  = re.findall(re_pattern_userinfo,review_json_data)
                
                for info in extracted_info:
                    userid = ''
                    if '"id": ' not in info:
                        unid = self.generate_unique_user_id()
                        userid = str(unid)
                    else:
                        id = info.split('id\": ')[-1].split(',')[0]
                        userid = id
                    
                    listuserid.append(userid)
                    
                    title = info.split('title\": \"')[-1].split('\"')[0]
                    listtitle.append(title)
                    
                    username = title.replace(' ', '_').lower()
                    listusername.append(username)

                    initalsplit = info.split('initials\":')[-1]
                    inital = ''
                    for char in initalsplit:
                        if char.isalpha():
                            inital = inital + char.lower()
                    listinitial.append(inital)
                    
                    password = inital+userid+inital
                    encryptedpass = self.encryption(password)
                    listpass.append(encryptedpass)

                    image = info.split('image_50x50\": \"')[-1].split('",')[0]
                    listimage.append(image)

                
                for i in range(len(listreviewid)):
                    studentinfo = listuserid[i]+';;;'+listusername[i]+';;;'+listpass[i]+';;;'+listtitle[i]+';;;'+listimage[i]+';;;'+listinitial[i]+';;;'+listreviewid[i]+'\n'
                    user_student.write(studentinfo)
        user_student.close()



    #3.2.6 extract_instructor_info()
    def extract_instructor_info(self):        
        listid = []
        listusername = []
        listpass = []
        listdisplayname = []
        listjobtitle = []
        listimage = []
        listcoursids = []

        rawfile = open('./data/course_data/raw_data.txt','r')
        rawfile.seek(0)
        raw_data = rawfile.read()
        rawfile.close()

        re_pattern_id = r'"course","id":[^,]*'
        extracted_ids  = re.findall(re_pattern_id,raw_data)
        for txt in extracted_ids:
            id = txt.split(':')[-1]
            listcoursids.append(id)

        #extract review id
        re_pattern_instuctorsinfo = r'"visible_instructors":[^}]*'
        extracted_info  = re.findall(re_pattern_instuctorsinfo,raw_data)
                
        for info in extracted_info:
            id = info.split('id\":')[-1].split(',')[0]
            listid.append(id)

            encryptedpass = self.encryption(id)
            listpass.append(encryptedpass)

            displayname = info.split('display_name\":\"')[-1].split('\",')[0]
            listdisplayname.append(displayname)

            username = displayname.replace(' ','_').lower()
            listusername.append(username)

            jobtitle = info.split('job_title\":\"')[-1].split('\",')[0]
            listjobtitle.append(jobtitle)

            image = info.split('image_100x100\":\"')[-1].split('jpg')[0] + 'jpg'
            listimage.append(image)

        listcheck = [] # check id was added
        listcontent = [] # list contains all content
        for i in range(len(listid)):
            ins_id = listid[i]
            # checking exist
            if ins_id not in listcheck:
                listcheck.append(ins_id)
                instructorinfo = ins_id+';;;'+listusername[i]+';;;'+listpass[i]+';;;'+listdisplayname[i]+';;;'+listjobtitle[i]+';;;'+listimage[i]+';;;'+listcoursids[i]+'\n'
                listcontent.append(instructorinfo)
            else:
                index  = listcheck.index(ins_id)
                currentinfo = listcontent[index]
                listcontent[index] = currentinfo.replace('\n','-'+listcoursids[i]+'\n')

        user_instructor_txt = open('./data/result/user_instructor.txt','a+')
        user_instructor_txt.writelines(listcontent)
        user_instructor_txt.close()



    # 3.2.7 extract info
    def extract_info(self):
        self.extract_review_info()
        self.extract_course_info()
        self.extract_instructor_info()
        self.extract_students_info()
        



    # 3.2.7 remove data
    def remove_data(self):
        open('./data/result/course.txt', 'w').close()
        open('./data/result/review.txt', 'w').close()
        open('./data/result/user_student.txt', 'w').close()
        open('./data/result/user_instructor.txt', 'w').close()



    # 3.2.8 view course
    def view_courses(self,args=[]):
        # check args empty
        if not args:
            Course().courses_overview()
        # check args not empty
        else:
            if len(args) != 2:
                print('View courses only include one command and one value')
            else:
                if args[0] == "TITLE_KEYWORD":
                    listsearched_course = Course().find_course_by_title_keyword(args[1])
                    for course_obj in listsearched_course:
                        courseinfo = course_obj.__str__()
                        print(courseinfo)

                elif args[0] == "ID" :
                    try : 
                        convertedint = int(args[1])
                        listscourse = Course().find_course_by_id(convertedint)
                        for course_obj in listscourse:
                            courseinfo = course_obj.__str__()
                            print(courseinfo)
                    except ValueError:
                        print('Incorrect value: id must be all digits')

                elif args[0] == "INSTRUCTOR_ID" :
                    try : 
                        convertedint = int(args[1])
                        listscourse = Course().find_course_by_instructor_id(convertedint)
                        for course_obj in listscourse:
                            courseinfo = course_obj.__str__()
                            print(courseinfo)
                    except ValueError:
                        print('Incorrect value: instructor id must be all digits')

                else:
                    print('Incorrect command: only "TITLE_KEYWORD/ID/INSTRUCTOR_ID"')


    

    # 3.2.9 view user
    def view_users(self):
        # user admin
        user_admin = open('./data/result/user_admin.txt','a+')
        user_admin.seek(0)
        admindata = user_admin.readlines()
        num_admin = len(admindata)
        print('The number of admin is:',num_admin)
        user_admin.close()

        # user student
        user_student = open('./data/result/user_student.txt','a+')
        user_student.seek(0)
        studentdata = user_student.readlines()
        num_student = len(studentdata)
        print('The number of student is:',num_student)
        user_student.close()

        # user admin
        user_instructor = open('./data/result/user_instructor.txt','a+')
        user_instructor.seek(0)
        isntructordata = user_instructor.readlines()
        num_instructor = len(isntructordata)
        print('The number of instructor is:',num_instructor)
        user_instructor.close()
        


    # 3.2.10 view_reviews
    def view_reviews(self,args=[]):
        #print(args)
        # check args empty
        if not args:
            Review().reviews_overview()
        # check args not empty
        else:
            if len(args) != 2:
                print('View courses only include one command and one value')
            else:
                if args[0] == "KEYWORD":
                    listreview = Review().find_review_by_keywords(args[1])
                    for review_obj in listreview:
                        reviewinfo = review_obj.__str__()
                        print(reviewinfo)
                
                elif args[0] == "ID" :
                    try : 
                        convertedint = int(args[1])
                        listscourse = Review().find_review_by_id(convertedint)
                        for course_obj in listscourse:
                            courseinfo = course_obj.__str__()
                            print(courseinfo)
                    except ValueError:
                        print('Incorrect value: id must be all digits')

                elif args[0] == "COURSE_ID" :
                    try : 
                        convertedint = int(args[1])
                        listscourse = Review().find_review_by_course_id(convertedint)
                        for course_obj in listscourse:
                            courseinfo = course_obj.__str__()
                            print(courseinfo)
                    except ValueError:
                        print('Incorrect value: course id must be all digits')

                else:
                    print('Incorrect command: only "ID/KEYWORD/COURSE_ID"')



    # 3.2.11 __str__()
    def __str__(self):
       admininfo = super().__str__()
       return admininfo


