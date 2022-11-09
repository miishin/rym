import pandas

TITLE = 5
RELEASE_YEAR = 6
RATING = 7


class csvParser:

    def __init__(self, file_name: str):
        self.df = pandas.read_csv(file_name)
        self.df = self.df.drop(['RYM Album', 'First Name localized', ' Last Name localized', 'Ownership', 'Purchase Date', 'Media Type', 'Review'], axis=1)

    # Return list of (Album_Name, Rating) for given year
    def get_albums_from_year(self, year):
        return self.df.query("Release_Date == %s" % year)

    def get_best_albums(self, year):
        albums = self.get_albums_from_year(year)
        return albums.sort_values(by=['Rating'], ascending=False)
        
    def top_n_albums(self, year, n):
        return self.get_best_albums(year).head(n)

def main():
    csvp = csvParser('rym.csv')
    albums = csvp.get_best_albums("2022")
    albums = albums.query("Rating >= 8")
    #albums = csvp.top_n_albums("2022", 10)
    print(albums)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
