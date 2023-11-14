import csv


def createCSV(headerList, infoList, csvName):
    with open('data/'+csvName, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(headerList)
        writer.writerows(infoList)