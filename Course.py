
class Course:

    # 3.5.1 parameterized constructor
    def __init__(self, course_id=None, course_title=None, 
    course_image_100x100=None, course_headline=None,
    course_num_subscribers=None,course_avg_rating=None,course_content_length=None):

        self.course_id = course_id if course_id is not None else -1
        self.course_title = course_title if course_title is not None else ""
        self.course_image_100x100 = course_image_100x100 if course_image_100x100 is not None else ""
        self.course_headline = course_headline if course_headline is not None else ""
        self.course_num_subscribers = course_num_subscribers if course_num_subscribers is not None else -1
        self.course_avg_rating = course_avg_rating if course_avg_rating is not None else -1.0
        self.course_content_length = course_content_length if course_content_length is not None else -1



    # 3.5.2 find_course_by_title_keyword
    def find_course_by_title_keyword(self,keyword):
        course_txt = open('./data/result/course.txt','a+')
        course_txt.seek(0)
        course_data = course_txt.readlines()
        course_txt.close()

        listcourse = []

        for line in course_data:
            if keyword in line:
                splitinfo = line.split(';;;')
                # index 0: courseid, 1: title, 2: image, 3: headline, 4: subcriber, 5: averaging, 6: content length
                searched_course = Course(int(splitinfo[0]),splitinfo[1],splitinfo[2],splitinfo[3],splitinfo[4],splitinfo[5],splitinfo[6])
                if searched_course not in listcourse:
                    listcourse.append(searched_course)

        return listcourse

    

    # 3.5.3 find course by id (course id)
    def find_course_by_id(self, course_id):
        course_txt = open('./data/result/course.txt','a+')
        course_txt.seek(0)
        course_data = course_txt.readlines()
        course_txt.close()

        course = None
        courseid_string = str(course_id) + ';;;'

        for line in course_data:
            if courseid_string in line:
                splitinfo = line.split(';;;')
                # index 0: courseid, 1: title, 2: image, 3: headline, 4: subcriber, 5: averaging, 6: content length
                course = Course(int(splitinfo[0]),splitinfo[1],splitinfo[2],splitinfo[3],splitinfo[4],splitinfo[5],splitinfo[6])
        return course

    

    # 3.5.4 find course by instructor id 
    def find_course_by_instructor_id(self,instructor_id):
        user_instructor_txt = open('./data/result/user_instructor.txt','a+')
        user_instructor_txt.seek(0)
        user_instructor_data = user_instructor_txt.readlines()
        user_instructor_txt.close()

        instructorid_string = str(instructor_id) + ';;;'

        listCourse = []

        for line in user_instructor_data:
            if instructorid_string in line:
                courseids = line.split(';;;')[-1][:-1].split('-')
                for id in courseids:
                    course_object = self.find_course_by_id(id)
                    if course_object not in listCourse:
                        listCourse.append(course_object)
        return listCourse



    # 3.5.5 course overview
    def courses_overview(self):
        course_txt = open('./data/result/course.txt','r')
        course_txt.seek(0)
        course_data = course_txt.readlines()
        course_txt.close()

        print('Total number of courses:',str(len(course_data)))



    # 3.5.6 str
    def __str__(self):
        coursestring = 'course id: '+str(self.course_id)+'\n'+'course title: '+self.course_title+'\n'+'course image: '+self.course_image_100x100+'\n'+'course headline: '+self.course_headline+'\n'+'course number subcribers: '+str(self.course_num_subscribers)+'\n'+'course average rating: '+str(self.course_avg_rating)+'\n'+'course content length: '+str(self.course_content_length)
        return coursestring
