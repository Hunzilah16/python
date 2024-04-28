1 def calculate_average(scores):
2 return sum(scores) / len(scores)
3
4 def determine_pass_fail(average_score):
5 if average_score >= 60:
6 return "Pass"
7 else:
8 return "Fail"
9
10 def main():
11	    # Sample list of tuples with student names and their scores
12	    students = [
    13	        ("Alice", [70, 80, 90]),
    14	        ("Bob", [50, 60, 70]),
    15	        ("Charlie", [80, 75, 55]),
    16	        ("David", [45, 65, 75]),
    17	        ("Emma", [85, 90, 95])
    
    
20 print("Student Scores:")
21 for student in students:
22	        name = student[0]
23	        scores = student[1]
24	        average_score = calculate_average(scores)
25	        result = determine_pass_fail(average_score)
26 print(f"{name}: Average Score = {average_score}, Result = {result}")
27
28 if __name__ == "__main__":
29	    main()
