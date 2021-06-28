from salesTax import dict
# opening both input and output file
f_input = open('input-File.csv',mode = 'r')
f_output = open('output-File.csv',mode = 'w')
#reading input file
data = f_input.read()
#spliting input file by lines and storing it in a list
list_input_lines = data.split('\n')
list_output = ['Product-Name,Product-CostPrice,Product-SalesTax,Product-SalesTaxAmount,Product-FinalPrice,Country\n']
# starting i from 1 coz at 0th index headings are placed 
i = 1
# looping through each lines of input file
while i < len(list_input_lines) :
    #spliting each list of input lines  in seperate values and storing it in a list like
    # [Product-Name,Product-CostPrice,Country]
    list_by_values = list_input_lines[i].split(',')
    salesTax = dict[list_by_values[2].strip()]
    salesTaxAmount = (salesTax/100)*float(list_by_values[1])
    FinalPrice = float(list_by_values[1])+salesTaxAmount
    # appending [Product-Name,Product-CostPrice,Product-SalesTax,
    # Product-SalesTaxAmount,Product-FinalPrice,Country] in string than appending it to list_output
    str = f"{list_by_values[0]},{list_by_values[1]},{salesTax},{salesTaxAmount},{FinalPrice},{list_by_values[2]}\n"
    list_output.append(str)
    i+=1
f_output.writelines(list_output)
f_input.close()
f_output.close()