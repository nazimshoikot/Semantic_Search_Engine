from tika import parser  
import os 
inpath = "./"
outpath = "./"

error_count = 0 #counts files which could not be read
correct_count = 0#counts files which were successfully read 

# opening pdf file in input directory
for file in os.listdir(inpath): 
    parsed_pdf = parser.from_file(os.path.join(inpath, file))
    
    #extract content from the files
    data = parsed_pdf['content'] 
    
    #catch error 
    if (not data): 
        error_count+=1
    
    #output the content into a text file with the same name 
    else: 
        data = data.replace("\n", "")
        outfilename  = file.split('.', 1)[0]
        outfilename = outfilename+".txt"
        outfile = open(os.path.join(outpath, outfilename), "w")
        outfile.write(data)
        outfile.close()
        correct_count+=1

print ("Files not read: ",error_count)
print ("Files read: ",correct_count)