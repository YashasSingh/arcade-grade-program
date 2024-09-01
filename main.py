import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

def display_grades(subjects, grades, theme='light'):
    # Ensure that the number of subjects matches the number of grades
    if len(subjects) != len(grades):
        print("Error: The number of subjects and grades must match.")
        return

    # Calculate the average grade
    average_grade = sum(grades) / len(grades)

    # Define theme colors
    themes = {
        'light': {'bar': 'skyblue', 'line': 'green', 'pie': 'Paired'},
        'dark': {'bar': 'darkblue', 'line': 'lime', 'pie': 'YlOrRd'}
    }
    colors = themes.get(theme, themes['light'])
    
    # Create interactive bar chart
    bar_fig = go.Figure()
    bar_fig.add_trace(go.Bar(x=subjects, y=grades, marker_color=colors['bar'], text=grades, textposition='outside'))
    bar_fig.update_layout(title='Grades by Subject', xaxis_title='Subjects', yaxis_title='Grades', yaxis_range=[0, 100])
    bar_fig.update_traces(texttemplate='%{text}', textposition='outside')
    
    # Create interactive pie chart
    pie_fig = go.Figure()
    pie_fig.add_trace(go.Pie(labels=subjects, values=grades, hole=0.3, textinfo='label+percent', marker=dict(colors=plt.cm.get_cmap(colors['pie']).colors)))
    pie_fig.update_layout(title='Grade Distribution')

    # Create interactive line chart
    line_fig = go.Figure()
    line_fig.add_trace(go.Scatter(x=subjects, y=grades, mode='lines+markers', marker_color=colors['line'], name='Grades'))
    line_fig.add_trace(go.Scatter(x=subjects, y=[average_grade]*len(subjects), mode='lines', line=dict(color='red', dash='dash'), name=f'Average: {average_grade:.2f}'))
    line_fig.update_layout(title='Grade Trends', xaxis_title='Subjects', yaxis_title='Grades', yaxis_range=[0, 100])

    # Save charts as images
    pio.write_image(bar_fig, 'bar_chart.png')
    pio.write_image(pie_fig, 'pie_chart.png')
    pio.write_image(line_fig, 'line_chart.png')

    # Show interactive charts
    bar_fig.show()
    pie_fig.show()
    line_fig.show()

def export_to_csv(subjects, grades, filename):
    df = pd.DataFrame({'Subject': subjects, 'Grade': grades})
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")

def get_user_input():
    def on_submit():
        subjects = entry_subjects.get().split(',')
        grades = entry_grades.get().split(',')
        theme = theme_var.get()

        try:
            grades = list(map(float, grades))
        except ValueError:
            messagebox.showerror("Input Error", "Grades must be numeric.")
            return

        subjects = [subject.strip() for subject in subjects]

        if len(subjects) != len(grades):
            messagebox.showerror("Input Error", "The number of subjects and grades must match.")
            return

        # Display charts
        display_grades(subjects, grades, theme)

        # Export data
        export_filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if export_filename:
            export_to_csv(subjects, grades, export_filename)
    
    # Create GUI
    root = Tk()
    root.title("Grade Displayer")

    Label(root, text="Subjects (comma-separated):").grid(row=0, column=0, padx=10, pady=10)
    entry_subjects = Entry(root, width=50)
    entry_subjects.grid(row=0, column=1, padx=10, pady=10)

    Label(root, text="Grades (comma-separated):").grid(row=1, column=0, padx=10, pady=10)
    entry_grades = Entry(root, width=50)
    entry_grades.grid(row=1, column=1, padx=10, pady=10)

    Label(root, text="Theme (light/dark):").grid(row=2, column=0, padx=10, pady=10)
    theme_var = Entry(root, width=20)
    theme_var.grid(row=2, column=1, padx=10, pady=10)
    theme_var.insert(0, 'light')  # Default theme

    Button(root, text="Submit", command=on_submit).grid(row=3, column=0, columnspan=2, pady=20)

    root.mainloop()

# Run the GUI
get_user_input()
