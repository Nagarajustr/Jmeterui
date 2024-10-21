import pandas as pd
import os

# print(result)
# data1 = r'C:\Users\2154856\OneDrive - Cognizant\Desktop\python\Performance_Data_Compare\CurrentRelease.csv';
# data2 = r'C:\Users\2154856\OneDrive - Cognizant\Desktop\python\Performance_Data_Compare\PreviousRelease.csv';
# data3 = r'C:\Users\2154856\OneDrive - Cognizant\Desktop\python\Performance_Data_Compare\result1.jtl';
# output_file = r'C:\Users\2154856\OneDrive - Cognizant\Desktop\python\Performance_Data_Compare\Output.xlsx'


# Get the current directory of the current subfolder
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file paths relative to the current directory
data1 = os.path.join(current_dir, 'CurrentRelease.csv')
data2 = os.path.join(current_dir, 'PreviousRelease.csv')
data3 = os.path.join(current_dir, 'result1.jtl')
output_file = os.path.join(current_dir, 'Output.xlsx')


df1 = pd.read_csv(data1)
df2 = pd.read_csv(data2)
df_result = pd.read_csv(data3)

# # Get the response count 500 for individual labels
# response_500_counts = df_result[df_result['responseCode'].str.match('^5\d{2}$')].groupby('label').size().reset_index(name='count_500')

# Get the response count 500 for individual labels
response_500_counts = df_result[df_result['responseCode'] == '500'].groupby('label').size().reset_index(name='count_500')

# Create a DataFrame of all unique labels
all_labels = pd.DataFrame({'label': df_result['label'].unique()})

# Merge to include all labels, filling missing values with 0
all_labels_with_500 = pd.merge(all_labels, response_500_counts, on='label', how='left').fillna({'count_500': 0})

new_df1 = pd.DataFrame({
    'Label': all_labels_with_500['label'],
    '500 Error Count': all_labels_with_500['count_500']
})

new_df1 = pd.merge(new_df1, df1[['Label', '90% Line']], on='Label', how='left')
new_df1.rename(columns={'90% Line': '90% Line Current Release'}, inplace=True)



new_df1 = pd.merge(new_df1, df2[['Label', '90% Line']], on='Label', how='left')
new_df1.rename(columns={'90% Line': '90% Line Previous Release'}, inplace=True)

new_df1['90% Line Difference'] = new_df1['90% Line Previous Release'] - new_df1['90% Line Current Release']
new_df1['Difference'] = (new_df1['90% Line Difference']/new_df1['90% Line Current Release'])*100


new_df1['Status'] = new_df1.apply(lambda row: 'PASS' if row['500 Error Count'] == 0 and row['Difference'] < 10 else 'FAIL', axis=1)


new_df1.to_excel(output_file, index=True)