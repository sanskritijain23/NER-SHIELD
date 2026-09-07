import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Header } from './components/Header';
import { Sidebar } from './components/Sidebar';
import { Home } from './pages/Home';
import { RiskMapPage } from './pages/RiskMapPage';
import { Reports } from './pages/Reports';
import { About } from './pages/About';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <Router>
      <div className="flex flex-col min-h-screen bg-slate-50">
        <Header />
        
        <div className="flex flex-1 pt-16">
          <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSidebar} />
          
          <main className="flex-1 overflow-x-hidden p-4 md:p-8">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/map" element={<RiskMapPage />} />
              <Route path="/reports" element={<Reports />} />
              <Route path="/about" element={<About />} />
            </Routes>
          </main>
        </div>
        
        {/* Mobile menu toggle button */}
        <button 
          className="md:hidden fixed bottom-6 right-6 z-50 bg-emerald-600 text-white p-3 rounded-full shadow-lg"
          onClick={toggleSidebar}
        >
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d={isSidebarOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16M4 18h16"}></path>
          </svg>
        </button>
      </div>
    </Router>
  );
}

export default App;
