# CSV & TopoJSON data for Cartography usage

## Without Antarctica?

removed Polygons with id's:
- 010 (Antarctica)
- 260 (French Southern Territories)

## Enriched?

Each Polygon is defined by an `id`. I added a couple of extra fields.

filename: `..._enriched.json`
```
country_name_en
country_code_2
country_code_3
country_region_en
country_sub_region_en
```

filename `..._enriched_with_capital.json`
```
country_name_en
country_code_2
country_code_3
country_region_en
country_sub_region_en
country_capital_en
country_capital_lat
country_capital_lng
```

filename `..._enriched_with_capital_and_geoname.json`
```
country_name_en
country_code_2
country_code_3
country_region_en
country_sub_region_en
country_capital_en
country_capital_lat
country_capital_lng
geoname_id
```

filename `..._enriched_with_geoname.json`
```
country_name_en
country_code_2
country_code_3
country_region_en
country_sub_region_en
geoname_id
```


### Example

```
{
  "id": 250,
  "country_name_en": "France",
  "country_code_2": "FR",
  "country_code_3": "FRA",
  "country_region_en": "Europe",
  "country_sub_region_en": "Western Europe",
  "country_capital_en": "Paris",
  "country_capital_lat": 48.85341,
  "country_capital_lng": 2.3488,
  "geoname_id": 3017382,
  "type": "MultiPolygon",
  "arcs": [...]
}
```

### Links

https://en.wikipedia.org/wiki/ISO_3166-1_numeric

