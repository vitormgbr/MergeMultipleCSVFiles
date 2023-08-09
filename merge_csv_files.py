#import pandas and os modules
import pandas as pd
import os

#read the path
file_path = r"FILE_PATH"  #insert file path here in between quotation marks

#list all the files from the directory
file_list = os.listdir(file_path)

#remove this python program and the resulting Merger.csv file from list of files to be merged
if "merge_csv_files.py" in file_list: file_list.remove("merge_csv_files.py")
if "merged_csv.csv" in file_list: file_list.remove("merged_csv.csv")

#define a readcsv function to change the read_csv() function arguments before the concat() function
def readcsv(args):
    return pd.read_csv(args, encoding ='latin1') #latin1 encoding allows any character in any cell from the input

#merge all csv files inside file_list into a merged_csv.csv file
df = pd.concat(map(readcsv, file_list))                                 
df.to_csv('merged_csv.csv', index=False, encoding='latin1') #latin1 encoding allows any character in any cell of the output

#console print confirming the conversion
print("File 'merged_csv.csv' successfully created in {}".format(file_path))