
total_points = 0
total_credits = 0

#You need to enter the point grade of the course and the credit hours
#You will have to refer to your schools point grade system to get the correct values
#Uses a loop to ask for grade and credit inputs depending on how many courses you have

try:
    course_amount = int(input("Enter your amount of courses: "))
    
    for course_number in range(course_amount):
        print(f"Course {course_number + 1}:")
        grade = float(input("Enter Grade Points (e.g 4.0, 3.7): "))
        credits = int(input("Enter Credit Hours (e.g 1, 2, 3, 4): "))
        
        total_points += grade * credits
        total_credits += credits
    
    gpa = total_points / total_credits
    print(f"Your GPA is {gpa:.1f}")

#Ends code if incorrect value is entered

except ValueError:
    print("Incorrect Value Entered")
    