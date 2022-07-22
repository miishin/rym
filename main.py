import csvparser as cpr


def main():
    csvp = cpr.csvParser('rym.txt')
    albums = csvp.top_10_albums("2022")
    for a in albums:
        print(a)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
