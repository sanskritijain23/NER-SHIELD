import React from 'react';
import { Settings2, CloudRain, Mountain, AlertTriangle, CheckCircle } from 'lucide-react';

export const RiskFactors = ({ location }) => {
  if (!location) return null;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-6">
      <div className="flex items-center space-x-2 mb-4">
        <Settings2 size={20} className="text-slate-600" />
        <h2 className="font-semibold text-slate-800 text-lg">Key Risk Factors</h2>
      </div>
      
      <ul className="space-y-4">
        <li className="flex items-start space-x-3">
          {location.rainfall > 100 ? (
            <CloudRain size={18} className="text-blue-500 mt-0.5 shrink-0" />
          ) : (
            <CheckCircle size={18} className="text-green-500 mt-0.5 shrink-0" />
          )}
          <div>
            <p className="text-sm text-slate-700">
              {location.rainfall > 100 ? 'Heavy rainfall' : 'Normal rainfall'} ({location.rainfall} mm)
            </p>
          </div>
        </li>

        <li className="flex items-start space-x-3">
          {location.slope >= 30 ? (
            <Mountain size={18} className="text-red-500 mt-0.5 shrink-0" />
          ) : (
            <CheckCircle size={18} className="text-green-500 mt-0.5 shrink-0" />
          )}
          <div>
            <p className="text-sm text-slate-700">
              {location.slope >= 30 ? 'Steep slope' : 'Moderate slope'} ({location.slope}°)
            </p>
          </div>
        </li>

        <li className="flex items-start space-x-3">
          {location.previousLandslide ? (
            <AlertTriangle size={18} className="text-amber-500 mt-0.5 shrink-0" />
          ) : (
            <CheckCircle size={18} className="text-green-500 mt-0.5 shrink-0" />
          )}
          <div>
            <p className="text-sm text-slate-700">
              {location.previousLandslide ? 'Previous landslide recorded' : 'No previous landslides recorded'}
            </p>
          </div>
        </li>
      </ul>
    </div>
  );
};
