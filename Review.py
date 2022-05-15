class Review:

    # 3.6.1 parameterized constructor
    def __init__(self, review_id=None, content=None, 
    rating=None, course_id=None):

        self.review_id = review_id if review_id is not None else -1
        self.content = content if content is not None else ""
        self.rating = rating if rating is not None else -1.0
        self.course_id = course_id if course_id is not None else -1

    

    # 3.6.2 find review by id
    def find_review_by_id(self,review_id):
        review_txt = open('./data/result/review.txt','r')
        review_txt.seek(0)
        review_data = review_txt.readlines()
        review_txt.close()

        review_obj = None
        reviewid_string = str(review_id)+';;;'
        
        for line in review_data:
            if reviewid_string in line:
                splitinfo = line.split(';;;')
                # index 0: reviewid, 1: content, 2: avgrating, 3: courseid
                review_obj = Review(int(splitinfo[0]),splitinfo[1],splitinfo[2],splitinfo[3])
        return review_obj



    # 3.6.3 find review by keyword on content
    def find_review_by_keywords(self,keyword):
        review_txt = open('./data/result/review.txt','r')
        review_txt.seek(0)
        review_data = review_txt.readlines()
        review_txt.close()

        list_review_obj = []
        
        for line in review_data:
            if keyword in line:
                splitinfo = line.split(';;;')
                # index 0: reviewid, 1: content, 2: avgrating, 3: courseid
                review_obj = Review(int(splitinfo[0]),splitinfo[1],splitinfo[2],splitinfo[3])
                if review_obj not in list_review_obj:
                    list_review_obj.append(review_obj)
        return list_review_obj

    

    #3.6.4 find_review_by_course_id(course_id)
    def find_review_by_course_id(self,course_id):
        review_txt = open('./data/result/review.txt','r')
        review_txt.seek(0)
        review_data = review_txt.readlines()
        review_txt.close()

        list_review_obj = []
        courseid_string = ';;;'+str(course_id)+'\n'
        
        for line in review_data:
            if courseid_string in line:
                splitinfo = line.split(';;;')
                # index 0: reviewid, 1: content, 2: avgrating, 3: courseid
                review_obj = Review(int(splitinfo[0]),splitinfo[1],splitinfo[2],splitinfo[3])
                if review_obj not in list_review_obj:
                    list_review_obj.append(review_obj)
        return list_review_obj



    #3.6.4 review overview
    def reviews_overview(self):
        review_txt = open('./data/result/review.txt','r')
        review_txt.seek(0)
        review_data = review_txt.readlines()
        review_txt.close()

        print('Total number of courses:',str(len(review_data)))

    #3.6.6 __str__()
    def __str__(self):
        review_string = 'review id: '+str(self.review_id)+'\n'+'review content: '+self.content+'\n'+'review rating: '+str(self.rating)+'\n'+'course id: '+str(self.course_id)
        return review_string



