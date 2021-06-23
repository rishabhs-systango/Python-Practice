# taking detail of alll the student
def studentDetail(name,age,location,coding_language) :
    print(name)
    print(age)
    print(location)
    print(coding_language)
studentDetail(name = "Rishabh",coding_language = "Python",location = "Ujjain",age = 22)



#Arbitary keyword arguments **args
def student_Detail(**args) :
    print(args["name"])
    print(args["age"])
    print(args["location"])
    print(args["coding_language"])
student_Detail(name = "Rishabh",coding_language = "Python",location = "Ujjain",age = 22)