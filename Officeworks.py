"""
NOTES:
-may have to install **pip, numpy, pandas, datetime, holidays on whatever computer
-THE VIC LOCATION FOR OFFICEWORKS HASN'T CHANGED?? (just the street name is diff; but need to update the item dict and
also the vic_shipping() function) (but also OW hasn't changed their own system lmao)
"""

# import modules and files
import pandas as pd
from CONSTANTS import OW_DICT
from CONSTANTS import OW_LOCATIONS
import datetime
from datetime import date
import holidays

# local constants
ONE_DAY = datetime.timedelta(days=1)
HOLIDAYS_AU = holidays.AU()


# functions
def get_product_details(item):
    """given an item name, returns a list with the official name, SKU, reseller code, and
    price of an item"""
    return OW_DICT[item]


def next_business_day():
    """gets the next business day (for expected shipment date)"""
    next_day = datetime.date.today() + ONE_DAY
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_AU:
        next_day += ONE_DAY
    return next_day


def nsw_shipping(data_frame):
    """auto-populates the shipping address to the NSW location"""
    data_frame['Shipping Name'] = 'Officeworks NSW North Rocks Offsite Yennora DC (W929)'
    data_frame['Shipping Street 1'] = 'Bldg 2A.2 57 Loftus Road'
    data_frame['Shipping City'] = 'Yennora'
    data_frame['Shipping State'] = 'NSW'
    data_frame['Shipping Postcode'] = 2161
    data_frame['Shipping Country'] = 'Australia'
    data_frame['Contact Email'] = 'supplyChainCFCNSW@officeworks.com.au'
    data_frame['Contact Phone'] = '0298484409'


def qld_shipping(data_frame):
    """auto-populates the shipping address to the QLD location"""
    data_frame['Shipping Name'] = 'Officeworks QLD (Redbank) OWB CFC (W941)'
    data_frame['Shipping Street 1'] = '59 Robert Smith Street'
    data_frame['Shipping City'] = 'Redbank'
    data_frame['Shipping State'] = 'QLD'
    data_frame['Shipping Postcode'] = 4301
    data_frame['Shipping Country'] = 'Australia'
    data_frame['Contact Email'] = 'officeworks.receiving@dbschenker.com'
    data_frame['Contact Phone'] = '0732809413'


def wa_shipping(data_frame):
    """auto-populates the shipping address to the WA location"""
    data_frame['Shipping Name'] = 'Officeworks WA (Perth Airport) OWB CFC (W969)'
    data_frame['Shipping Street 1'] = '1 Affleck Road Perth Airport'
    data_frame['Shipping City'] = 'Perth'
    data_frame['Shipping State'] = 'WA'
    data_frame['Shipping Postcode'] = 6105
    data_frame['Shipping Country'] = 'Australia'
    data_frame['Contact Email'] = 'supplychaincfcWA@officeworks.com.au'
    data_frame['Contact Phone'] = '0892701304'


def vic_shipping(data_frame):
    """auto-populates the shipping address to the VIC location"""
    data_frame['Shipping Name'] = 'Officeworks VIC (Laverton North) OWB CFC (W939)'
    data_frame['Shipping Street 1'] = '219 - 225 Fitzgerald Road Laverton North'
    data_frame['Shipping City'] = 'North Laverton'
    data_frame['Shipping State'] = 'VIC'
    data_frame['Shipping Postcode'] = 3026
    data_frame['Shipping Country'] = 'Australia'
    data_frame['Contact Email'] = 'SupplyChainCFCVIC@officeworks.com.au'
    data_frame['Contact Phone'] = '0732809413'


def csv_name():
    order_number = df.iloc[0]['Order No']
    return 'OW-' + str(order_number) + '.csv'


# -------------code-------------
# read CSV file named 'ow.csv'
df = pd.read_csv("ow.csv")
NUM_ORDERS_NON_DISTINCT = len(df.index)

# define the DataFrame that will be outputted
output = pd.DataFrame(index=range(NUM_ORDERS_NON_DISTINCT),
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

# copy columns into DataFrame
output['Reference #'] = df['Order No']
output['Item Reference #'] = df['Order No']
output['Order Date'] = date.today().strftime("%d/%m/%Y")
output['Expected Shipment Date'] = next_business_day()

# these fields are fixed for every Officeworks order
output['Customer Name'] = 'Officeworks'
output['Billing Street'] = '1 South Drive, 236 - 262 East'
output['Billing City'] = 'East Bentleigh'
output['Billing State'] = 'VIC'
output['Billing Postcode'] = 3165
output['Billing Country'] = 'Australia'
output['Channel'] = 'Officeworks'
output['Sales Order Level Tax'] = 'GST'
output['Sales Order Level Tax %'] = 10
output['Sales Order Level Tax Exemption Reason'] = 'GST FREE'
output['Is Discount Before Tax'] = 'TRUE'
output["Entity Discount Percent"] = 0
output["Currency Code"] = 'AUD'
output["Item Channel"] = 'Officeworks'

# determine shipping address based on 'Deliver to' field
map_to = df.iloc[0]['Deliver to']
location = OW_LOCATIONS[map_to]
if location == "QLD":
    qld_shipping(output)
elif location == "VIC":
    vic_shipping(output)
elif location == "NSW":
    nsw_shipping(output)
else:
    wa_shipping(output)

# go through each row (order) and get item details
for i in range(NUM_ORDERS_NON_DISTINCT):
    # item details - name, SKU, reseller code, price, quantity
    details = get_product_details(df.iloc[i]['Description'])

    # put information in appropriate columns
    output.at[i, 'Item Name'] = details[0]
    output.at[i, 'SKU'] = details[1]
    output.at[i, 'Reseller Code'] = details[2]
    output.at[i, 'Item Price'] = details[3]
    output.at[i, 'Quantity'] = df.iloc[i]['Qty']

# convert output DataFrame into csv, then finished!
output.to_csv(csv_name())
print("File exported correctly. Your file is called " + csv_name())
