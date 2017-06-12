# coding='utf-8'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Import the modules
import json
import csv
import pandas as pd


def enrich_topojson(topojson_filename):

    with open(topojson_filename + ".json") as data_file:
        topojson_data = json.load(data_file)

    countries = pd.read_csv("../countries_capitals/country_alphas_regions_continent_enriched_capitals.csv", index_col="country-code", encoding="utf-8", delimiter=",", keep_default_na=False, na_values=[''])
    countries = countries.fillna("")

    print countries.shape


    for idx, geometry in enumerate(topojson_data["objects"]["countries"]["geometries"]):
        if topojson_data["objects"]["countries"]["geometries"][idx]["id"] >= 0:
            row = countries.loc[topojson_data["objects"]["countries"]["geometries"][idx]["id"]]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"] = {}
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_code_2"] = row["alpha-2"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_code_3"] = row["alpha-3"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_name_en"] = row["name"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_pretty_name_en"] = row["pretty-name"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_region_en"] = row["region"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_sub_region_en"] = row["sub-region"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_capital_en"] = row["capital-name"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_capital_lat"] = row["capital-lat"]
            topojson_data["objects"]["countries"]["geometries"][idx]["properties"]["country_capital_lng"] = row["capital-lng"]
            print topojson_data["objects"]["countries"]["geometries"][idx]


    with open(topojson_filename + "_enriched_with_capital.json", "w") as f:
        json.dump(topojson_data, f)
        # f.write(json.dumps(topojson_data))

"""
main()
"""
if __name__ == '__main__':

    topojson_filename = "world-50m-without-antarctica"

    enrich_topojson(topojson_filename)
