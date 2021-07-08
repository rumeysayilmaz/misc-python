import csv

csv_filename = 'serverdetails.csv'
fieldnames = ['username', 'servername', 'ip']


def create_csv_file():
    server_csv_file = open(csv_filename, 'w', newline='')
    server_settings_file_writer = csv.DictWriter(server_csv_file, fieldnames)
    server_settings_file_writer.writeheader()
    server_csv_file.close()


def read_server_settings():
    server_settings_file = open(csv_filename)
    # server_settings_dic_reader = csv.DictReader(server_settings_file, fieldnames)
    server_settings_dic_reader = csv.DictReader(server_settings_file)
    for row in server_settings_dic_reader:
        print(row['username'], row['servername'], row['ip'])
    server_settings_file.close()
    return


def write_server_settings():
    server_settings_file = open(csv_filename, 'w', newline='')
    server_settings_file_writer = csv.DictWriter(server_settings_file, fieldnames)
    server_settings_file_writer.writeheader()
    server_settings_file_writer.writerow({'username': 'x', 'servername': 'y', 'ip': '125.34.9.0'})
    server_settings_file.close()


if __name__ == '__main__':
    create_csv_file()
    read_server_settings()
    # write_server_settings()
