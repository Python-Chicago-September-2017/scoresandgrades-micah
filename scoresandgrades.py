
def scores_and_grades():
    gradesheet = ["F", "D", "C", "B", "A"]
    import random
    for i in range(10):
        random_num = random.randint(60,100)
        grade = gradesheet[int(random_num/10)-5]
        random_num = str(random_num)
        print "Score: " + random_num + "; Your grade is " + grade 
    print "End of line...Master Control signing off"
scores_and_grades()