# import necessary modules
import datetime
import numpy as np
import pandas as pd

# functions
def read_csv_file(filename):
    newname = pandas.read_csv(filename, header=0, sep=';')
    return newname

def add_new_col(data_frame, header, cell_text):
    """adds the new column to the data frame"""
    var = [cell_text]
    data_frame[header] = var
    return data_frame


def get_order_number(file, row):
    """gets the reference number of the order and returns a string called AP-referencenumber"""
    row_after = row + 1
    order = file[row:row_after]['Order']
    order_number = 'AP-' + str(order[row])
    return order_number

def get_number_of_orders(filename):
    """# check how many different orders there are in the file:"""
    num_orders = 0  # number of different orders there are in a file aka numbre of ppl
    if len(filename) > 1:

        ref_num = get_order_number(filename, 0)[3:]

        for i in range(1, len(filename)):
            new_ref_num = get_order_number(filename, i)[3:]  # gets only the order, without the 'AP-'
            if new_ref_num == ref_num:
                pass
            else:
                num_orders += 1
                ref_num = new_ref_num
    return num_orders


def refine_phone(phone_number):
    """returns the phone number in Australia format - with a +61 in front. Must be imported a number"""
    phone_string = str(phone_number)[]

    if (phone_string[0] == '0') and (phone_string[1] != '0'):
        cute_phone = '+61 ' + phone_string[1:]
        return cute_phone
    elif (phone_string[0] == '6') and (phone_string[1] == '1'):
        cute_phone = '+' + phone_string
        return cute_phone
    elif phone_string[0] != '0':
        cute_phone = '+61 ' + phone_string
        return cute_phone
    else:
        return phone_string


def shipping_address(file, row):
    """attention! we consider 0 to be the first row"""
    row_after = row + 1  # python starts at 0
    costumer_name = file[row:row_after]['Name']
    address = file[row:row_after]['Address']
    city = file[row:row_after]['City']
    state = file[row:row_after]['State']
    postcode = file[row:row_after]['Postcode']
    country = 'Australia'
    phone = file[row:row_after]['Phone']  # since Australia Post cuts the first zero of the phones
    # needs to be optimized doing an if/else with the first
    email = file[row:row_after]['Email']
    where_to_ship = [costumer_name, address, city, state, postcode, country, phone, email]
    # makes a data table txt style
    return where_to_ship


def get_date(file, row):
    """this function gets the date of the shipment order when it is placed"""
    'in Australia Post, orders are as dd/mm/yyyy hh:mm:ss (24-hour format)'
    "e.g. 13/07/2019 21:04:56 this changes it to dd/mm/yyy"
    row_after = row + 1
    cell_date = file[row:row_after]['Date']
    return cell_date[row][:10]


def get_expected_shipment_date(file):
    """ the string type of the expected shipment date is in yyyy-mm-dd"""
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    NextDay_Date_short = str(NextDay_Date)[:10]
    return NextDay_Date_short


def get_quantity(file, row):
    row_after = row + 1
    qtty = file[row:row_after]['Quantity']
    return qtty[row]


def get_reseller_code(file, row):
    row_after = row + 1
    code = file[row:row_after]['Code']
    return code[row]


def get_product_details(file, row):
    row_after = row + 1
    item = file[row:row_after]['Product'][row]
    if item == "Zero waste box - Beauty Products (Med)":
        return ['ZWB - Beauty Products (Medium)', 893086008752, 170.97]
    elif item == 'Zero waste box - Beauty Products (Small)':
        return ['ZWB - Beauty Products (Small)', 893086008745, 145.08]

    elif item == 'Zero waste box - Binders (Med)':
        return ['ZWB - Binders (Medium)', 893086001760, 166.37]
    elif item == 'Zero waste box - Binders (Small)':
        return ['ZWB - Binders (Small)', 893086003122, 142.01]

    elif item == 'Zero waste box - Breakroom Separation (Med)':
        return ['ZWB - Breakroom Separation (Medium)', 893086002392, 129.65]
    elif item == 'Zero waste box - Breakroom Separation (Small)':
        return ['ZWB - Breakroom Separation (Small)', 893086001708, 111.98]

    elif item == 'Zero waste box - Cigarette Waste (Med)':
        return ['ZWB - Cigarette Waste (Medium)', 893086008899, 205]
    elif item == 'Zero waste box - Cigarette Waste (Small)':
        return ['ZWB - Cigarette Waste (Small)', 893086008882, 137.18]

    elif item == 'Zero waste box - Coffee capsules (Small)':
        return ['ZWB - Coffee Capsules (Small)', 893086001715, 143.49]

    elif item == 'Zero waste box - Beard and Hair Nets (Med)':
        return ['ZWB - Hair nets and beard nets (Medium)', 893086002378, 150.75]
    elif item == 'Zero waste box - Beard and Hair Nets (Small)':
        return ['ZWB - Hair nets and beard nets (Small)', 893086001685, 133.64]

    elif item == 'Zero waste box - Mailroom Supplies (Med)':
        return ['ZWB - Mailroom Supplies (Medium)', 893086002125, 132.88]
    elif item == 'Zero waste box - Mailroom Supplies (Small)':
        return ['ZWB - Mailroom Supplies (Small)', 893086001432, 119.69]

    elif item == 'Zero waste box - Media Storage (Small)':
        return ['ZWB - Media Storage (Small)', 893086002941, 168.15]

    elif item == 'Zero waste box - Office Supplies (Small)':
        return ['ZWB - Office Supplies (Small)', 893086007922, 139.99]

    elif item == 'Zero waste box - Pens and Markers (Med)':
        return ['ZWB - Pens and Markers (Medium)', 893086002163, 216.19]
    elif item == 'Zero waste box - Pens and Markers (Small)':
        return ['ZWB - Pens and Markers (Small)', 893086001470, 145.83]

    elif item == 'Zero waste box - Plastic Gloves (Med)':
        return ['ZWB - Plastic Gloves (Medium)', 893086002361, 205.16]
    elif item == 'Zero waste box - Plastic Gloves (Small)':
        return ['ZWB - Plastic Gloves (Small)', 893086001678, 167.84]

    elif item == 'Zero waste box - Safety Equipment (Med)':
        return ['ZWB - Safety Equipment and Protective Gear (Medium)', 893086002361, 205.16]
    elif item == 'Zero waste box - Safety Equipment (Small)':
        return ['ZWB - Safety Equipment and Protective Gear (Small)', 893086001678, 167.84]

    elif item == 'Zero waste box - Plastic Gloves (Med)':
        return ['ZWB - Plastic Gloves (Medium)', 893086006710, 198.18]
    elif item == 'Zero waste box - Plastic Gloves (Small)':
        return ['ZWB - Plastic Gloves (Small)', 893086003573, 136.08]

    elif item == 'Zero waste box - Snack Wrappers (Med)':
        return ['ZWB - Snack Wrappers (Medium)', 893086002248, 125.47]
    elif item == 'Zero waste box - Snack Wrappers (Small)':
        return ['ZWB - Snack Wrappers (Small)', 893086006819, 110.08]

    elif item == 'Zero waste box - Straws (Med)':
        return ['ZWB - Straws (Medium)', 99999999, 0]

    elif item == 'Zero waste box - Toys (Med)':
        return ['ZWB - Toys (Medium)', 893086002316, 194.11]
    elif item == 'Zero waste box - Toys (Small)':
        return ['ZWB - Toys (Small)', 893086001623, 155.02]
    else:
        pass


def get_total_price(file, row):
    [name, SKU, price] = get_product_details(file, row)
    quantity = get_quantity(file, row)
    total_price = quantity * price
    return total_price


def create_all_cols_oneorder(filename, num_cost):
    # num_cost is the equivalent of the number of line in which the order is placed
    ship_ad = shipping_address(filename, num_cost)
    ship_ad_towrite = {'Customer Name': 'Australia Post',
                       'Shipping Name': ship_ad[0],
                       'Address': ship_ad[1],
                       'City': ship_ad[2],
                       'State': ship_ad[3],
                       'Postcode': ship_ad[4],
                       'Country': ship_ad[5],
                       'Phone': refine_phone(ship_ad[6][num_cost]),
                       'Email': ship_ad[7]}

    ship_ad_cols = ['Customer Name', 'Shipping Name', 'Address', 'City', 'State', 'Postcode', 'Country', 'Phone',
                    'Email']

    # define dataframe
    df = pandas.DataFrame(ship_ad_towrite, columns=ship_ad_cols)

    df['Shipping Phone'] = df['Phone']

    add_new_col(df, 'Currency', 'AUD')

    add_new_col(df, 'Billing Name', 'Australia Post')
    add_new_col(df, 'Billing Address', 'Level 26 Lonsdale St')
    add_new_col(df, 'Billing State', 'VIC')
    add_new_col(df, 'Billing Postcode', '3000')
    add_new_col(df, 'Billing Country', 'Australia')

    # if there is only one person ordering and the person has only ordered one type of ZWB:
    # then len(AP_myfile) is the number of different ZWB they have ordered

    add_new_col(df, 'Date', get_date(filename, num_cost))
    add_new_col(df, 'Expected Shipment Date', get_expected_shipment_date(filename))
    add_new_col(df, 'Reference #', get_order_number(filename, num_cost))
    add_new_col(df, 'Reference # 2', get_order_number(filename, num_cost)[3:])

    add_new_col(df, 'Item name', get_product_details(filename, num_cost)[0])
    add_new_col(df, 'SKU', get_product_details(filename, num_cost)[1])
    add_new_col(df, 'Item Price', get_product_details(filename, num_cost)[2])
    add_new_col(df, 'Quantity', get_quantity(filename, num_cost))
    add_new_col(df, 'Code', get_reseller_code(filename, num_cost))
    add_new_col(df, 'Total Price', get_total_price(filename, num_cost))
    add_new_col(df, 'Channel', 'Australia Post')
    add_new_col(df, 'Channel 2', 'Australia Post')

    add_new_col(df, 'Sales Order Level Tax', 'GST')
    add_new_col(df, 'Sales Order Level Tax %', 10)
    add_new_col(df, 'Sales Order Level Tax Exemption Reason', 'GST FREE')
    add_new_col(df, 'Is Discount Before Tax', 'true')
    add_new_col(df, 'Entity Discount Percent', 0)

    return df


def create_all_cols_multipleorders(filename, start_line, end_line):
    ship_ad = shipping_address(filename, start_line)
    ship_ad_towrite = {'Customer Name': 'Australia Post',
                       'Shipping Name': ship_ad[0],
                       'Address': ship_ad[1],
                       'City': ship_ad[2],
                       'State': ship_ad[3],
                       'Postcode': ship_ad[4],
                       'Country': ship_ad[5],
                       'Phone': refine_phone(ship_ad[6][start_line]),
                       'Email': ship_ad[7]}

    ship_ad_cols = ['Customer Name', 'Shipping Name', 'Address', 'City', 'State', 'Postcode', 'Country', 'Phone',
                    'Email']

    # define dataframe
    df = pandas.DataFrame(ship_ad_towrite, columns=ship_ad_cols)

    df['Shipping Phone'] = df['Phone']

    add_new_col(df, 'Currency', 'AUD')

    add_new_col(df, 'Billing Name', 'Australia Post')
    add_new_col(df, 'Billing Address', 'Level 26 Lonsdale St')
    add_new_col(df, 'Billing State', 'VIC')
    add_new_col(df, 'Billing Postcode', '3000')
    add_new_col(df, 'Billing Country', 'Australia')

    # now we have to see all the products the person has ordered
    # we will have to do as many rows as orders the person has asked for
    add_new_col(df, 'Date', get_date(filename, start_line))
    add_new_col(df, 'Expected Shipment Date', get_expected_shipment_date(filename))
    add_new_col(df, 'Reference #', get_order_number(filename, start_line))
    add_new_col(df, 'Reference # 2', get_order_number(filename, start_line)[3:])  # we need to adapt to Zoho's bullshit

    add_new_col(df, 'Channel', 'Australia Post')
    add_new_col(df, 'Channel 2', 'Australia Post')  # Zoho's cowpoop

    add_new_col(df, 'Sales Order Level Tax', 'GST')
    add_new_col(df, 'Sales Order Level Tax %', 10)
    add_new_col(df, 'Sales Order Level Tax Exemption Reason', 'GST FREE')
    add_new_col(df, 'Is Discount Before Tax', 'true')
    add_new_col(df, 'Entity Discount Percent', 0)

    length_array = end_line - start_line  # this is the length of our new table and array

    df = df.append([df] * length_array, ignore_index=True)

    array_strings = ['' for x in range(length_array + 1)]  # python needs a + 1
    array_SKU = ['' for x in range(length_array + 1)]
    array_item_price = ['' for x in range(length_array + 1)]
    array_qtty = ['' for x in range(length_array + 1)]
    array_code = ['' for x in range(length_array + 1)]
    array_total_price = ['' for x in range(length_array + 1)]

    for i in range(0, length_array + 1):
        array_strings[i] = get_product_details(filename, i + start_line)[0]
        array_SKU[i] = get_product_details(filename, i + start_line)[1]
        array_item_price[i] = get_product_details(filename, i + start_line)[2]
        array_qtty[i] = get_quantity(filename, i + start_line)
        array_code[i] = get_reseller_code(filename, i + start_line)
        array_total_price[i] = get_total_price(filename, i + start_line)

    df.insert(10, 'Item name', array_strings)
    df.insert(11, 'SKU', array_SKU)
    df.insert(12, 'Item Price', array_item_price)
    df.insert(13, 'Quantity', array_qtty)
    df.insert(14, 'Code', array_code)
    df.insert(15, 'Total Price', array_total_price)

    return df


def csv_name(row_to_order):
    ordername = get_order_number(AP_myfile, row_to_order)
    ordername = ordername + '.csv'
    return ordername


## start of file..........................

# here the code starts referring to the above definitions:
# change aporder.csv for the filename you want. Must include and be in the format .csv

AP_myfile = read_csv_file('aporder.csv')
number_of_orders = get_number_of_orders(AP_myfile)  # number of orders is number of people who have

if number_of_orders == 0:
    # if there is only 1 customer ordering that day
    # i did that specifically because some days there is only 1 costumer ordering, and for better understanding of the code
    # write all the necessary information for the shipping address:

    if len(AP_myfile) == 1:  # if that customer has only ordered 1 thing:
        my_dataframe = create_all_cols_oneorder(AP_myfile, 0)
        export_csv = my_dataframe.to_csv(csv_name(0), index=None,
                                         header=True)  # here you have to write path, where result file will be stored
        print('File exported correctly. Your file is called', csv_name(0))

    else:  # if that customer has ordered more than 1 thing:
        my_dataframe = create_all_cols_multipleorders(AP_myfile, 0, len(AP_myfile) - 1)
        export_csv = my_dataframe.to_csv(csv_name(0), index=None, header=True)
        print('File exported correctly. Your file is called', csv_name(0))


# una altra manera seria fer un vector o crear tantes variables com customers hi hagi i llavors update el numero d'ordres de cada customer al numero de varialbees
# aixi evitariem el loop de l'if

else:
    j = 0
    new_startline = 0
    k = 0
    while j < len(AP_myfile):

        if k + 1 >= len(AP_myfile):

            if ((
                    k - new_startline) == 0):  # if the person which the code is going through has only ordered 1 type of box:
                my_dataframe = create_all_cols_oneorder(AP_myfile, j)
                export_csv = my_dataframe.to_csv(csv_name(j), index=None, header=True)
                new_startline = k + 1  # update the startline
                print('File exported correctly. The customer ordered 1 box type. Your file is called', csv_name(j))

            else:  # however, if it has ordered several types of boxes:

                my_dataframe = create_all_cols_multipleorders(AP_myfile, new_startline, k)
                # new_startline = k+1 no need to update because it is end of file
                export_csv = my_dataframe.to_csv(csv_name(j), index=None, header=True)
                print('File exported correctly. The customer orderered', k - new_startline + 1,
                      'different products. Your file is called', csv_name(k))


        elif get_order_number(AP_myfile, k) != get_order_number(AP_myfile, k + 1):  # or the end of the file!!!

            if ((
                    k - new_startline) == 0):  # if the person which the code is going through has only ordered 1 type of box:
                my_dataframe = create_all_cols_oneorder(AP_myfile, j)
                export_csv = my_dataframe.to_csv(csv_name(j), index=None, header=True)
                new_startline = k + 1  # update the startline
                print('File exported correctly. A customer ordered 1 box type. Your file is called', csv_name(j))

            else:  # however, if it has ordered several types of boxes:
                my_dataframe = create_all_cols(AP_myfile, new_startline, k)
                new_startline = k + 1
                export_csv = my_dataframe.to_csv(csv_name(0), index=None,
                                                 header=True)  # here you have to write path, where result file will be stored
                print('File exported correctly. The customer orderered', k - new_startline + 1,
                      'different products. Your file is called', csv_name(k))

        else:  # that means if the following order coming in the file is from the same customer
            pass

        k += 1
        j += 1

    ## end of file..........................
# https://www.guru99.com/python-csv.html
