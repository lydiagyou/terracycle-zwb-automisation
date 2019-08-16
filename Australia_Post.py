"""
AU Post is weird because they put all the customer orders in one doc
add in Reseller code?? -- which ones does ONLY AP do and which ones does ONLY the other ones do?
output/print how many distinct orders there are
-how to deal with Companyname?
AP orders include time of the order -- need to shorten (no, because you just take the order date to be the current date)
"""

# import modules and files
import pandas as pd
from CONSTANTS import AU_ITEM_DICT
import datetime
from datetime import date
import holidays


# local constants
ONE_DAY = datetime.timedelta(days=1)
HOLIDAYS_AU = holidays.AU()


# functions
def next_business_day():
    """gets the next business day (for expected shipment date)"""
    next_day = datetime.date.today() + ONE_DAY
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_AU:
        next_day += ONE_DAY
    return next_day


def csv_name():
    """sets the name of the output file to AP-first reference number in the csv"""
    order_number = df.iloc[0]['Order']
    return 'AP-' + str(order_number) + '.csv'


def get_product_details(item):
    return AU_ITEM_DICT[item]


# code
df = pd.read_csv("ap.csv")

# define the DataFrame that will be outputted
output = pd.DataFrame(index=range(len(df.index)),
                      columns=["Reference #", "Customer Name", "Billing Street", "Billing City", "Billing State",
                               "Billing Postcode", "Billing Country", "Shipping Name", "Shipping Street 1",
                               "Shipping City", "Shipping State",
                               "Shipping Postcode", "Shipping Country", "Order Date",
                               "Expected Shipment Date", "Channel", "Contact Email", "Contact Phone",
                               "Item Name", "Item Price", "Currency Code", "Quantity", "SKU", "Reseller Code",
                               "Item Channel", "Item Reference #", "Sales Order Level Tax", "Sales Order Level Tax %",
                               "Sales Order Level Tax Exemption Reason", "Is Discount Before Tax",
                               "Entity Discount Percent"])
output.index.name = 'Index'


# copy in columns
output['Reference #'] = df['Order']
output['Item Reference #'] = df['Order']
output['Order Date'] = date.today().strftime("%d/%m/%Y")
output['Expected Shipment Date'] = next_business_day()
output['Shipping Name'] = df['Name']
output['Shipping Street 1'] = df['Address']
output['Shipping City'] = df['City']
output['Shipping State'] = df['State']
output['Shipping Postcode'] = df['Postcode']
output['Contact Email'] = df['Email']
output['Contact Phone'] = df['Phone']
output["Reseller Code"] = df['Code']


# fixed for all Australia Post orders
output['Customer Name'] = 'Australia Post'
output['Shipping Country'] = "Australia"
output['Billing Street'] = 'Level 26 Lonsdale St'
output['Billing City'] = 'Melbourne'
output['Billing State'] = 'VIC'
output['Billing Postcode'] = 3000
output['Billing Country'] = 'Australia'
output['Channel'] = 'Australia Post'
output['Sales Order Level Tax'] = 'GST'
output['Sales Order Level Tax %'] = 10
output['Sales Order Level Tax Exemption Reason'] = 'GST FREE'
output['Is Discount Before Tax'] = 'TRUE'
output["Entity Discount Percent"] = 0
output["Currency Code"] = 'AUD'
output["Item Channel"] = 'Australia Post'


# go through each row (order) and get item details
for i in range(len(df.index)):
    # item details - name, SKU, reseller code, price, quantity
    details = get_product_details(df.iloc[i]['Product'])

    # put information in appropriate columns
    output.at[i, 'Item Name'] = details[0]
    output.at[i, 'SKU'] = details[1]
    output.at[i, 'Item Price'] = details[2]
    output.at[i, 'Quantity'] = df.iloc[i]['Quantity']


# convert output DataFrame into csv, then finished!
output.to_csv(csv_name())
print("File exported correctly. Your file is called " + csv_name())
