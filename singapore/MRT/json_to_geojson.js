const d3 = require('d3@5');
const polyline = require('@mapbox/polyline'); // require('https://bundle.run/@mapbox/polyline')

// fetch data
const _singaporeMRTJSON = await d3.json('https://raw.githubusercontent.com/cheeaun/railrouter-sg/master/data/v2/all.json');

// init geojson
let _singaporeMRTGeoJSON = { type: "FeatureCollection", features: [] };

// process MRT lines
_singaporeMRTJSON.lines.forEach(line => {
  let _lineGeoJSON = polyline.toGeoJSON(line['coords']);
  _lineGeoJSON['properties'] = {
    type: 'line',
    name: '',
    color: line['colour']
  };
  _singaporeMRTGeoJSON.features.push(_lineGeoJSON);
});

// process MRT stops
_singaporeMRTJSON.stops.forEach(stop => {
  _singaporeMRTGeoJSON.features.push({
    type: "Feature",
    properties: {
      type: 'station',
      name: stop['name'],
      network: stop['network'],
      lines: stop['codes'].map(code => code['text']),
      wikipedia_url: stop['wikipedia_url'],
      wikipedia_image_url: stop['wikipedia_image_url'],
      name_zh: stop['name:zh'],
      name_hi: stop['name:hi']
    },
    geometry: { type: "Point", coordinates: stop['coord'].reverse() }
  });
})

// return
return _singaporeMRTGeoJSON;