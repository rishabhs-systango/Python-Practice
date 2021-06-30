from output import *
class SalesTax :
   
    def calculateSalestax(self,list_input_lines) :
        # creating list which will store the data which should be returned as output
        # and placing product details at index 0
        list_output = ['Product-Name,Product-CostPrice,Product-SalesTax,Product-SalesTaxAmount,Product-FinalPrice,Country\n']

        i =1
        # loop is starting from index 1 because we already stored product headings at index 0  
        # looping through each lines of input file
        while i < len(list_input_lines) :
            #spliting each list of input lines  in seperate values and storing it in a list like
            #Product-Name(list_by_values[0]),Product-CostPrice(list_by_values[1]),
            # Product-SalesTax-Percentage(list_by_values[2]),Country(list_by_values[3])
            list_by_values = list_input_lines[i].split(',')
            try :
                # checking is any input line is blank or not containg proper field
                if len(list_by_values) != 4 :
                    list_output.append("Input not Proper\n")
                    raise Exception (f"Input in line {i+1} shoud be filled Properly for each columnn")
                else :
                    # checking is costrPrice and sales tax are number or not
                    if len(list_by_values) == 4 and list_by_values[2].isdigit() and list_by_values[1].isdigit() :
                        salesTax = float(list_by_values[2])
                        salesTaxAmount = (salesTax/100)*float(list_by_values[1])
                        FinalPrice = float(list_by_values[1])+salesTaxAmount
                        # appending [Product-Name,Product-CostPrice,Product-SalesTax,
                        # Product-SalesTaxAmount,Product-FinalPrice,Country] in string than appending it to list_output
                        str = f"{list_by_values[0]},{list_by_values[1]},{list_by_values[2]},{salesTaxAmount},{FinalPrice},{list_by_values[3]}\n"
                        list_output.append(str)
                    else :
                        list_output.append("Input not Proper\n")
                        raise Exception(f"Input in line {i+1}  is not Proper costprice,salesTax should be number")
            except Exception as obj :
                print(obj)
            i = i + 1
        # calling write output method to write in output file    
        outputObj = Output()
        outputObj.writeOutput(list_output)