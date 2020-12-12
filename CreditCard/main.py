## 1) Taking in data csv ##
import pandas as pd

data = pd.read_csv('BankChurners.csv')
print(data)

## 2) All the parameters for the dataset, change the names to simpler meaningful words ##
print(data.columns)

n_data = data.drop(['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
                    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'],axis=1)
print(n_data.head())

## 3) Understand all the columns ##
# 1) Client Number: For identification

# 2) Attrition Flag: 'Existing Customer', 'Attrited Customer'
    # We need to use Existing Customer to see if it will churn or not.
    # We can use churned data to see which are going away.

# 3) Customer_Age
# 4) Gender : ['M' 'F']
# 5) Dependent_count : [3 5 4 2 0 1]
# 6) Education_Level : ['High School' 'Graduate' 'Uneducated' 'Unknown' 'College' 'Post-Graduate'
#                      'Doctorate']
# 7) Marital_Status  :  ['Married' 'Single' 'Unknown' 'Divorced']
# 8) Income_Category :  ['$60K - $80K' 'Less than $40K' '$80K - $120K' '$40K - $60K' '$120K +'
#                       'Unknown']
# 9) Card_Category  :   ['Blue' 'Gold' 'Silver' 'Platinum']
# 10) Months_on_book  :
# 11) Total_Relationship_Count :  [5 6 4 3 2 1]


for col in n_data:
    if col in ['CLIENTNUM', 'Customer_Age', 'Total_Amt_Chng_Q4_Q1','Total_Ct_Chng_Q4_Q1' ,'Avg_Utilization_Ratio']:
        print(col, ': ', 'Too Much Data, Use Visualization')
    else: 
        print(col, ': ', n_data[col].unique())





