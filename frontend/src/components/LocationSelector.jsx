import React, { useState, useMemo } from 'react';
import { MapPin, Search, Loader2 } from 'lucide-react';
import { locations } from '../data/locations';

export const LocationSelector = ({ onAnalyze, currentLocation }) => {
  const [selectedState, setSelectedState] = useState('Meghalaya');
  const [selectedLocation, setSelectedLocation] = useState('loc-1');
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const availableStates = useMemo(() => {
    return [...new Set(locations.map(loc => loc.state))].sort();
  }, []);

  const availableLocations = useMemo(() => {
    if (!selectedState) return [];
    return locations
      .filter(loc => loc.state === selectedState)
      .sort((a, b) => a.name.localeCompare(b.name));
  }, [selectedState]);

  // Sync with external selection (e.g. map clicks) during render
  const [prevCurrentLocation, setPrevCurrentLocation] = useState(currentLocation);
  if (currentLocation && currentLocation !== prevCurrentLocation) {
    setPrevCurrentLocation(currentLocation);
    setSelectedState(currentLocation.state);
    setSelectedLocation(currentLocation.id);
  }

  const handleStateChange = (newState) => {
    setSelectedState(newState);
    const locs = locations
      .filter(loc => loc.state === newState)
      .sort((a, b) => a.name.localeCompare(b.name));
    if (locs.length > 0) {
      setSelectedLocation(locs[0].id);
    } else {
      setSelectedLocation('');
    }
  };

  const handleAnalyzeClick = () => {
    if (!selectedLocation) return;
    
    setIsAnalyzing(true);
    
    // Simulate loading/analysis delay
    setTimeout(() => {
      onAnalyze(selectedLocation);
      setIsAnalyzing(false);
    }, 800);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-6">
      <div className="flex items-center space-x-2 mb-4">
        <MapPin size={20} className="text-emerald-600" />
        <h2 className="font-semibold text-slate-800 text-lg">Select Location</h2>
      </div>
      
      <div className="flex flex-col md:flex-row md:items-end gap-4">
        <div className="flex-1">
          <label className="block text-sm font-medium text-slate-600 mb-1.5">State</label>
          <div className="relative">
            <select
              value={selectedState}
              onChange={(e) => handleStateChange(e.target.value)}
              className="block w-full bg-slate-50 border border-slate-200 text-slate-800 rounded-lg py-2.5 pl-3 pr-8 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 appearance-none"
            >
              <option value="">Select State</option>
              {availableStates.map(state => (
                <option key={state} value={state}>{state}</option>
              ))}
            </select>
            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-slate-500">
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
            </div>
          </div>
        </div>

        <div className="flex-1">
          <label className="block text-sm font-medium text-slate-600 mb-1.5">Location</label>
          <div className="relative">
            <select
              value={selectedLocation}
              onChange={(e) => setSelectedLocation(e.target.value)}
              disabled={!selectedState}
              className="block w-full bg-slate-50 border border-slate-200 text-slate-800 rounded-lg py-2.5 pl-3 pr-8 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 appearance-none disabled:opacity-50 disabled:bg-slate-100"
            >
              <option value="">Select Location</option>
              {availableLocations.map(loc => (
                <option key={loc.id} value={loc.id}>{loc.name}</option>
              ))}
            </select>
            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-slate-500">
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7"></path></svg>
            </div>
          </div>
        </div>

        <button
          onClick={handleAnalyzeClick}
          disabled={!selectedLocation || isAnalyzing}
          className="w-full md:w-auto mt-4 md:mt-0 bg-emerald-700 hover:bg-emerald-800 text-white font-medium py-2.5 px-6 rounded-lg shadow-sm transition-colors duration-200 flex items-center justify-center min-w-[140px] disabled:opacity-70 disabled:cursor-not-allowed"
        >
          {isAnalyzing ? (
            <>
              <Loader2 size={18} className="mr-2 animate-spin" />
              Analyzing...
            </>
          ) : (
            <>
              <Search size={18} className="mr-2" />
              Analyze Risk
            </>
          )}
        </button>
      </div>
    </div>
  );
};
