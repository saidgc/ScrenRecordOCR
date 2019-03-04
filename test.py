import csv

if __name__ == "__main__":
    with open('read1.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        fecha = "algo"
        for row in reader:
            if fecha != row['date']:
                print(row['value'], row['date'])
                fecha = row['date']

