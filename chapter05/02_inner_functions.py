def calculate_grade(assignment_scores, course_score, final_score):
    def weighted_average():
        assignment_score = sum(assignment_scores) / len(assignment_scores)
        return (assignment_score * 0.4) + (course_score * 0.3) + (final_score * 0.3)

    def determine_grade(average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        elif average >= 50:
            return 'E'
        else:
            return 'F'

    avg = weighted_average()
    grade = determine_grade(avg)

    return avg, grade

def main():
    final_average, final_grade = calculate_grade([85, 90, 70, 100, 95], 94, 80)
    print(f"Final Grade: {final_grade} with average: {final_average}")

if __name__ == "__main__":
    main()