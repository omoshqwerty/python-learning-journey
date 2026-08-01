students = int(input("Enter number of students: "))
scores = {}

def get_scores():
    for student in range(students):
        name = input("Enter name: ")
        score = float(input("Enter score: "))
        scores[name]=score
    return scores
results = get_scores()   


def class_average(scores_dict):
    avg = sum(scores_dict.values()) / len(scores_dict)
    return avg

ans = class_average(results)


def top_student(scores_dict):
    best = max(scores_dict, key=scores_dict.get)
    return best

topper = top_student(results)


print("="*40)
print("SCHOOL REPORT!")
print("="*40)
print()
print(f"Average: {ans}")
print(f"Best: {topper}")

#●	Create a function get_scores() that asks the user how many students there are, then loops to collect each student's name and score, storing them in a dictionary {name: score}
#●	Create a function class_average(scores_dict) that returns the average score of all students
#●	Create a function top_student(scores_dict) that returns the name of the student with the highest score
#●	In the main part of the program, call all three functions and print a summary report showing the class average and the top student







 
