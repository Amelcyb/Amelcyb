number_students = int(input("Please enter number of students: "))

with open("reg_form.txt", "w+") as f:
    for num in range(number_students):
        name = int(input("Entet student ID number: "))
        reg_name = f.write(f'{str(name)}....................\n')  
        
