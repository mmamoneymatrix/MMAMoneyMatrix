import React, { useState } from 'react';

const MatchupRunner = () => {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);

  const runSim = async () => {
    setLoading(true);
    // Simulate API call to Flask backend
    setTimeout(() => {
      setResults({
        win_probability: 0.65,
        method_probabilities: { "KO/TKO": 0.4, "Submission": 0.1, "Decision": 0.5 },
        round_probabilities: { 1: 0.2, 2: 0.3, 3: 0.5 }
      });
      setLoading(false);
    }, 2000);
  };

  return (
    <div className="space-y-8">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="p-6 bg-gray-800 rounded-xl border border-gray-700">
          <h3 className="text-lg font-bold mb-4">Fighter A</h3>
          <input className="w-full bg-gray-900 border border-gray-700 p-2 rounded mb-4" placeholder="Search fighter..." />
          <div className="text-sm text-gray-400">Stats: Reach: 72", SLpM: 4.5, TD Def: 80%</div>
        </div>
        <div className="p-6 bg-gray-800 rounded-xl border border-gray-700">
          <h3 className="text-lg font-bold mb-4">Fighter B</h3>
          <input className="w-full bg-gray-900 border border-gray-700 p-2 rounded mb-4" placeholder="Search fighter..." />
          <div className="text-sm text-gray-400">Stats: Reach: 70", SLpM: 3.8, TD Def: 75%</div>
        </div>
      </div>

      <div className="flex justify-center">
        <button 
          onClick={runSim}
          disabled={loading}
          className="bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-12 rounded-full transition-all disabled:opacity-50"
        >
          {loading ? "SIMULATING..." : "RUN MONTE CARLO"}
        </button>
      </div>

      {results && (
        <div className="mt-12 p-8 bg-gray-800 rounded-2xl border-2 border-red-600/30">
          <h2 className="text-2xl font-bold mb-6 text-center">Simulation Results</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="text-4xl font-black text-red-500">{(results.win_probability * 100).toFixed(1)}%</div>
              <div className="text-sm text-gray-400 mt-2">WIN PROBABILITY</div>
            </div>
            <div>
              <h4 className="text-sm font-bold mb-2">METHOD BREAKDOWN</h4>
              {Object.entries(results.method_probabilities).map(([method, prob]) => (
                <div key={method} className="flex justify-between text-sm mb-1">
                  <span>{method}</span>
                  <span className="font-mono">{(prob * 100).toFixed(0)}%</span>
                </div>
              ))}
            </div>
            <div>
              <h4 className="text-sm font-bold mb-2">ROUND PROBABILITY</h4>
              {Object.entries(results.round_probabilities).map(([rd, prob]) => (
                <div key={rd} className="flex justify-between text-sm mb-1">
                  <span>Round {rd}</span>
                  <span className="font-mono">{(prob * 100).toFixed(0)}%</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MatchupRunner;
