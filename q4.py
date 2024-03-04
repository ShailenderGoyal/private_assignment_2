

# TODO : Number of Subjects -- Dynamic
def avg_student(s_dict, overall_avg_dict):
    marks=s_dict.values()
    avg_marks=0
    marks=list(marks)
    marks=marks[0]
    print(marks)
    for x in marks:
        avg_marks = avg_marks+ x
    avg_marks= avg_marks/(len(marks))
    overall_avg_dict[list(s_dict.keys())[0]]=avg_marks
    return overall_avg_dict
    # print(avg_marks)


def calculate_average(list_s_dicts):
    avg_dict={}
    for x in list_s_dicts:
        avg_dict=avg_student(x,avg_dict)
    # print(avg_dict)
    return avg_dict

def highest_avg_scorer(avg_dict):
    max_avg = max(avg_dict.values())
    high_score=0
    high_scorer=0
    for key, value in avg_dict.items():
        if value == max_avg:
            # print(key)
            high_scorer=key
            high_score=value

    return {high_scorer:high_score}

def highest_sub_scorer(list_s_dicts):
    max_dict={}
    for x in range(5):  #Subjects
        max_score=0
        max_scorer=0
        for student in list_s_dicts:
            if (list(student.values())[0][x]>max_score):
                max_score=list(student.values())[0][x]
                max_scorer=list(student.keys())[0][0]
        max_dict[x]=[max_scorer,max_score]
    return max_dict


def find_highest_scorer(list_s_dicts, avg_dict):
    d1=highest_sub_scorer(list_s_dicts)
    d2=highest_avg_scorer(avg_dict)
    return d1,d2


i=[{"s":[1,2,3,4]},{"d":[6,7,8,9]}]

# TODO : Dataset Generator and importing Dataset



def data_add(i):
    print("Adding Data")
    n=int(input("Enter the number of Students:- "))
    for x in range(n):
        name=input("Enter Name:-")
        marks=input("Enter Marks in 5 subjects(space separated):- ")
        marks.split()
        marks=[int(y) for y in marks]
        i[name]=marks
    return i

def dict_printer(dict):
    for x,y in dict.items():
        print("Student : ",x," Marks : ", y)

while(1):
    print("Menu")
    print("1. Add Data")
    print("2. Calculate and Display Averages")
    print("3. Find Highest Scorers")
    print("4. Exit")

    choice=input("Enter Choice: ")
    if choice == "1":
        data_add(i)
    elif choice == "2":
        avg_dictionary=calculate_average(i)
        dict_printer(avg_dictionary)
    elif choice == "3":
        avg_dictionary=calculate_average(i)
        # name_high_scorer,high_score=highest_avg_scorer(avg_dictionary)
        # max_scorers=highest_sub_scorer(i)
        h_avg,h_sub=find_highest_scorer(i,avg_dictionary)
        name_high_scorer,high_score=h_avg.items()
        print("Highest Average Score : ",high_score, " Highest Scorer : ", name_high_scorer)
        for x,y in h_sub:
            print("Subject ",x," Student: ", y[0]," Marks: ",y[1])
    elif choice == "4":
        break