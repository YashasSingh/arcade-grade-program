

# Grade Displayer

A Python application for visualizing and analyzing grades with interactive charts. This tool allows you to display grades for different subjects using bar, pie, and line charts, and export the data to a CSV file. It also features a graphical user interface (GUI) for easy interaction.

## Features

- **Interactive Charts:** Visualize grades using bar charts, pie charts, and line charts with interactive features.
- **Export to CSV:** Save the subjects and grades to a CSV file for further analysis.
- **Customizable Themes:** Choose between light and dark themes for the charts.
- **Graphical User Interface (GUI):** Input subjects, grades, and select themes using a simple GUI.

## Requirements

- Python 3.x
- `plotly` for interactive charts
- `pandas` for exporting data to CSV
- `tkinter` for the graphical user interface

Install the required Python libraries using pip:

```bash
pip install plotly pandas
```

`tkinter` is included with standard Python installations, so no additional installation is needed.

## Usage

1. **Run the Application:**

   Execute the script with Python to open the GUI:

   ```bash
   python grade_displayer.py
   ```

2. **Enter Data:**

   - **Subjects:** Enter subjects as a comma-separated list (e.g., `Math, Physics, Chemistry`).
   - **Grades:** Enter corresponding grades as a comma-separated list (e.g., `85, 90, 78`).
   - **Theme:** Specify the theme as either `light` or `dark`.

3. **Submit Data:**

   Click the "Submit" button to generate the interactive charts. You will be prompted to save the charts as images and export the data to a CSV file.

4. **View Charts:**

   The charts will be displayed in your web browser. The following charts are generated:
   - **Bar Chart:** Grades by subject.
   - **Pie Chart:** Grade distribution.
   - **Line Chart:** Grade trends with an average line.

5. **Export Data:**

   Choose a location and filename to save the CSV file containing your subjects and grades.

## Example

Here's an example of running the application and inputting data:

```text
Subjects (comma-separated): Math, Physics, Chemistry, English, History
Grades (comma-separated): 85, 90, 78, 88, 92
Theme (light/dark): light
```

The application will generate and display the following:
- A bar chart with grades by subject.
- A pie chart showing the distribution of grades.
- A line chart illustrating grade trends with an average line.

It will also save the charts as PNG files and export the data to a CSV file.

## Troubleshooting

- **Error: The number of subjects and grades must match.**
  Ensure that the number of subjects matches the number of grades.

- **Error: Grades must be numeric.**
  Verify that all grades are numerical values.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

