
from Course import Course
from User import User
from Review import Review


class Instructor(User):
    
    #3.3.1 parameterized constructor
    def __init__(self,user_id=None, username=None, password=None,
    display_name=None,job_title=None,image_100x100=None,course_id_list=None):

        super().__init__(user_id, username, password)
        self.display_name = display_name if display_name is not None else ""
        self.job_title = job_title if job_title is not None else ""
        self.image_100x100 = image_100x100 if image_100x100 is not None else ""
        self.course_id_list = course_id_list if course_id_list is not None else []



    #3.3.2 view course
    def  view_courses(self,args=[]):
        listcourse = Course().find_course_by_instructor_id(str(self.user_id))
        count = 0
        for course_obj in listcourse:
            count +=1
            #only print max 10 courses
            if count <=10:
                courseinfo = course_obj.__str__()
                print(courseinfo)
                    



    # view_review
    def view_reviews(self,args=[]):
        listcourse = Course().find_course_by_instructor_id(str(self.user_id))
        count = 0
        for course_obj in listcourse:
            courseid = course_obj.course_id
            list_review_obj = Review().find_review_by_course_id(courseid)

            for review_obj in list_review_obj:
                count +=1
                #only print max 10 reviews
                if count <=10:
                    review_info = review_obj.__str__()
                    print(review_info)


    #3.3.4 str
    def __str__(self):
        courseids_string = ''
        for courseids_string in self.course_id_list:
            courseids_string += courseids_string + '-'
        courseids_string = courseids_string[:-1]

        currentinfo = super().__str__()
        currentinfo = currentinfo.replace('\n',';;;')
        currentinfo += self.display_name + ';;;' + self.job_title + ';;;' + self.image_100x100 + ';;;' + courseids_string

        return currentinfo


