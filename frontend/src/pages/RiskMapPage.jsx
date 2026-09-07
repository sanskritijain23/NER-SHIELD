import React, { useState } from 'react';
import { RiskMap } from '../components/RiskMap';
import { getLocationRisk } from '../data/locations';
import { getRiskClassification } from '../utils/riskUtils';
import { RiskAssessment } from '../components/RiskAssessment';

export const RiskMapPage = () => {
  const [selectedLocation, setSelectedLocation] = useState(null);
  const [riskLevel, setRiskLevel] = useState(null);

  const handleMarkerClick = async (locationId) => {
    const location = await getLocationRisk(locationId);
    if (location) {
      setSelectedLocation(location);
      setRiskLevel(getRiskClassification(location.riskScore));
    }
  };

  return (
    <div className="max-w-7xl mx-auto h-[calc(100vh-8rem)] flex flex-col">
      <div className="mb-4">
        <h1 className="text-2xl md:text-3xl font-bold text-slate-800 mb-2">Interactive Risk Map</h1>
        <p className="text-slate-600">Explore landslide risks across the Northeast region in full screen.</p>
      </div>
      
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-4 gap-6 min-h-0">
        <div className="lg:col-span-3 h-full pb-6">
           <RiskMap 
              selectedLocationId={selectedLocation?.id} 
              onMarkerClick={handleMarkerClick} 
            />
        </div>
        
        <div className="lg:col-span-1 h-full overflow-y-auto">
          {selectedLocation ? (
             <RiskAssessment location={selectedLocation} riskLevel={riskLevel} />
          ) : (
            <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-8 text-center h-48 flex flex-col items-center justify-center">
              <div className="animate-pulse bg-slate-100 w-12 h-12 rounded-full mb-3"></div>
              <p className="text-slate-500 font-medium text-sm">Click a marker on the map to view details.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
