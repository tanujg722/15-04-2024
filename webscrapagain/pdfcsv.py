import csv
# Open the file
data = open('example.csv',encoding='utf-8')
# csv.reader
csv_data = csv.reader(data)
#reformat it into a python object list of lists
data_lines =  list(csv_data)
#print(data_lines)
#print(data_lines[1])
#print(len(data_lines))
#for line in data_lines[:5]:
    #print(line)
#all_emails = []
#for line in data_lines[1:15]:
 #   all_emails.append(line[3])

#print(all_emails)
#full_name =[]
#for i in data_lines[1:10]:
 #   full_name.append(i[1]+' '+i[2])
#print(full_name)
# how to make a csv file
file_to_output = open('tanuj.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()