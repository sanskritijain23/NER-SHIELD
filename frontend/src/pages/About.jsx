import React from 'react';
import { Mountain, ShieldCheck, Activity, Users } from 'lucide-react';

export const About = () => {
  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-12">
      <div className="text-center mb-12">
        <div className="bg-emerald-100 text-emerald-800 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm">
          <Mountain size={32} />
        </div>
        <h1 className="text-3xl md:text-4xl font-bold text-slate-800 mb-4">About NER-SHIELD</h1>
        <p className="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">
          NER-SHIELD is a prototype landslide risk early-warning platform designed to combine environmental and historical information to help identify potentially high-risk areas in Northeast India.
        </p>
      </div>

      <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div className="bg-slate-900 p-8 text-white">
          <h2 className="text-xl font-bold mb-2">Prototype Disclaimer</h2>
          <p className="text-slate-300 leading-relaxed text-sm">
            Please note that the current version is a PROTOTYPE. It uses local, simulated data for demonstration purposes. It is not currently connected to live government APIs, physical sensors, or real-time ML prediction models. This dashboard is intended to demonstrate the user interface and functionality of a future complete system.
          </p>
        </div>
        
        <div className="p-8">
          <h3 className="text-lg font-bold text-slate-800 mb-6 border-b border-slate-100 pb-2">Core Pillars</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div>
              <div className="bg-blue-50 text-blue-600 w-12 h-12 rounded-xl flex items-center justify-center mb-4">
                <Activity size={24} />
              </div>
              <h4 className="font-bold text-slate-800 mb-2">Data Monitoring</h4>
              <p className="text-sm text-slate-600 leading-relaxed">
                Aggregates environmental factors such as rainfall intensity, terrain slope, and historical landslide incidents.
              </p>
            </div>
            
            <div>
              <div className="bg-emerald-50 text-emerald-600 w-12 h-12 rounded-xl flex items-center justify-center mb-4">
                <ShieldCheck size={24} />
              </div>
              <h4 className="font-bold text-slate-800 mb-2">Risk Assessment</h4>
              <p className="text-sm text-slate-600 leading-relaxed">
                Calculates risk scores and visualizes threat levels across a map to identify critical zones requiring attention.
              </p>
            </div>
            
            <div>
              <div className="bg-amber-50 text-amber-600 w-12 h-12 rounded-xl flex items-center justify-center mb-4">
                <Users size={24} />
              </div>
              <h4 className="font-bold text-slate-800 mb-2">Community Action</h4>
              <p className="text-sm text-slate-600 leading-relaxed">
                Provides actionable recommendations based on risk tiers to facilitate rapid response and field inspections.
              </p>
            </div>
          </div>
        </div>
      </div>
      
      <div className="text-center text-slate-500 text-sm mt-8">
        <p>Built for the Northeast India region.</p>
        <p className="mt-2 font-semibold">Prevention • Preparedness • Safety</p>
      </div>
    </div>
  );
};
