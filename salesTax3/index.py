import os
from salesTax import *

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

#calling open Input file method to read input file        
try :
    inputObj = Input()
    inputObj.openInputFile()
except Exception as obj :
    print(obj)