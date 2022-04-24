students = {"John": ["Python", "Java", "JavaScript"], "Bob": ["JavaScript", "C programming"]}
keys = students.keys()
for eachkey in keys:
    print("Courses takebn by",eachkey, "are")
    for eachCourse in students[eachkey]:
        print (eachCourse)