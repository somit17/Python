import csv

with open('currency.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_currency_dict.csv','w') as new_file:
        fieldnames=['Code','Symbol','Name']
        csv_writer= csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='-')
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)