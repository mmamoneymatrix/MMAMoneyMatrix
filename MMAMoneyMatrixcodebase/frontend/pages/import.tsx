import React, { useState } from 'react';

export default function ImportPage() {
  const [url, setUrl] = useState('');
  const [status, setStatus] = useState('idle');

  const handleImport = async (e) => {
    e.preventDefault();
    setStatus('loading');
    // Simulate API call
    setTimeout(() => setStatus('success'), 1500);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold mb-8">Fighter Data Ingestion</h1>
        
        <form onSubmit={handleImport} className="space-y-6">
          <div className="bg-gray-800 p-6 rounded-xl border border-gray-700">
            <label className="block text-sm font-medium text-gray-400 mb-2">UFC Stats URL</label>
            <input 
              type="text" 
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="http://ufcstats.com/fighter-details/..."
              className="w-full bg-gray-900 border border-gray-700 p-3 rounded-lg focus:ring-2 focus:ring-red-600 outline-none"
            />
          </div>

          <button 
            type="submit"
            className="w-full bg-white text-black font-bold py-4 rounded-lg hover:bg-gray-200 transition-colors"
          >
            {status === 'loading' ? 'INGESTING...' : 'START INGESTION'}
          </button>

          {status === 'success' && (
            <div className="p-4 bg-green-900/30 border border-green-500 text-green-500 rounded-lg text-center">
              Fighter data successfully ingested and normalized.
            </div>
          )}
        </form>

        <div className="mt-12">
          <h3 className="text-sm font-bold text-gray-500 uppercase tracking-widest mb-4">Supported Sources</h3>
          <div className="flex gap-4 opacity-50 grayscale">
            <span className="px-3 py-1 bg-gray-800 rounded">UFC Stats</span>
            <span className="px-3 py-1 bg-gray-800 rounded">UFC.com</span>
            <span className="px-3 py-1 bg-gray-800 rounded">AI Extraction</span>
          </div>
        </div>
      </div>
    </div>
  );
}
