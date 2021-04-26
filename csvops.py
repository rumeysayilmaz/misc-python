import csv


def read_server_settings():
    server_settings_file = open('serverdetails.csv')
    # server_settings_dic_reader = csv.DictReader(server_settings_file, ['username', 'servername', 'ip'])
    server_settings_dic_reader = csv.DictReader(server_settings_file)
    for row in server_settings_dic_reader:
        print(row['username'], row['servername'], row['ip'])
    server_settings_file.close()
    return


def write_server_settings():
    server_settings_file = open('serverdetails.csv', 'w', newline='')
    server_settings_file_writer = csv.DictWriter(server_settings_file, ['username', 'servername', 'ip'])
    server_settings_file_writer.writeheader()
    server_settings_file_writer.writerow({'username': 'x', 'servername': 'y', 'ip': '125.34.9.0'})
    server_settings_file.close()


if __name__ == '__main__':
    read_server_settings()
    # write_server_settings()
