# ... (previous code)

# Calculate assignee counts
assignee_counts = df['Assignee'].value_counts().reset_index()
assignee_counts.columns = ['Assignee', 'Total Count']

# Create a DataFrame for assignee counts
assignee_counts_df = pd.DataFrame(assignee_counts)

# Calculate the total open count per assignee
open_counts = df[df['Status'] != 'Closed']['Assignee'].value_counts().reset_index()
open_counts.columns = ['Assignee', 'Open Count']

# Calculate the total close count per assignee
close_counts = df[df['Status'] == 'Closed']['Assignee'].value_counts().reset_index()
close_counts.columns = ['Assignee', 'Close Count']

# Merge the DataFrames to include the open and close counts
assignee_counts_df = assignee_counts_df.merge(open_counts, on='Assignee', how='left')
assignee_counts_df = assignee_counts_df.merge(close_counts, on='Assignee', how='left')

# Fill NaN values with 0 for assignees with no open or close counts
assignee_counts_df['Open Count'] = assignee_counts_df['Open Count'].fillna(0)
assignee_counts_df['Close Count'] = assignee_counts_df['Close Count'].fillna(0)

# Calculate resource utilization as a percentage (total close count divided by user's close count multiplied by 100)
assignee_counts_df['Resource Utilization (%)'] = (assignee_counts_df['Close Count'] / assignee_counts_df['Close Count'].sum()) * 100

# Create an Excel writer object for the output file
excel_filename = "jira_issues_for_assignees.xlsx"

# Save all issues to the "all issues" sheet
df.to_excel(excel_filename, sheet_name='all issues', index=False)

# Create a Pandas Excel writer object with openpyxl
with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a', datetime_format='yyyy-mm-dd') as writer:
    # Save assignee counts to a new sheet
    assignee_counts_df.to_excel(writer, sheet_name='assignee counts', index=False)

# ... (rest of the code for sending the email)

# ...
