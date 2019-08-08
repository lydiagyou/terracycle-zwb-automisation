# terracycle-zwb-automisation
Summary: This program automatically take an orders CSV from Australia Post and outputs a file (with all orders combined) to be imported into Zoho.

## Things that need to be changed
-Get the name of the person and put that in another column (so it's clear on Zoho import to select that column) 
-Time needs to be cut out and the order date put into one column
-Product name needs to be changed to exactly what the item name is in Zoho (using a dictionary)
-generate a reference number (AP-something)
-expected shipment date (next business day)

## Stuff that's the same for every order
-Customer name needs to be changed to Australia Post
-Channel = Australia Post
-Sales Order level tax, tax %
-Sales Order Level Tax Exemption Reason	
-Is Discount Before Tax
-Entity Discount Percent

?? what if there's a business name - put that in Street 1
