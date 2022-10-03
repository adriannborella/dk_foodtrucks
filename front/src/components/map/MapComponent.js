import React from "react";
import { useMapEvents } from "react-leaflet/hooks";
import "./MapComponent.scss";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import { useTrackFoods } from "../../hooks/useTrackFoods";

import L from "leaflet";
import iconShadow from "leaflet/dist/images/marker-shadow.png";

import icon_food_cart from "./food_cart.jpeg";
import icon_food_truck from "./food-truck.png";

let food_cart = L.icon({
  iconUrl: icon_food_cart,
  shadowUrl: iconShadow,
  iconSize: [32, 32],
});

let food_truck = L.icon({
  iconUrl: icon_food_truck,
  shadowUrl: iconShadow,
  iconSize: [32, 32],
});

function MyCustomMap(props) {
  let { getPlaces, center } = props;

  const map = useMapEvents({
    dragend: async (event) => {
      const position = map.getCenter();
      center = position;

      await getPlaces(position);
    },
  });
  return null;
}

export function MapComponent() {
  let center = [37.756865, -122.4564857];
  const zoom = 14;
  const { loading, getPlaces, data } = useTrackFoods();
  if (loading) {
    return (
      <div className="spinner-container">
        <div className="loading-spinner"></div>
      </div>
    );
  }
  if (data) {
    center = [data[0].latitude, data[0].longitude];
  }

  console.log(data);
  return (
    <MapContainer center={center} zoom={zoom} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {data != null &&
        data.map((place) => (
          <Marker
            position={[place.latitude, place.longitude]}
            icon={place.facilitytype == "Truck" ? food_truck : food_cart}
          >
            <Popup>
              <b>{place.applicant}</b>
              <br />
              <i>{place.address}</i>
              <br />
              <p>{place.locationdescription}</p>
              <br />
              <span>{place.facilitytype}</span>
              <br />
              <a href="{place.schedule}" target="new">
                Go to schedule
              </a>
            </Popup>
          </Marker>
        ))}
      <MyCustomMap getPlaces={getPlaces} center={center}></MyCustomMap>
    </MapContainer>
  );
}
