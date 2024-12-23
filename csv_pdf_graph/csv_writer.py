import csv

def write_csv(filename, header, data):
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            csv_writer.writeheader()
            csv_writer.writerows(data)
    except (IOError, OSError) as csv_file_error:
        print(f'Unable to write the contents to csv_pdf file. Exception: {csv_file_error}')

if __name__ == '__main__':
    header = ['name', 'age', 'gender']
    data = [{'name': 'Richard', 'age': 32, 'gender': 'M'},
            {'name': 'Mumzil', 'age': 21, 'gender': 'F'},
            {'name': 'Melinda', 'age': 25, 'gender': 'F'}]
    filename = 'sample_output.csv'
    write_csv(filename=filename, header=header, data=data)