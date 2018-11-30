# CSV & TopoJSON data for Cartography usage

## Without Antarctica ?

removed Polygons with id's:
- 010 (Antarctica)
- 260 (French Southern Territories)

## Enriched ?

Each Polygon is defined by an `id`. I added 5 extra fields:
- `country_name_en`
- `country_code_2`
- `country_code_3`
- `country_region_en`
- `country_sub_region_en`

### Example

```
{
  "id": 250,
  "country_name_en": "France",
  "country_code_2": "FR",
  "country_code_3": "FRA",
  "country_region_en": "Europe",
  "country_sub_region_en": "Western Europe",
  "type": "MultiPolygon",
  "arcs": [...]
}
```

### Links

https://en.wikipedia.org/wiki/ISO_3166-1_numeric

