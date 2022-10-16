import csv

def print_txt():
    with open('phone.txt', 'r', encoding='utf-8') as f:
        read_file = f.read()
    print(read_file)


def print_csv():
    with open('phone.csv', newline='', encoding='utf-8') as f:  
        reader = csv.reader(f)
        for row in reader:
            print(row)


def writing_txt():
    with open('phone.txt') as f:
        text = f.read()
    with open('new_phone', 'w') as f:
        f.write(text)


def writing_csv():
    with open('phone.csv') as f:
        text = csv.reader(f)
        with open('new_phone.csv', 'w') as f:
            writer = csv.writer(f)
            for row in text:
                writer.writerow(row)

