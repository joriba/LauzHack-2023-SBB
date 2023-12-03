import './style.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import {Vector as VectorLayer} from 'ol/layer';
import {Vector as VectorSource} from 'ol/source';
import LineString from 'ol/geom/LineString';
import Feature from 'ol/Feature';
import {Fill, Style, Stroke} from 'ol/style';
import {fromLonLat} from 'ol/proj';
//import VectorTile from 'ol/source/VectorTile.js';
import TileImage from 'ol/source/TileImage.js';

let coordinates = eval(decodeURIComponent(window.location.hash.substring(1)))
if(coordinates == undefined){
  coordinates = []
}
coordinates = coordinates.map(x => fromLonLat(x, 'EPSG:3857'))

const api_key = new URL(window.location.href).search.substring(1)

const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new TileImage({
        url: "https://journey-maps-tiles.geocdn.sbb.ch/styles/base_bright_v2/{z}/{x}/{y}.webp?api_key="+api_key
      })
    })
  ],
  view: new View({
    center: fromLonLat([8.286928794895285, 46.73678128684938], 'EPSG:3857'),
    zoom: 8.5
  })
});

let lineFeature = new Feature({
            geometry: new LineString(coordinates),
            name: 'Line'
        })
var layerLines = new VectorLayer({
    source: new VectorSource({
        features: [lineFeature]
    }),
    style: new Style({
        fill: new Fill({ color: '#FF0000', weight: 10 }),
        stroke: new Stroke({ color: '#FF0000', width: 5 })
    })
});

map.addLayer(layerLines)