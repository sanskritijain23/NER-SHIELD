import React from 'react';
import { Home, Map as MapIcon, FileText, Info, MountainSnow } from 'lucide-react';
import { NavLink } from 'react-router-dom';

export const Sidebar = ({ isOpen, toggleSidebar }) => {
  const navItems = [
    { name: 'Home', path: '/', icon: Home },
    { name: 'Risk Map', path: '/map', icon: MapIcon },
    { name: 'Reports', path: '/reports', icon: FileText },
    { name: 'About', path: '/about', icon: Info },
  ];

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black/50 z-40 md:hidden"
          onClick={toggleSidebar}
        />
      )}
      
      <aside 
        className={`fixed md:sticky top-0 md:top-16 left-0 h-full md:h-[calc(100vh-4rem)] w-64 bg-slate-900 border-r border-slate-800 flex flex-col transition-transform duration-300 z-50 ${isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'}`}
      >
        {/* Mobile close btn space - handled by header typically, or added here if needed */}
        <div className="md:hidden h-16 bg-slate-900 border-b border-slate-800 flex items-center px-6">
          <span className="font-bold text-white tracking-wide">NER-SHIELD Menu</span>
        </div>
        
        <nav className="flex-1 py-8 px-4 space-y-2 overflow-y-auto">
          {navItems.map((item) => (
            <NavLink
              key={item.name}
              to={item.path}
              end={item.path === '/'}
              className={({ isActive }) =>
                `flex items-center space-x-3 px-4 py-3 rounded-xl transition-all duration-200 ${
                  isActive 
                    ? 'bg-emerald-700 text-white font-medium shadow-md' 
                    : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
                }`
              }
              onClick={() => isOpen && toggleSidebar()}
            >
              {({ isActive }) => (
                <>
                  <item.icon size={20} className={isActive ? 'text-white' : 'text-slate-400'} />
                  <span>{item.name}</span>
                </>
              )}
            </NavLink>
          ))}
        </nav>
        
        <div className="p-6 border-t border-slate-800 bg-slate-900 flex flex-col items-center text-center">
          <MountainSnow size={40} className="text-emerald-500 mb-3 opacity-80" />
          <p className="text-xs text-slate-400 font-medium tracking-wide">Monitoring today</p>
          <p className="text-xs text-slate-400 font-medium tracking-wide">for a safer tomorrow</p>
        </div>
      </aside>
    </>
  );
};
