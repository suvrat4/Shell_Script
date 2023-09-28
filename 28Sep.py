# ... (previous code)

# Calculate assignee counts
assignee_counts = df['Assignee'].value_counts().reset_index()
assignee_counts.columns = ['Assignee', 'Count']

# Create a DataFrame for assignee counts
assignee_counts_df = pd.DataFrame(assignee_counts)

# Create a new column for "Resource Utilization" (percentage) as a floating-point number
assignee_counts_df['Resource Utilization'] = (assignee_counts_df['Count'] / len(df)) * 100

# Create an Excel writer object for the output file
excel_filename = "jira_issues_for_assignees.xlsx"

# Save all issues to the "all issues" sheet
df.to_excel(excel_filename, sheet_name='all issues', index=False)

# Create a Pandas Excel writer object with openpyxl
with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a', datetime_format='yyyy-mm-dd') as writer:
    # Save assignee counts to a new sheet
    assignee_counts_df.to_excel(writer, sheet_name='assignee counts', index=False)

    # Get the worksheet for the "assignee counts" sheet
    worksheet = writer.sheets['assignee counts']

    # Define a cell format for displaying percentages with two decimal places
    percentage_format = openpyxl.styles.NamedStyle(name='percentage_format')
    percentage_format.number_format = '0.00%'
    
    # Apply the percentage format to the "Resource Utilization" column
    for cell in worksheet['C'][1:]:
        cell.style = percentage_format

# ... (rest of the code for sending the email)

# ...
