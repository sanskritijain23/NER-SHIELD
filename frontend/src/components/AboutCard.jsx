import React from 'react';
import { ShieldCheck, Mountain } from 'lucide-react';

export const AboutCard = () => {
  return (
    <div className="bg-emerald-50 rounded-xl shadow-sm border border-emerald-100 p-6 flex flex-col md:flex-row items-center justify-between mt-6">
      <div className="flex items-start space-x-4 mb-4 md:mb-0 md:mr-6">
        <div className="bg-emerald-600 p-3 rounded-xl shrink-0 mt-1 shadow-sm">
          <ShieldCheck size={28} className="text-white" />
        </div>
        <div>
          <h3 className="font-bold text-slate-800 text-lg mb-1">About NER-SHIELD</h3>
          <p className="text-sm text-slate-700 leading-relaxed max-w-2xl">
            A simple and smart tool to assess landslide risk in the Northeast region using environmental data and historical records.
          </p>
        </div>
      </div>
      
      <div className="flex flex-col items-center justify-center shrink-0 border-t md:border-t-0 md:border-l border-emerald-200 pt-4 md:pt-0 md:pl-6 w-full md:w-auto">
        <Mountain size={36} className="text-emerald-700/60 mb-2" strokeWidth={1.5} />
        <div className="flex items-center space-x-2 text-[11px] font-semibold text-emerald-800 uppercase tracking-widest">
          <span>Prevention</span>
          <span className="w-1 h-1 rounded-full bg-emerald-400"></span>
          <span>Preparedness</span>
          <span className="w-1 h-1 rounded-full bg-emerald-400"></span>
          <span>Safety</span>
        </div>
      </div>
    </div>
  );
};
