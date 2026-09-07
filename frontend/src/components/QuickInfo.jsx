import React from 'react';
import { Lightbulb } from 'lucide-react';

export const QuickInfo = () => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-5 flex items-start space-x-4">
      <div className="bg-blue-50 p-2.5 rounded-lg shrink-0 mt-1">
        <Lightbulb size={24} className="text-blue-600" />
      </div>
      <div>
        <h3 className="font-semibold text-slate-800 mb-1">Quick Info</h3>
        <p className="text-sm text-slate-600 leading-relaxed">
          Click on any location on the map or select from the dropdown to check its risk level and detailed environmental factors.
        </p>
      </div>
    </div>
  );
};
