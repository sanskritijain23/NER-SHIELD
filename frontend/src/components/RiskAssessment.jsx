import React from 'react';
import { CloudRain, Mountain, AlertTriangle, AlertCircle } from 'lucide-react';

export const RiskAssessment = ({ location, riskLevel }) => {
  if (!location || !riskLevel) return null;

  // Calculate gauge dasharray (circumference of circle)
  const radius = 46;
  const circumference = 2 * Math.PI * radius;
  const strokeDasharray = `${(location.riskScore / 100) * circumference} ${circumference}`;

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6 relative overflow-hidden">
      <div className="flex items-center space-x-2 mb-6">
        <AlertCircle size={20} className={riskLevel.color} />
        <h2 className="font-bold text-slate-800 text-lg">Risk Assessment ({location.name})</h2>
      </div>

      <div className="flex flex-col md:flex-row items-center justify-between">
        
        {/* Gauge Chart Area */}
        <div className="relative flex flex-col items-center justify-center mb-6 md:mb-0">
          <div className="relative w-40 h-40">
            <svg className="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
              <circle
                cx="50"
                cy="50"
                r="46"
                fill="transparent"
                stroke="#f1f5f9"
                strokeWidth="8"
              />
              <circle
                cx="50"
                cy="50"
                r="46"
                fill="transparent"
                stroke="currentColor"
                strokeWidth="8"
                strokeDasharray={strokeDasharray}
                className={`${riskLevel.color} transition-all duration-1000 ease-out`}
                strokeLinecap="round"
              />
            </svg>
            <div className="absolute inset-0 flex flex-col items-center justify-center">
              <div className="flex items-baseline">
                <span className="text-4xl font-bold text-slate-800 tracking-tighter">{location.riskScore}</span>
                <span className="text-lg font-medium text-slate-400 ml-1">/100</span>
              </div>
            </div>
          </div>
          <div className={`mt-3 px-4 py-1.5 rounded-full text-xs font-bold tracking-wider uppercase ${riskLevel.bgColor} text-white shadow-sm`}>
            {riskLevel.level} RISK
          </div>
        </div>

        {/* Factors List */}
        <div className="flex flex-col space-y-5 md:ml-8 w-full md:w-auto">
          <div className="flex items-start space-x-3">
            <div className="bg-blue-50 p-2 rounded-lg mt-0.5">
              <CloudRain size={18} className="text-blue-500" />
            </div>
            <div>
              <p className="text-xs text-slate-500 font-medium">Rainfall</p>
              <p className="text-sm font-semibold text-slate-800">{location.rainfall} mm</p>
            </div>
          </div>
          
          <div className="flex items-start space-x-3">
            <div className="bg-amber-50 p-2 rounded-lg mt-0.5">
              <Mountain size={18} className="text-amber-600" />
            </div>
            <div>
              <p className="text-xs text-slate-500 font-medium">Slope</p>
              <p className="text-sm font-semibold text-slate-800">{location.slope}°</p>
            </div>
          </div>
          
          <div className="flex items-start space-x-3">
            <div className="bg-slate-100 p-2 rounded-lg mt-0.5">
              <AlertTriangle size={18} className="text-slate-600" />
            </div>
            <div>
              <p className="text-xs text-slate-500 font-medium">Previous Landslide</p>
              <p className="text-sm font-semibold text-slate-800">{location.previousLandslide ? 'Yes' : 'No'}</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};
