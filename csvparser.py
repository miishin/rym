import csv

TITLE = 5
RELEASE_YEAR = 6
RATING = 7


class csvParser:

    def __init__(self, file_name: str):
        self.file_name = file_name

    # Return list of (Album_Name, Rating) for given year
    def get_albums_from_year(self, year: int) -> list[(str, int)]:
        result = []
        with open(self.file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[RELEASE_YEAR] == year:
                    result.append((row[TITLE], int(row[RATING])))
        return result

    def top_10_albums(self, year: int) -> list[str]:
        albums = self.get_albums_from_year(year)
        albums = list(reversed(sorted(albums, key=lambda x: x[1])))
        if len(albums) > 10:
            return albums[0:10]
        return albums
