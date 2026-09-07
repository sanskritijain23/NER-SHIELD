export const locations = [
  {
    id: "loc-1",
    name: "Shillong",
    state: "Meghalaya",
    latitude: 25.5788,
    longitude: 91.8933,
    rainfall: 120,
    slope: 32,
    elevation: 1496,
    previousLandslide: true,
    riskScore: 82
  },
  {
    id: "loc-2",
    name: "Cherrapunji",
    state: "Meghalaya",
    latitude: 25.2818,
    longitude: 91.7208,
    rainfall: 450,
    slope: 45,
    elevation: 1484,
    previousLandslide: true,
    riskScore: 95
  },
  {
    id: "loc-3",
    name: "Nongstoin",
    state: "Meghalaya",
    latitude: 25.5204,
    longitude: 91.2676,
    rainfall: 80,
    slope: 20,
    elevation: 1409,
    previousLandslide: false,
    riskScore: 45
  },
  {
    id: "loc-4",
    name: "Aizawl",
    state: "Mizoram",
    latitude: 23.7271,
    longitude: 92.7176,
    rainfall: 150,
    slope: 50,
    elevation: 1132,
    previousLandslide: true,
    riskScore: 91
  },
  {
    id: "loc-5",
    name: "Lunglei",
    state: "Mizoram",
    latitude: 22.8837,
    longitude: 92.7385,
    rainfall: 90,
    slope: 35,
    elevation: 722,
    previousLandslide: false,
    riskScore: 65
  },
  {
    id: "loc-6",
    name: "Kohima",
    state: "Nagaland",
    latitude: 25.6701,
    longitude: 94.1077,
    rainfall: 110,
    slope: 38,
    elevation: 1444,
    previousLandslide: true,
    riskScore: 78
  },
  {
    id: "loc-7",
    name: "Dimapur",
    state: "Nagaland",
    latitude: 25.9060,
    longitude: 93.7275,
    rainfall: 50,
    slope: 5,
    elevation: 145,
    previousLandslide: false,
    riskScore: 15
  },
  {
    id: "loc-8",
    name: "Gangtok",
    state: "Sikkim",
    latitude: 27.3389,
    longitude: 88.6065,
    rainfall: 130,
    slope: 42,
    elevation: 1650,
    previousLandslide: true,
    riskScore: 85
  },
  {
    id: "loc-9",
    name: "Guwahati",
    state: "Assam",
    latitude: 26.1445,
    longitude: 91.7362,
    rainfall: 60,
    slope: 15,
    elevation: 55,
    previousLandslide: false,
    riskScore: 28
  }
];

export const getLocations = () => {
  return Promise.resolve(locations);
};

export const getLocationRisk = (locationId) => {
  const location = locations.find(loc => loc.id === locationId);
  return Promise.resolve(location);
};
