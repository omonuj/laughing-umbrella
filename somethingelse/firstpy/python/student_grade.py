def main():
    num_students = int(input("Enter number of students: "))
    num_subjects= int(input("How many subjects: "))

    scores = []
    for student in range(num_students):
        student_scores = []
        for subject in range(num_subjects):
            score = int(input(f"Enter score for student {student + 1} for subject {subject + 1}: "))
            student_scores.append(score)
        scores.append(student_scores)

    totals = [sum(student_scores) for student_scores in scores]
    averages = [total / num_subjects for total in totals]
    positions = sorted(range(len(totals)), key = lambda blue: totals[blue], reverse = True)
    positions = [positions.index(red) + 1 for red in range(len(positions))]

    print("\nSTUDENT SUMMARY")
    for student in range(num_students):
        print(f"Student {student + 1}:")
        for subject in range(num_subjects):
            print(f"Subject {subject + 1}: {scores[student][subject]}")
        print(f"Total: {totals[student]}")
        print(f"Average: {averages[student]:.2f}")
        print(f"Position: {positions[student]}\n")

    for subject in range(num_subjects):
        subject_scores = [scores[student][subject] for student in range(num_students)]
        highest_score = max(subject_scores)
        lowest_score = min(subject_scores)
        total_score = sum(subject_scores)
        average_score = total_score / num_subjects
        num_passes = len([score for score in subject_scores if score >= 50])
        num_fails = num_subjects - num_passes

        print(f"SUBJECT {subject + 1} SUMMARY")
        print(
        f"  Highest scoring student: Student {subject_scores.index(highest_score) + 1} scoring {highest_score}")
        print(f"  Lowest scoring student: Student {subject_scores.index(lowest_score) + 1} scoring {lowest_score}")
        print(f"  Total score: {total_score}")
        print(f"  Average score: {average_score:.2f}")
        print(f"  Number of passes: {num_passes}")
        print(f"  Number of fails: {num_fails}\n")

if __name__ == "__main__":
                main()
