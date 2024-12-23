import csv

def read_csv(filename):
    """Read and output the details of CSV file."""
    try:
        with open(filename, newline='') as csv_file:  # автоматичне закриття ресурсів після виконання коду
            # newline='': Це означає, що символи нового рядка не будуть автоматично перетворюватися при читанні або записі файлу
            csv_reader = csv.DictReader(csv_file)  # method returns an iterable 'reader' object
            for record in csv_reader:
                print(record)
    except (IOError, OSError) as file_read_error:  # IOError - Input/Output. OSError - OS помилки.
        print(f'Unable to open the csv_pdf file. Exception: {file_read_error}')


if __name__ == '__main__':
    read_csv('market_cap.csv')