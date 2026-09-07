import React, { useState, useEffect } from 'react';
import { MapPin, Search, Loader2 } from 'lucide-react';
import { locations } from '../data/locations';

export const LocationSelector = ({ onAnalyze, currentLocation }) => {
  const [selectedState, setSelectedState] = useState('');
  const [selectedDistrict, setSelectedDistrict] = useState('');
  const [selectedLocation, setSelectedLocation] = useState('');
  
  const [availableStates, setAvailableStates] = useState([]);
  const [availableDistricts, setAvailableDistricts] = useState([]);
  const [availableLocations, setAvailableLocations] = useState([]);
  
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  // Initial load
  useEffect(() => {
    const states = [...new Set(locations.map(loc => loc.state))].sort();
    setAvailableStates(states);
    
    // Default values matching prototype
    const defaultState = 'Meghalaya';
    setSelectedState(defaultState);
  }, []);

  // Sync with external selection (e.g. map clicks)
  useEffect(() => {
    if (currentLocation) {
      setSelectedState(currentLocation.state);
      setSelectedDistrict(currentLocation.district);
      setSelectedLocation(currentLocation.id);
    }
  }, [currentLocation]);

  // When State changes
  useEffect(() => {
    if (selectedState) {
      const districts = [...new Set(locations.filter(loc => loc.state === selectedState).map(loc => loc.district))].sort();
      setAvailableDistricts(districts);
      
      // Auto-select first district or default, only if current isn't valid
      if (!districts.includes(selectedDistrict)) {
        if (selectedState === 'Meghalaya') {
          setSelectedDistrict('East Khasi Hills');
        } else if (districts.length > 0) {
          setSelectedDistrict(districts[0]);
        } else {
          setSelectedDistrict('');
        }
      }
    } else {
      setAvailableDistricts([]);
      setSelectedDistrict('');
    }
  }, [selectedState]);

  // When District changes
  useEffect(() => {
    if (selectedDistrict) {
      const locs = locations.filter(loc => loc.district === selectedDistrict).sort((a, b) => a.name.localeCompare(b.name));
      setAvailableLocations(locs);
      
      // Auto-select first location or default, only if current isn't valid
      if (!locs.find(l => l.id === selectedLocation)) {
        if (selectedDistrict === 'East Khasi Hills') {
          setSelectedLocation('loc-1'); // Shillong ID
        } else if (locs.length > 0) {
          setSelectedLocation(locs[0].id);
        } else {
          setSelectedLocation('');
        }
      }
    } else {
      setAvailableLocations([]);
      setSelectedLocation('');
    }
  }, [selectedDistrict]);

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
              onChange={(e) => setSelectedState(e.target.value)}
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
          <label className="block text-sm font-medium text-slate-600 mb-1.5">District</label>
          <div className="relative">
            <select
              value={selectedDistrict}
              onChange={(e) => setSelectedDistrict(e.target.value)}
              disabled={!selectedState}
              className="block w-full bg-slate-50 border border-slate-200 text-slate-800 rounded-lg py-2.5 pl-3 pr-8 shadow-sm focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 appearance-none disabled:opacity-50 disabled:bg-slate-100"
            >
              <option value="">Select District</option>
              {availableDistricts.map(district => (
                <option key={district} value={district}>{district}</option>
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
              disabled={!selectedDistrict}
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
