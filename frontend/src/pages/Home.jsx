import React, { useState, useEffect } from 'react';
import { LocationSelector } from '../components/LocationSelector';
import { RiskMap } from '../components/RiskMap';
import { RiskAssessment } from '../components/RiskAssessment';
import { RecommendedAction } from '../components/RecommendedAction';
import { RiskFactors } from '../components/RiskFactors';
import { QuickInfo } from '../components/QuickInfo';
import { AboutCard } from '../components/AboutCard';
import { getLocationRisk } from '../data/locations';
import { getRiskClassification } from '../utils/riskUtils';

export const Home = () => {
  const [selectedLocation, setSelectedLocation] = useState(null);
  const [riskLevel, setRiskLevel] = useState(null);

  const handleLocationChange = async (locationId) => {
    const location = await getLocationRisk(locationId);
    if (location) {
      setSelectedLocation(location);
      setRiskLevel(getRiskClassification(location.riskScore));
    }
  };

  // Initial load
  useEffect(() => {
    handleLocationChange('loc-1'); // Default to Shillong
  }, []);

  return (
    <div className="max-w-7xl mx-auto space-y-6">
      
      <div className="mb-8">
        <h1 className="text-2xl md:text-3xl font-bold text-slate-800 mb-2">Welcome to NER-SHIELD</h1>
        <p className="text-slate-600 max-w-3xl leading-relaxed">
          Select a location in the Northeast region to check the landslide risk and get insights based on environmental and historical data.
        </p>
      </div>

      <LocationSelector onAnalyze={handleLocationChange} currentLocation={selectedLocation} />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Column - Map */}
        <div className="lg:col-span-2 flex flex-col h-full">
          <RiskMap 
            selectedLocationId={selectedLocation?.id} 
            onMarkerClick={handleLocationChange} 
          />
          <div className="hidden lg:block mt-auto">
             <AboutCard />
          </div>
        </div>

        {/* Right Column - Assessment */}
        <div className="lg:col-span-1">
          {selectedLocation ? (
            <>
              <RiskAssessment location={selectedLocation} riskLevel={riskLevel} />
              <RecommendedAction riskLevel={riskLevel} />
              <RiskFactors location={selectedLocation} />
              <QuickInfo />
            </>
          ) : (
            <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-8 text-center h-full flex flex-col items-center justify-center">
              <div className="animate-pulse bg-slate-100 w-16 h-16 rounded-full mb-4"></div>
              <p className="text-slate-500 font-medium">Select a location to view risk assessment.</p>
            </div>
          )}
        </div>
        
        {/* Mobile About Card */}
        <div className="lg:hidden">
          <AboutCard />
        </div>
      </div>
      
    </div>
  );
};
