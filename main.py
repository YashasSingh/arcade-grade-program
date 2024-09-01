import matplotlib.pyplot as plt

def display_grades(subjects, grades):
    # Ensure that the number of subjects matches the number of grades
    if len(subjects) != len(grades):
        print("Error: The number of subjects and grades must match.")
        return

    # Calculate the average grade
    average_grade = sum(grades) / len(grades)

    # Create a figure with 3 subplots
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Bar Chart
    axs[0].bar(subjects, grades, color='skyblue')
    axs[0].set_title('Grades by Subject')
    axs[0].set_xlabel('Subjects')
    axs[0].set_ylabel('Grades')
    axs[0].set_ylim(0, 100)  # Set y-axis limit to 0-100
    axs[0].grid(axis='y', linestyle='--', alpha=0.7)

    # Display grade values above bars
    for i, grade in enumerate(grades):
        axs[0].text(i, grade + 1, str(grade), ha='center', va='bottom')

    # Pie Chart for Grade Distribution
    axs[1].pie(grades, labels=subjects, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
    axs[1].set_title('Grade Distribution')

    # Line Chart for Grade Trends
    axs[2].plot(subjects, grades, marker='o', color='green')
    axs[2].set_title('Grade Trends')
    axs[2].set_xlabel('Subjects')
    axs[2].set_ylabel('Grades')
    axs[2].set_ylim(0, 100)
    axs[2].grid(True)

    # Display the average grade on the line chart
    axs[2].axhline(y=average_grade, color='r', linestyle='--', label=f'Average: {average_grade:.2f}')
    axs[2].legend()

    # Show the entire plot
    plt.suptitle('Grade Displayer for One Person', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

# Example Usage with Sample Data
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'History']
grades = [85, 90, 78, 88, 92]

display_grades(subjects, grades)
