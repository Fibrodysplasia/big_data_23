import pandas as pd

# If you don't specify dtype = object you will get an error because of the mixed types
data = pd.read_csv('./complaints.csv', dtype = object)

# separate out the headers
headers = list(data.columns.values)
print(headers)
# The output should look like this:
#['Date received', 'Product', 'Sub-product', 'Issue', 'Sub-issue', 'Consumer complaint narrative', 'Company public response', 'Company', 'State', 'ZIP code', 'Tags', 'Consumer consent provided?', 'Submitted via', 'Date sent to company', 'Company response to consumer', 'Timely response?', 'Consumer disputed?', 'Complaint ID']

# As we are interested in consumer complaints by product,
# we need a list of the unique products:
# print(products)
# ['Debt collection' 'Money transfer, virtual currency, or money service'
#  'Credit reporting or other personal consumer reports' 'Credit card'
#  'Vehicle loan or lease' 'Student loan' 'Mortgage'
#  'Checking or savings account'
#  'Payday loan, title loan, personal loan, or advance loan'
#  'Debt or credit management' 'Prepaid card'
#  'Credit reporting, credit repair services, or other personal consumer reports'
#  'Credit card or prepaid card' 'Payday loan, title loan, or personal loan'
#  'Bank account or service' 'Credit reporting' 'Money transfers'
#  'Consumer Loan' 'Payday loan' 'Other financial service'
#  'Virtual currency']

# Given the number of products, we are going to be taking the top 5, 
# to get a count type:
product_counts = data['Product'].value_counts()
print(product_counts)
# Product
# Credit reporting, credit repair services, or other personal consumer reports    2164394
# Debt collection                                                                  514068
# Mortgage                                                                         386436
# Credit card or prepaid card                                                      206362
# Credit reporting or other personal consumer reports                              192967
# Checking or savings account                                                      187844
# Credit reporting                                                                 140429
# Credit card                                                                       99158
# Bank account or service                                                           86205
# Student loan                                                                      79076
# Money transfer, virtual currency, or money service                                60389
# Vehicle loan or lease                                                             49069
# Consumer Loan                                                                     31575
# Payday loan, title loan, or personal loan                                         30639
# Payday loan                                                                        5541
# Money transfers                                                                    5354
# Prepaid card                                                                       4705
# Payday loan, title loan, personal loan, or advance loan                            1189
# Other financial service                                                            1058
# Debt or credit management                                                           214
# Virtual currency                                                                     18
# Name: count, dtype: int64


# We are going to take the top 4 products (over 77% of the total complaints) to work with:
product_counts = product_counts.head(4)
print(product_counts)
# Product
# Credit reporting, credit repair services, or other personal consumer reports    2164394
# Debt collection                                                                  514068
# Mortgage                                                                         386436
# Credit card or prepaid card                                                      206362
# Name: count, dtype: int64

# Now we want to filter all columns except Product and Consumer Complaint Narrative out
# and only include products from our top 4:
# Make sure you're working with a DataFrame:
df = pd.DataFrame(data)

# Now let's grab the Products and Consumer complaint narrative:
product_complaint = df[['Product', 'Consumer complaint narrative']]

# Verify this worked:
l = list(product_complaint.columns.values)
print(l)
# ['Product', 'Consumer complaint narrative']
product_complaint.shape
# (4246690, 2)

# Now we want to filter everything but our top 4 products:
top = product_complaint['Product'].value_counts().head(4).index
filtered = product_complaint.loc[product_complaint['Product'].isin(top)]
# And you an see we are left with the top 4:
filtered.shape
# (3271260, 2)

# We also want to check and remove NaN values from customers 
# not providing a narrative:
filtered.isnull().sum()
# Product                               0
# Consumer complaint narrative    2021925
filtered.dropna(inplace=True)

# Check you dropped them all:
filtered.shape
# (1249335, 2)

# See what it looks like:
print(filtered.head(20))
                                                # Product                       Consumer complaint narrative
# 50                                      Debt collection  I do not have a contract or written agreement ...
# 51                                      Debt collection  XXXX XXXX XXXX sent my account to collection o...
# 108                                     Debt collection  I do not recognize this derogatory account lis...
# 185                                            Mortgage  My monthly mortgage payment for Select Portfol...
# 255                                            Mortgage  Dear Ameri Home Mortgage, L.L.C. \nI trust thi...
# 290                                     Debt collection  The incident started when the company over cha...
# 296                                     Debt collection  Please consider this a formal request to inves...
# 340   Credit reporting, credit repair services, or o...  I was a victim of Identity Theft. Per the Fair...
# 410                                     Debt collection  Specialized Loan Servicing LLC ( SLS ), is in ...
# 512                                     Debt collection  In the last three days I have received two tex...
# 516                         Credit card or prepaid card  Once upon a time, in the year 2021, XXXX and X...
# 517                         Credit card or prepaid card  Cred.ai is the company that oversees tis XXXX ...
# 529                         Credit card or prepaid card  I paid the card balance in full XXXX. Since th...
# 539                                     Debt collection  MIDLAND CREDIT MANANGMENT has illegally posted...
# 562                                            Mortgage  I am currently going through a divorce proceed...
# 564                                            Mortgage  The servicing of my loan was transferred from ...
# 600                                     Debt collection  Good Morning, The purpose of this writing is t...
# 1111                                           Mortgage  My husband became unemployed as of XX/XX/XXXX....
# 1574                                           Mortgage  My fianc and I are set to close on our first h...
# 2329                                           Mortgage  Loan Number : XXXX Property Address : XXXX XXX...

# Create a test dataset and save the full dataset to .txt files with comma separated values
filtered.head(2000).to_csv('2000_test.txt', sep='\t', index=False)
filtered.to_csv('filtered.txt', sep='\t', index = False)