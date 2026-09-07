import React, { useState } from 'react';
import { FileText, Plus, Search, Filter } from 'lucide-react';

export const Reports = () => {
  const [showModal, setShowModal] = useState(false);

  const mockReports = [
    { id: 1, location: 'Shillong', type: 'Slope Crack', date: '09 Jun 2025', status: 'Under Review', statusColor: 'bg-amber-100 text-amber-700 border-amber-200' },
    { id: 2, location: 'Aizawl', type: 'Road Blockage', date: '09 Jun 2025', status: 'Verified', statusColor: 'bg-emerald-100 text-emerald-700 border-emerald-200' },
    { id: 3, location: 'Kohima', type: 'Soil Movement', date: '08 Jun 2025', status: 'Under Review', statusColor: 'bg-amber-100 text-amber-700 border-amber-200' },
    { id: 4, location: 'Cherrapunji', type: 'Minor Landslide', date: '07 Jun 2025', status: 'Resolved', statusColor: 'bg-slate-100 text-slate-700 border-slate-200' },
  ];

  return (
    <div className="max-w-7xl mx-auto">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between mb-8 gap-4">
        <div>
          <h1 className="text-2xl md:text-3xl font-bold text-slate-800 mb-2">Field Reports</h1>
          <p className="text-slate-600">View and manage incident reports submitted by field teams.</p>
        </div>
        <button 
          onClick={() => setShowModal(true)}
          className="bg-emerald-700 hover:bg-emerald-800 text-white font-medium py-2.5 px-5 rounded-lg shadow-sm transition-colors duration-200 flex items-center justify-center sm:w-auto w-full"
        >
          <Plus size={18} className="mr-2" />
          New Report
        </button>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden mb-8">
        <div className="p-5 border-b border-slate-200 bg-slate-50 flex flex-col sm:flex-row gap-4 items-center justify-between">
          <div className="relative w-full sm:w-96">
            <input 
              type="text" 
              placeholder="Search reports by location..." 
              className="w-full bg-white border border-slate-300 text-slate-800 rounded-lg py-2 pl-10 pr-4 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 shadow-sm"
            />
            <Search size={18} className="absolute left-3 top-2.5 text-slate-400" />
          </div>
          <button className="flex items-center space-x-2 text-slate-600 bg-white border border-slate-300 px-4 py-2 rounded-lg hover:bg-slate-50 transition w-full sm:w-auto justify-center">
            <Filter size={16} />
            <span>Filter</span>
          </button>
        </div>
        
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-slate-50 text-slate-500 text-sm border-b border-slate-200">
                <th className="font-semibold py-4 px-6">Location</th>
                <th className="font-semibold py-4 px-6">Report Type</th>
                <th className="font-semibold py-4 px-6">Date</th>
                <th className="font-semibold py-4 px-6">Status</th>
                <th className="font-semibold py-4 px-6 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {mockReports.map((report) => (
                <tr key={report.id} className="hover:bg-slate-50/50 transition-colors">
                  <td className="py-4 px-6 font-medium text-slate-800">{report.location}</td>
                  <td className="py-4 px-6 text-slate-600 flex items-center">
                    <FileText size={16} className="mr-2 text-slate-400" />
                    {report.type}
                  </td>
                  <td className="py-4 px-6 text-slate-600">{report.date}</td>
                  <td className="py-4 px-6">
                    <span className={`px-2.5 py-1 text-xs font-semibold rounded-full border ${report.statusColor}`}>
                      {report.status}
                    </span>
                  </td>
                  <td className="py-4 px-6 text-right">
                    <button className="text-emerald-600 hover:text-emerald-800 font-medium text-sm">View Details</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Simple Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center z-[100] p-4">
          <div className="bg-white rounded-xl shadow-xl border border-slate-200 w-full max-w-lg overflow-hidden flex flex-col max-h-[90vh]">
            <div className="p-5 border-b border-slate-100 flex justify-between items-center bg-slate-50">
              <h2 className="font-bold text-slate-800 text-lg">Submit New Report</h2>
              <button onClick={() => setShowModal(false)} className="text-slate-400 hover:text-slate-600">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>
            
            <div className="p-6 space-y-4 overflow-y-auto">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Location</label>
                <select className="w-full border border-slate-300 rounded-lg py-2 px-3 focus:outline-none focus:ring-2 focus:ring-emerald-500/50">
                  <option>Select Location</option>
                  <option>Shillong</option>
                  <option>Aizawl</option>
                  <option>Kohima</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Report Type</label>
                <select className="w-full border border-slate-300 rounded-lg py-2 px-3 focus:outline-none focus:ring-2 focus:ring-emerald-500/50">
                  <option>Select Type</option>
                  <option>Slope Crack</option>
                  <option>Soil Movement</option>
                  <option>Road Blockage</option>
                  <option>Minor Landslide</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Description</label>
                <textarea rows="4" className="w-full border border-slate-300 rounded-lg py-2 px-3 focus:outline-none focus:ring-2 focus:ring-emerald-500/50" placeholder="Provide details..."></textarea>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Upload Photo</label>
                <div className="border-2 border-dashed border-slate-300 rounded-lg p-8 text-center text-slate-500 hover:bg-slate-50 hover:border-emerald-400 cursor-pointer transition">
                  <Plus size={24} className="mx-auto mb-2 text-slate-400" />
                  <p className="text-sm">Click to upload or drag and drop</p>
                </div>
              </div>
            </div>
            
            <div className="p-5 border-t border-slate-100 bg-slate-50 flex justify-end space-x-3">
              <button 
                onClick={() => setShowModal(false)}
                className="px-4 py-2 text-slate-600 font-medium hover:bg-slate-200 rounded-lg transition"
              >
                Cancel
              </button>
              <button 
                onClick={() => setShowModal(false)}
                className="px-4 py-2 bg-emerald-700 text-white font-medium hover:bg-emerald-800 rounded-lg shadow-sm transition"
              >
                Submit Report
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
