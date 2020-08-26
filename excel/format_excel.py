import pandas
import re

exportExcelData = pandas.read_excel('product_category_name_translation.xlsx', sheetname='Sheet 1')

# print whole sheet data
# print(exportExcelData)

# print(exportExcelData.columns.ravel())

productList = exportExcelData['product_category_name'].tolist()

formatedProducts = []

for oneData in range(len(productList)):
    formatedProducts.append(re.sub(r'[_]',' ',productList[oneData]))

# Create a Pandas dataframe from the data.
df = pandas.DataFrame({'product_category_name': formatedProducts})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pandas.ExcelWriter('formated_product_category_name.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()