#import


#Constants
bob_int_list = [1,2,3,4,5]
manny_list = [10,12,14,16]
manny_str_list = ["10","12","14","16"]
bob_str_list = ["1","2","3"]



#DEFINITION
def iterate_thru_list(my_list):
    test = "bobby"
    print(test)
    index = 0
    for element in my_list:
        print(element)
        if index == 7:
            print("im at the 7th one")
        index = index + 1
        

def is_lower(a,b):
    if a < b:
        print(f'{a} is lower than {b}')
        return True
    else:
        print(f'{a} is higher than {b}')
        return False

unorganized_list = [2,51246,134,7,3,343,1,32,5]

def min_list(my_list):
    index = 0
    index_of_min = 0
    min_element = my_list[0]
    for element in my_list:
        if my_list[index] < min_element:
            index_of_min = index
            min_element = my_list[index]
        else:
            pass

        index = index + 1

    return min_element,index_of_min

def sort_list(my_list):
    sorted_list = []
    
    for x in range(len(my_list)):
        minimum, index_of_min = min_list(my_list) 
        sorted_list.append(minimum)
        my_list.pop(index_of_min)


    return sorted_list


def get_list_midpoint(my_list):

    return my_list[len(my_list)//2]

def bob_main():
    print(get_list_midpoint(bob_str_list))

def manny_main():
    print(manny_list)
    print(manny_list[2-1])


second_list = manny_list

#Execution
if __name__ == "__main__":
    # print("BOBBY")
    # bob_main()
    # print("\n")

    # print("MANNY")
    # manny_main()
    is_lower(69,17)

    print(sort_list(unorganized_list))



