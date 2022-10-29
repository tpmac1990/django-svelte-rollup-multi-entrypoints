import * as L from 'leaflet';

const curveMidpointTheta = Math.PI / 10;
const cosCurveMidpointTheta = Math.cos(curveMidpointTheta);

function calculateCurve(from, to) {
  let lineAngle = Math.atan2(to.lat - from.lat, to.lng - from.lng);
  let lineMidPointDistance =
    Math.sqrt((to.lng - from.lng) ** 2 + (to.lat - from.lat) ** 2) / 2;
  let hypotenuse = lineMidPointDistance / cosCurveMidpointTheta;
  let totalTheta = lineAngle + curveMidpointTheta;

  return L.latLng(
    hypotenuse * Math.sin(totalTheta) + from.lat,
    hypotenuse * Math.cos(totalTheta) + from.lng
  );
}

export default function makeLineCoordinates(
  map,
  from,
  to,
  reverse
) {
  let curveMidpoint = calculateCurve(reverse ? to : from, reverse ? from : to);
  // Designed for use with the Curve component.
  return [
    'M',
    [from.lat, from.lng],
    'Q',
    [curveMidpoint.lat, curveMidpoint.lng],
    [to.lat, to.lng],
  ];
}
