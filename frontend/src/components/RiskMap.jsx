import React, { useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { locations } from '../data/locations';
import { getRiskClassification } from '../utils/riskUtils';
import { Map as MapIcon } from 'lucide-react';

// Custom icons based on risk level
const createIcon = (color) => {
  return L.divIcon({
    className: 'custom-marker',
    html: `
      <div style="
        background-color: ${color === 'green' ? '#22c55e' : color === 'yellow' ? '#eab308' : color === 'orange' ? '#f97316' : '#dc2626'};
        width: 20px;
        height: 20px;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
      "></div>
    `,
    iconSize: [20, 20],
    iconAnchor: [10, 10],
  });
};

// Component to handle map centering
const MapController = ({ selectedLocationId }) => {
  const map = useMap();

  useEffect(() => {
    if (selectedLocationId) {
      const location = locations.find(loc => loc.id === selectedLocationId);
      if (location) {
        map.flyTo([location.latitude, location.longitude], 10, {
          duration: 1.5,
        });
      }
    }
  }, [selectedLocationId, map]);

  return null;
};

export const RiskMap = ({ selectedLocationId, onMarkerClick }) => {
  // Default center (Northeast India roughly)
  const defaultCenter = [25.5788, 92.5];
  const defaultZoom = 7;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-2 relative h-[500px] flex flex-col mb-6">
      <div className="absolute top-4 left-4 z-[1000] bg-slate-900/90 backdrop-blur-sm text-white px-4 py-2 rounded-lg flex items-center space-x-2 shadow-lg">
        <MapIcon size={18} />
        <h2 className="font-semibold text-sm tracking-wide">Risk Map &ndash; Northeast India</h2>
      </div>

      <div className="flex-1 rounded-lg overflow-hidden relative z-0">
        <MapContainer 
          center={defaultCenter} 
          zoom={defaultZoom} 
          style={{ height: '100%', width: '100%' }}
          zoomControl={false}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />
          
          {/* Add custom zoom control position */}
          <div className="leaflet-top leaflet-left mt-14 ml-2">
            <div className="leaflet-control-zoom leaflet-bar leaflet-control">
              <a className="leaflet-control-zoom-in" href="#" title="Zoom in" role="button" aria-label="Zoom in">+</a>
              <a className="leaflet-control-zoom-out" href="#" title="Zoom out" role="button" aria-label="Zoom out">&#x2212;</a>
            </div>
          </div>

          <MapController selectedLocationId={selectedLocationId} />

          {locations.map((loc) => {
            const risk = getRiskClassification(loc.riskScore);
            return (
              <Marker 
                key={loc.id} 
                position={[loc.latitude, loc.longitude]}
                icon={createIcon(risk.mapColor)}
                eventHandlers={{
                  click: () => onMarkerClick(loc.id),
                }}
              >
                <Popup>
                  <div className="text-center p-1 min-w-[150px]">
                    <h3 className="font-bold text-slate-800 text-base border-b border-slate-100 pb-2 mb-2">{loc.name}</h3>
                    <div className="flex items-center justify-center space-x-2 mb-3">
                      <span className="text-sm text-slate-500">Score:</span>
                      <span className={`font-bold text-lg ${risk.color}`}>{loc.riskScore}/100</span>
                    </div>
                    <div className={`px-2 py-1 rounded text-xs font-bold text-white uppercase ${risk.bgColor}`}>
                      {risk.level} RISK
                    </div>
                    
                    <div className="mt-4 text-left border-t border-slate-100 pt-3">
                      <p className="text-xs text-slate-600 mb-1"><strong>Rainfall:</strong> {loc.rainfall} mm</p>
                      <p className="text-xs text-slate-600 mb-1"><strong>Slope:</strong> {loc.slope}°</p>
                      <p className="text-xs text-slate-600 mb-3"><strong>Previous Landslide:</strong> {loc.previousLandslide ? 'Yes' : 'No'}</p>
                      
                      <p className="text-xs text-slate-800 font-medium leading-relaxed bg-slate-50 p-2 rounded">
                        {risk.action}
                      </p>
                    </div>
                  </div>
                </Popup>
              </Marker>
            );
          })}
        </MapContainer>
      </div>

      <div className="absolute bottom-4 left-4 z-[1000] bg-slate-900/90 backdrop-blur-sm text-white p-3 rounded-lg shadow-lg">
        <ul className="space-y-2 text-xs font-medium">
          <li className="flex items-center space-x-2">
            <span className="w-3 h-3 rounded-full bg-green-500 border-2 border-white shadow-sm"></span>
            <span>Low Risk</span>
          </li>
          <li className="flex items-center space-x-2">
            <span className="w-3 h-3 rounded-full bg-yellow-500 border-2 border-white shadow-sm"></span>
            <span>Medium Risk</span>
          </li>
          <li className="flex items-center space-x-2">
            <span className="w-3 h-3 rounded-full bg-orange-500 border-2 border-white shadow-sm"></span>
            <span>High Risk</span>
          </li>
          <li className="flex items-center space-x-2">
            <span className="w-3 h-3 rounded-full bg-red-600 border-2 border-white shadow-sm"></span>
            <span>Critical Risk</span>
          </li>
        </ul>
      </div>

    </div>
  );
};
