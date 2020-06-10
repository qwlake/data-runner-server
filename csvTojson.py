import csv

if __name__ == '__main__':
    data = []
    with open('C:\\Users\\김재연\\Desktop\\메이저러너\\한국농어촌공사_농어촌체험마을_20191223.csv', 'r') as inputFile, \
            open('C:\\Users\\김재연\\Desktop\\메이저러너\\test.json', 'w') as outputFile:
        reader = csv.reader(inputFile)
        col_names = next(reader)
        json_file = ""
        for cols in reader:
            doc = {col_name: col for col_name, col in zip(col_names, cols)}
            data.append(doc)
        print(data, file=outputFile)
    print(data)
