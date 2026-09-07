import React, { useState } from 'react';
import { FileText, Plus, Search, CheckCircle } from 'lucide-react';
import { locations } from '../data/locations';

export const Reports = () => {
  const [showModal, setShowModal] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState('All');
  const [selectedDetail, setSelectedDetail] = useState(null);

  const [reports, setReports] = useState([
    { id: 1, location: 'Shillong', type: 'Slope Crack', date: '09 Jun 2025', status: 'Under Review', description: 'Noticeable fissures on the upper slope embankment near highway junction.', statusColor: 'bg-amber-100 text-amber-700 border-amber-200' },
    { id: 2, location: 'Aizawl', type: 'Road Blockage', date: '09 Jun 2025', status: 'Verified', description: 'Rock debris blocking the secondary bypass road. Clearance underway.', statusColor: 'bg-emerald-100 text-emerald-700 border-emerald-200' },
    { id: 3, location: 'Kohima', type: 'Soil Movement', date: '08 Jun 2025', status: 'Under Review', description: 'Gradual downward soil creep observed around residential perimeter.', statusColor: 'bg-amber-100 text-amber-700 border-amber-200' },
    { id: 4, location: 'Cherrapunji', type: 'Minor Landslide', date: '07 Jun 2025', status: 'Resolved', description: 'Small mud slide following continuous downpour. Secured with mesh.', statusColor: 'bg-slate-100 text-slate-700 border-slate-200' },
  ]);

  // Form state
  const [formLocation, setFormLocation] = useState('');
  const [formType, setFormType] = useState('Slope Crack');
  const [formDescription, setFormDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formLocation) return;

    const newReport = {
      id: Date.now(),
      location: formLocation,
      type: formType,
      date: new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }),
      status: 'Under Review',
      description: formDescription || 'Field incident report submitted for inspection.',
      statusColor: 'bg-amber-100 text-amber-700 border-amber-200'
    };

    setReports([newReport, ...reports]);
    setFormLocation('');
    setFormDescription('');
    setShowModal(false);
  };

  const filteredReports = reports.filter(report => {
    const matchesSearch = report.location.toLowerCase().includes(searchQuery.toLowerCase()) ||
                          report.type.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesFilter = statusFilter === 'All' || report.status === statusFilter;
    return matchesSearch && matchesFilter;
  });

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
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search reports by location or type..." 
              className="w-full bg-white border border-slate-300 text-slate-800 rounded-lg py-2 pl-10 pr-4 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 shadow-sm"
            />
            <Search size={18} className="absolute left-3 top-2.5 text-slate-400" />
          </div>
          <div className="flex items-center space-x-2 w-full sm:w-auto">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Status:</span>
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className="bg-white border border-slate-300 text-slate-700 text-sm rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-emerald-500/50"
            >
              <option value="All">All Statuses</option>
              <option value="Under Review">Under Review</option>
              <option value="Verified">Verified</option>
              <option value="Resolved">Resolved</option>
            </select>
          </div>
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
              {filteredReports.length === 0 ? (
                <tr>
                  <td colSpan="5" className="py-8 text-center text-slate-500">
                    No reports match your search criteria.
                  </td>
                </tr>
              ) : (
                filteredReports.map((report) => (
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
                      <button 
                        onClick={() => setSelectedDetail(report)}
                        className="text-emerald-600 hover:text-emerald-800 font-medium text-sm transition"
                      >
                        View Details
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Detail Modal */}
      {selectedDetail && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center z-[100] p-4">
          <div className="bg-white rounded-xl shadow-xl border border-slate-200 w-full max-w-md overflow-hidden flex flex-col">
            <div className="p-5 border-b border-slate-100 flex justify-between items-center bg-slate-50">
              <h2 className="font-bold text-slate-800 text-lg">Report Details</h2>
              <button onClick={() => setSelectedDetail(null)} className="text-slate-400 hover:text-slate-600">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>
            <div className="p-6 space-y-4 text-sm">
              <div className="flex justify-between">
                <span className="text-slate-500 font-medium">Location:</span>
                <span className="font-semibold text-slate-800">{selectedDetail.location}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500 font-medium">Report Type:</span>
                <span className="font-semibold text-slate-800">{selectedDetail.type}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500 font-medium">Date Logged:</span>
                <span className="text-slate-700">{selectedDetail.date}</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-slate-500 font-medium">Status:</span>
                <span className={`px-2.5 py-0.5 text-xs font-semibold rounded-full border ${selectedDetail.statusColor}`}>
                  {selectedDetail.status}
                </span>
              </div>
              <div className="pt-2 border-t border-slate-100">
                <span className="text-slate-500 font-medium block mb-1">Notes:</span>
                <p className="text-slate-700 bg-slate-50 p-3 rounded-lg leading-relaxed">{selectedDetail.description}</p>
              </div>
            </div>
            <div className="p-4 border-t border-slate-100 bg-slate-50 flex justify-end">
              <button 
                onClick={() => setSelectedDetail(null)}
                className="px-4 py-2 bg-slate-800 text-white font-medium hover:bg-slate-700 rounded-lg text-sm transition"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      {/* New Report Modal */}
      {showModal && (
        <div className="fixed inset-0 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center z-[100] p-4">
          <div className="bg-white rounded-xl shadow-xl border border-slate-200 w-full max-w-lg overflow-hidden flex flex-col max-h-[90vh]">
            <div className="p-5 border-b border-slate-100 flex justify-between items-center bg-slate-50">
              <h2 className="font-bold text-slate-800 text-lg">Submit New Report</h2>
              <button onClick={() => setShowModal(false)} className="text-slate-400 hover:text-slate-600">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path></svg>
              </button>
            </div>
            
            <form onSubmit={handleSubmit} className="p-6 space-y-4 overflow-y-auto">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Location</label>
                <select 
                  value={formLocation} 
                  onChange={(e) => setFormLocation(e.target.value)}
                  required
                  className="w-full border border-slate-300 rounded-lg py-2 px-3 focus:outline-none focus:ring-2 focus:ring-emerald-500/50"
                >
                  <option value="">Select Location</option>
                  {locations.map((loc) => (
                    <option key={loc.id} value={loc.name}>{loc.name} ({loc.state})</option>
                  ))}
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Report Type</label>
                <select 
                  value={formType}
                  onChange={(e) => setFormType(e.target.value)}
                  className="w-full border border-slate-300 rounded-lg py-2 px-3 focus:outline-none focus:ring-2 focus:ring-emerald-500/50"
                >
                  <option>Slope Crack</option>
                  <option>Soil Movement</option>
                  <option>Road Blockage</option>
                  <option>Minor Landslide</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Description</label>
                <textarea 
                  rows="4" 
                  value={formDescription}
                  onChange={(e) => setFormDescription(e.target.value)}
                  className="w-full border border-slate-300 rounded-lg py-2 px-3 focus:outline-none focus:ring-2 focus:ring-emerald-500/50" 
                  placeholder="Provide incident observations or details..."
                ></textarea>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">Upload Photo</label>
                <div className="border-2 border-dashed border-slate-300 rounded-lg p-6 text-center text-slate-500 hover:bg-slate-50 hover:border-emerald-400 cursor-pointer transition">
                  <CheckCircle size={24} className="mx-auto mb-2 text-slate-400" />
                  <p className="text-sm">Optional: Attach site survey photo</p>
                </div>
              </div>

              <div className="pt-4 border-t border-slate-100 flex justify-end space-x-3">
                <button 
                  type="button"
                  onClick={() => setShowModal(false)} 
                  className="px-4 py-2 text-slate-600 font-medium hover:bg-slate-200 rounded-lg transition"
                >
                  Cancel
                </button>
                <button 
                  type="submit" 
                  disabled={!formLocation}
                  className="px-4 py-2 bg-emerald-700 text-white font-medium hover:bg-emerald-800 rounded-lg shadow-sm transition disabled:opacity-50"
                >
                  Submit Report
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
