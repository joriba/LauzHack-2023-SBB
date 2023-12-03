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

let coordinates_car = coordinates[0]
let coordinates_train = coordinates[1]

let coordinates_car_proj = coordinates_car.map(x => fromLonLat(x, 'EPSG:3857'))
let coordinates_train_proj = coordinates_train.map(x => fromLonLat(x, 'EPSG:3857'))

let combined = [...coordinates_car, ...coordinates_train]
let first = combined[0]
let last = combined[combined.length - 1]

let middle = [(first[0] + last[0]) / 2, (first[1] + last[1]) / 2]
let approx_length = Math.sqrt((first[0] - last[0])*(first[0] - last[0]) * 0.681 * 0.681 + (first[1] - last[1]) * (first[1] - last[1]))

console.log("Approx length:" + approx_length)

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
    center: fromLonLat(middle, 'EPSG:3857'),
    zoom: 9 - Math.log2(approx_length)
  })
});

var layerLinesCar = new VectorLayer({
    source: new VectorSource({
        features: [new Feature({
            geometry: new LineString(coordinates_car_proj),
            name: 'Line'
        })]
    }),
    style: new Style({
        fill: new Fill({ color: '#0000FF', weight: 10 }),
        stroke: new Stroke({ color: '#0000FF', width: 5 })
    })
});

map.addLayer(layerLinesCar)

var layerLinesTrain = new VectorLayer({
    source: new VectorSource({
        features: [new Feature({
            geometry: new LineString(coordinates_train_proj),
            name: 'Line'
        })]
    }),
    style: new Style({
        fill: new Fill({ color: '#FF0000', weight: 10 }),
        stroke: new Stroke({ color: '#FF0000', width: 5 })
    })
});

map.addLayer(layerLinesTrain)