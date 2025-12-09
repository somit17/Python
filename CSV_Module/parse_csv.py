import csv

#next(csv_reader) #skip 1st row
# print(line[2]) #2nd delimiter value
with open('currency.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_currency.csv','w') as new_file:
        csv_writer= csv.writer(new_file,delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)
