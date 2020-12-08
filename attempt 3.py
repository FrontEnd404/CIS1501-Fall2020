class Assignment:

    def __init__(self):

        global grade_list
        grade_list = []

    def add_score(self,new_score):
        self.new_score = new_score
        grade_list.append(self.new_score)
        return grade_list

    def get_average_score(self):
        global grade_list_sum
        grade_list_sum = sum(grade_list)
        global number_of_elemnts_in_list
        number_of_elemnts_in_list = len(grade_list)
        global average_score
        average_score = grade_list_sum/number_of_elemnts_in_list

    def get_max_score(self):
        global max_score
        grade_list.sort()
        length = (len(grade_list))
        max_score = grade_list[length - 1]

    def get_min_score(self):
        global min_score
        grade_list.sort()
        length2 = (len(grade_list))
        min_score = grade_list[0]


class Curved_Assignment(Assignment):
    def __init__(self):
        global curved_grade_list
        curved_grade_list = []

    def get_average_score(self):
        global curved_grade_list_sum
        curved_grade_list_sum = sum(curved_grade_list)
        global number_of_elemnts_in__curved_list
        number_of_elemnts_in__curved_list = len(curved_grade_list)
        global curved_average_score
        curved_average_score = curved_grade_list_sum / number_of_elemnts_in__curved_list

    def get_max_score(self):
        global curved_max_score
        curved_grade_list.sort()
        length2 = (len(grade_list))
        curved_max_score = curved_grade_list[length2 - 1]

    def get_min_score(self):
        global curved_min_score
        curved_grade_list.sort()
        length2 = (len(grade_list))
        curved_min_score = grade_list[0]



grade_list1 = Assignment()
grade_list1.add_score(200)
print(grade_list)
grade_list1.add_score(100)
grade_list1.get_average_score()
print(grade_list)
print(average_score)
grade_list1.get_max_score()
print(grade_list)
print(max_score)
grade_list1.get_min_score()
print(min_score)


