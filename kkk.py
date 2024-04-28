def calculate_average(scores):
 return sum(scores) / len(scores)
	
def  determine_pass_fail(average_score):
   if average_score >= 60:
        return "Pass"
   else:
    return "Fail"
	
    def main():
   # Sample list of tuples with student names and their scores
     students =[ 
       
13	        ("Alice", [70, 80, 90]),
14	        ("Bob", [50, 60, 70]),
15	        ("Charlie", [80, 75, 55]),
16	        ("David", [45, 65, 75]),
17	        ("Emma", [85, 90, 95])
18	    ]
print ("Student Scores:")
for student in students:
	        name = student[0]
scores = student[1]
        average_score = calculate_average(scores)
        result = determine_pass_fail(average_score)
        print(f"{name}: Average Score = {average_score}, Result = {result}")
	
if __name__ == "__main__":
	    main()