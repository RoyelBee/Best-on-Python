import pdftables_api

# c = pdftables_api.Client('my-api-key')
# c.xlsx('D:/Python Code/Best-on-Python/Data/a.pdf', 'output.xlsx')
#replace c.xlsx with c.csv to convert to CSV
#replace c.xlsx with c.xml to convert to XML
#replace c.xlsx with c.html to convert to HTML


import pdftables_api

import pdftables_api

c = pdftables_api.Client('y5xragibebq3',  timeout=(60, 180))
c.xlsx('D:/Python Code/Best-on-Python/Data/a.pdf', 'output.xlsx')

# To get authentication Key you have to create a account in
# https://pdftables.com/pdf-to-excel-api

# Here timeout 60 is . It will used 60 seconds to connect with server and 180 seconds to convert the pdf into excel.
