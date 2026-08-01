import React, { useState } from 'react';
import MatchupRunner from '../components/MatchupRunner';

export default function MatchupPage() {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <div className="max-w-6xl mx-auto">
        <header className="mb-8">
          <h1 className="text-3xl font-bold">Matchup Runner</h1>
          <p className="text-gray-400">Select fighters and configure simulation parameters.</p>
        </header>
        
        <MatchupRunner />
      </div>
    </div>
  );
}
