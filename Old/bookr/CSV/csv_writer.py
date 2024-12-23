import csv

def write_csv(filename, header, data):
    """Write the provided data to the CSV file.
    :param str filename: The name of the file to which
    the data should be written
    :param list header: The header for the columns in
    csv_pdf_graph file
    :param list data: The list of list mapping the
    values to the columns
    """
    try:
        with open(filename, 'w') as csv_file:  # передаємо файл в змінну з можливістю перезапису
            # якщо файлу не існує, то створює новий
            csw_writer = csv.DictWriter(csv_file,
                                        fieldnames=header)  # отримуємо writer() об'єкт
            csw_writer.writeheader()  # зберігаємо header
            csw_writer.writerows(data)  # зберігаємо data
    except (IOError, OSError) as csv_file_error:
        print(f"Unable to write the contents to csv_pdf_graph file. Exception: {csv_file_error}")


if __name__ == '__main__':
    header = ['name', 'age', 'gender']
    data = [{'name': 'Richard', 'age': 32, 'gender': 'M'},
            {'name': 'Mumzil', 'age': 21, 'gender': 'F'},
            {'name': 'Melinda', 'age': 25, 'gender': 'F'}]
    filename = 'sample_output.csv'
    write_csv(filename, header, data)