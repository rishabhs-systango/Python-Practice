class Output :
    def writeOutput(Self,list_output) : 
        #opening input file
        # if os.path.isfile('output.csv') :
        f_output = open('output.csv',mode = 'w')
        # writing the output list in output.csv file
        f_output.writelines(list_output)
        f_output.close()