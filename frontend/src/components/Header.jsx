import React, { useState, useEffect } from 'react';
import { Mountain, Clock, Calendar } from 'lucide-react';

export const Header = () => {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  const formatDate = (date) => {
    return date.toLocaleDateString('en-GB', {
      weekday: 'short',
      day: 'numeric',
      month: 'short',
      year: 'numeric',
    });
  };

  const formatTime = (date) => {
    return date.toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true,
    });
  };

  return (
    <header className="bg-slate-900 text-white w-full h-16 flex items-center justify-between px-6 shadow-md fixed top-0 z-50">
      <div className="flex items-center space-x-3">
        <div className="bg-white text-slate-900 p-1.5 rounded-lg flex items-center justify-center">
          <Mountain size={28} className="text-slate-900" />
        </div>
        <div className="flex flex-col">
          <h1 className="text-lg font-bold leading-tight tracking-wide">NER-SHIELD</h1>
          <p className="text-xs text-slate-300">Landslide Risk Early Warning System</p>
        </div>
      </div>
      
      <div className="hidden md:flex items-center space-x-6">
        <div className="flex items-center space-x-4 text-sm text-slate-300 font-medium">
          <span>Safer Hills</span>
          <span className="w-px h-4 bg-slate-600"></span>
          <span>Stronger Communities</span>
          <span className="w-px h-4 bg-slate-600"></span>
          <span>A Resilient Northeast</span>
        </div>
        
        <div className="flex items-center space-x-4 text-sm bg-slate-800 px-4 py-2 rounded-lg border border-slate-700">
          <div className="flex items-center space-x-1.5 text-slate-200">
            <Calendar size={14} className="text-emerald-400" />
            <span>{formatDate(currentTime)}</span>
          </div>
          <div className="flex items-center space-x-1.5 text-slate-200 border-l border-slate-600 pl-4">
            <Clock size={14} className="text-emerald-400" />
            <span>{formatTime(currentTime)}</span>
          </div>
        </div>
      </div>
    </header>
  );
};
