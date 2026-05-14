#=======================================
#Concept    Python (pandas)	     SAS
#=======================================
# Dataset	    DataFrame	         SAS Dataset
# Column	    Series	             Variable
# Row	        Row	                 Observation
# Datastep	    pandas operations	 DATA step
# SQL	        df.query() / joins	 PROC SQL
#=======================================



# =============================================
# PYTHON CRASH TEST FOR SAS/SQL USERS
# =============================================
# Covers:
# - Creating datasets (customer + transactions)
# - Importing from Excel
# - Joins (merge)
# - Data manipulation
# - Feature engineering
# - Loops
# - Arrays (lists)
# =============================================
import pandas as pd
import numpy as np

# =============================================
# OPTION 1: CREATE DATA WITHIN PYTHON
# =============================================

#Customer level dataset
Customers=pd.DataFrame([(1,'Amit',28,'Delhi'),
                        (2,'Gaurav',35,'Noida'),
                        (3,'Saurav',31,'Gurgaon'),
                        (4,'Sunil',23,'Bhopal'),
                        (5,'Karan',26,'Haridwar')],
                        columns=['cust_id','Name','Age','Location'])
print(Customers)
print(Customers.head())
print(Customers.tail())
print(Customers.info())
print(Customers.describe())

#Transaction level dataset
Transactions=pd.DataFrame([(1,123,'2024-01-01',50.99),
                           (2,223,'2024-02-01',51.99),
                           (2,213,'2024-01-21',20.9),
                           (3,154,'2024-02-15',101.21),
                           (4,113,'2024-02-28',49),
                           (4,93,'2024-04-05',11.99),
                           (5,54,'2024-01-08',151)],
columns=['cust_id','transaction_id','transaction_date','amount'])
print(Transactions)
print(Transactions.head())
print(Transactions.tail())
print(Transactions.info())
print(Transactions.describe())
print(Transactions.info())

# =============================================
# OPTION 2: IMPORT FROM EXCEL
# =============================================
# Uncomment and use if needed
# customers = pd.read_excel('customers.xlsx')
# transactions = pd.read_excel('transactions.xlsx')

# =============================================
# JOIN (LIKE SQL JOIN)
# =============================================
merged=pd.merge(Customers,Transactions,on='cust_id',how='left')
print(merged.head())

# =============================================
# BASIC DATA MANIPULATION
# =============================================

#Filter (Where)
Noida_data=merged[merged['Location']=='Noida']
print(Noida_data)

#Create new column - using numpy where clause to create condition based flag
merged['Amount_Flag']=np.where(merged['amount']>=50,'High','Low')
print(merged)

#Group By - Aggregation
agg_data = merged.groupby('cust_id').agg(
    total_spend=('amount','sum'),
    avg_spend=('amount','mean'),
    txn_count=('transaction_id','count')
    ).reset_index()
print(agg_data)

# =============================================
# FEATURE ENGINEERING
# =============================================

#Recency - days since last transaction
from datetime import date

merged['transaction_date1']=pd.to_datetime(merged['transaction_date'], errors='coerce')
#errors='coerce' is used to force invalid values to convert into NaT or NaN
merged = merged.sort_values(['cust_id', 'transaction_date1'])
print(merged.info())
merged['prev_txn_date'] = merged.groupby('cust_id')['transaction_date1'].shift(1) 
print(merged)
print(merged.info())
#Grouping by cust_id in above step and going up one row in transaction_date field to get prev txn date
print(merged['transaction_date'].head())
print(merged['transaction_date'].dtype)

merged['days_since_lst_txn'] = (merged['transaction_date1'] - merged['prev_txn_date']).dt.days
print(merged['days_since_lst_txn'])
print(merged.info())

# =============================================
# LOOPS (SIMILAR TO DATA STEP LOOPS)
# =============================================
#Merge merged and agg_data
merged2=pd.merge(merged,agg_data,on='cust_id',how='left')
print(merged2)

#Example - Categorise spends manually - Create spend bins
Spend_category=[]
for val in merged2['total_spend']:
    if val == 0:
        Spend_category.append('Nil')
    elif val<=100:
          Spend_category.append('<=100')
    else:
          Spend_category.append('>100')
merged2['Spend_category']=Spend_category
print(merged2)

#Parent child problem
family=pd.DataFrame([('Aman','Ramesh'),
                    ('Vinay','Suresh'),
                     ('Ramesh','Amit'),
                    ('Vinay','Roshan'),
                    ('Suresh','Romit')], columns=['Parent','Child'])
print(family)
family2=family.merge(family,left_on='Child', right_on='Parent',suffixes=('_left','_right'))
print(family2)
family2_final=family2[['Parent_left','Child_right']].rename(columns={'Parent_left':'Grandfather','Child_right':'Grandson'})
print(family2_final)

# =============================================
# ARRAYS (LISTS IN PYTHON)
# =============================================
#Create multiple flags using list
thresholds=[20,40,50,100]
for t in thresholds:
    merged2[f'flag_{t}']=np.where(merged2['total_spend']>t,1,0)
print(merged2)

print("\nFinal Data:")
print(merged2)

#Max transaction amount per customer
merged3=merged2.groupby('Name').agg(Max_amount=('amount','max'))
print(merged3)

#Identify customers with no transactions - left join logic. First do left join then see where there are no matches found


Light="Green"
if Light=="Red":
     print("Stop")
elif Light=="Green":
     print("Go")
else:
     print("Wait")

#Grade students based on marks
marks=69
if marks>=90:
     Grade="A"
elif marks>=80:
     Grade="B"
elif marks>=70:
     Grade="C"
else:
     Grade="D"
print(Grade)

#Check if a given number is even or odd
nbr=6
remainder=nbr % 2
if remainder==1:
     print("Odd")
else:
     print("even")

#WAP to find the greatest of the three numbers entered by the user
a=20
b=30
c=70
print(max(a,b,c))

#WAP to check if a number is a multiple of 7 or not
n=51
if n % 7 == 0:
     print("Multiple of 7")
else: print("Not a multiple of 7")

