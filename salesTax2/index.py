import os

class Input :
    def openInputFile(self) :
        #opening input file
        if os.path.isfile('input.csv') :
            f_input = open('input.csv',mode = 'r')
            #reading input file
            data = f_input.read()
            f_input.close()
            #spliting input file by lines and storing it in a list
            list_input_lines = data.split('\n')
            # calling calculateSalesTax method to calculate sales Tax and final price
            salesTaxObj = SalesTax()
            salesTaxObj.calculateSalestax(list_input_lines)
        else :
            raise Exception ('Input File dosent Exist')

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
            salesTax = float(list_by_values[2])
            salesTaxAmount = (salesTax/100)*float(list_by_values[1])
            FinalPrice = float(list_by_values[1])+salesTaxAmount
            # appending [Product-Name,Product-CostPrice,Product-SalesTax,
            # Product-SalesTaxAmount,Product-FinalPrice,Country] in string than appending it to list_output
            str = f"{list_by_values[0]},{list_by_values[1]},{list_by_values[2]},{salesTaxAmount},{FinalPrice},{list_by_values[3]}\n"
            list_output.append(str)
            i+=1
        # calling write output method to write in output file    
        outputObj = Output()
        outputObj.writeOutput(list_output)

class Output :
    def writeOutput(Self,list_output) : 
        #opening input file
        if os.path.isfile('output.csv') :
            f_output = open('output.csv',mode = 'w')
            # writing the output list in output.csv file
            f_output.writelines(list_output)
            f_output.close()

#calling open Input file method to read input file        
try :
    inputObj = Input()
    inputObj.openInputFile()
except Exception as obj :
    print(obj)
