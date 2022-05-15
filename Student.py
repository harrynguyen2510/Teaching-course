
from User import User
from Course import Course
from Review import Review


class Student(User):

    # 3.4.1 constructor
    def __init__(self,user_id=None, username=None, password=None,
    user_title=None,user_image_50x50=None,user_initials=None,review_id=None):

        super().__init__(user_id, username, password)

        self.user_title = user_title if user_title is not None else ""
        self.user_image_50x50 = user_image_50x50 if user_image_50x50 is not None else ""
        self.user_initials = user_initials if user_initials is not None else ""
        self.review_id = review_id if review_id is not None else -1

    # 3.4.2 view_course
    def view_courses(self, args=[]):
        user_student_txt = open('./data/result/user_student.txt','a+')
        user_student_txt.seek(0)
        user_student_data = user_student_txt.readlines()
        user_student_txt.close()

        review_txt = open('./data/result/review.txt','a+')
        review_txt.seek(0)
        review_data = review_txt.readlines()
        review_txt.close()

        string_studentid = str(self.user_id)+';;;'

        coursetitle = ''

        for line in user_student_data:
            if string_studentid in line:
                reviewid = line.split(';;;')[-1][:-1] # [:-1] for remove '/n'
                
                string_reviewid = reviewid+';;;'

                for rline in review_data:
                    if string_reviewid in rline:
                        courseid = rline.split(';;;')[-1][:-1]
                        registerdcourse = Course().find_course_by_id(courseid)
                        coursetitle = registerdcourse.course_title
        return coursetitle
        


    # 3.4.3 view review
    def view_reviews(self, args=[]):
        user_student_txt = open('./data/result/user_student.txt','a+')
        user_student_txt.seek(0)
        user_student_data = user_student_txt.readlines()
        user_student_txt.close()

        reviewcontent = ''

        string_userid = str(self.user_id)+';;;'

        for line in user_student_data:
            if string_userid in line:
                reviewid = line.split(';;;')[-1][:-1]
                review_obj = Review().find_review_by_id(reviewid)
                reviewcontent = review_obj.content
                
        return reviewcontent



    # 3.4.4 __str__
    def __str__(self):
        currentinfo = super().__str__()
        currentinfo = currentinfo.replace('\n',';;;')
        currentinfo += self.user_title+';;;'+self.user_image_50x50+';;;'+self.user_initials+';;;'+str(self.review_id)
        return currentinfo

