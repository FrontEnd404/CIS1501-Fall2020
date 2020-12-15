def  reverse_list():

    list1 = ["one","two","three","four","five"]


    print(list1)
    x = 0
    length_of_list = len(list1)
    while x != length_of_list:
        place_holder = list1[length_of_list-1]
        list1.remove(list1[length_of_list-1])
        list1.insert(0 + x,place_holder)
        x = x+1

    print(list1)

reverse_list()








