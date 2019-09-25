import json
import csv
import pandas as pd


# duplicate 'name' into 'pretty-name'
def duplicate_column(filename):

    csv_data = []

    with open(filename + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for idx, row in enumerate(reader):
            if idx == 0:
                csv_data.append([row[0], "pretty-name", row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
            else:
                try:
                    csv_data.append([row[0], row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
                except:
                    print(idx)

    with open(filename + "_enriched.csv", 'wb') as f:
        wr = csv.writer(f, delimiter=',', lineterminator='\n')
        wr.writerows(csv_data)


def add_capitals(filename):

    capitals = pd.read_csv("capitals.csv", index_col="Country code", delimiter=";", encoding="utf-8")
    # countries = pd.read_csv(filename + ".csv", encoding="utf-8")
    csv_data = []

    with open(filename + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for idx, row in enumerate(reader):
            if idx == 0:
                row.extend(['capital-name', 'capital-lat', 'capital-lng'])
                csv_data.append(row)
            else:
                try:
                    capital = capitals.loc[row[2]]
                    row.extend([capital["City (en)"], str(capital["Latitude"]), str(capital["Longitude"])])
                    csv_data.append(row)
                except:
                    print(row[0])
                    row.extend(["", "", ""])
                    csv_data.append(row)

    with open(filename + "_capitals.csv", 'wb') as f:
        wr = csv.writer(f, delimiter=',', lineterminator='\n')
        wr.writerows(csv_data)


def csv_to_json(filename):

    result = {}

    with open(filename + '.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for idx, row in enumerate(reader):
            if idx > 0:
                result[row[5]] = row[4]
        
    with open('geonames.json', 'w') as outfile:
        json.dump(result, outfile)


"""
main()
"""
if __name__ == '__main__':

    # filename = "country_alphas_regions_continent_enriched"
    # filename = "geonames"

    # duplicate_column(filename)
    # add_capitals(filename)
    # csv_to_json(filename)
