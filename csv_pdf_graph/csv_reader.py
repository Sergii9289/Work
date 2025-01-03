import csv

def read_csv(filename):
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for record in csv_reader:
                print(record.get('stock_symbol'))
    except (IOError, OSError) as file_read_error:
        print(f'Unable to open the csv_pdf file. Exception: {file_read_error}')

if __name__ == '__main__':
    read_csv('market_cap.csv')