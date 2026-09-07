import React from 'react';
import { ShieldAlert, Info } from 'lucide-react';

export const RecommendedAction = ({ riskLevel }) => {
  if (!riskLevel) return null;

  return (
    <div className={`${riskLevel.lightBgColor} rounded-xl border ${riskLevel.borderColor} p-5 mb-6 flex items-start space-x-3 transition-colors duration-300`}>
      <div className="mt-0.5">
        <ShieldAlert size={20} className={riskLevel.color} />
      </div>
      <div>
        <h3 className={`font-semibold text-sm mb-1 ${riskLevel.color}`}>Recommended Action</h3>
        <p className={`text-sm text-slate-700`}>
          {riskLevel.action}
        </p>
      </div>
    </div>
  );
};
