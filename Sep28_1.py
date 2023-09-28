# ... (previous code)

# Calculate assignee counts
assignee_counts = df['Assignee'].value_counts().reset_index()
assignee_counts.columns = ['Assignee', 'Count']

# Create a DataFrame for assignee counts
assignee_counts_df = pd.DataFrame(assignee_counts)

# Create a new column for "Resource Utilization" (percentage) as a floating-point number
assignee_counts_df['Resource Utilization'] = (assignee_counts_df['Count'] / len(df)) * 100

# Calculate status counts
status_counts = df['Status'].value_counts().reset_index()
status_counts.columns = ['Status', 'Count']

# Create a DataFrame for status counts
status_counts_df = pd.DataFrame(status_counts)

# Define a color palette for the pie chart
colors = ['#E74C3C', '#3498DB', '#2ECC71', '#F1C40F', '#9B59B6', '#E67E22', '#95A5A6', '#34495E', '#1ABC9C', '#D35400']

# Create an Excel writer object for the output file
excel_filename = "jira_issues_for_assignees.xlsx"

# Save all issues to the "all issues" sheet
df.to_excel(excel_filename, sheet_name='all issues', index=False)

# Create a Pandas Excel writer object with openpyxl
with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a', datetime_format='yyyy-mm-dd') as writer:
    # Save assignee counts to a new sheet
    assignee_counts_df.to_excel(writer, sheet_name='assignee counts', index=False)

    # Save status counts to a new sheet
    status_counts_df.to_excel(writer, sheet_name='status counts', index=False)

    # Get the worksheet for the "status counts" sheet
    worksheet = writer.sheets['status counts']

    # Create a pie chart
    chart = openpyxl.chart.PieChart()
    labels = openpyxl.chart.Reference(worksheet, min_col=1, min_row=2, max_row=worksheet.max_row, max_col=1)
    data = openpyxl.chart.Reference(worksheet, min_col=2, min_row=1, max_row=worksheet.max_row, max_col=2)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(labels)
    chart.title = "Status Distribution"

    # Assign colors from the color palette to the data points
    for i, color in enumerate(colors):
        slice = openpyxl.chart.Series(data, labels, title=status_counts_df['Status'][i])
        slice.graphicalProperties.solidFill = color
        chart.series.append(slice)

    # Add the chart to the worksheet
    worksheet.add_chart(chart, "D2")

# ... (rest of the code for sending the email)

# ...
