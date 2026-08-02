import React from 'react';

const FighterCard = ({ fighter }) => {
  return (
    <div className="bg-gray-800 border border-gray-700 rounded-lg p-4 hover:border-red-500 transition-colors">
      <div className="flex justify-between items-start mb-4">
        <div>
          <h3 className="text-xl font-bold">{fighter.name}</h3>
          <p className="text-gray-400 text-xs uppercase tracking-widest">{fighter.nickname || 'The Prospect'}</p>
        </div>
        <div className="bg-red-600/20 text-red-500 text-xs font-bold px-2 py-1 rounded">
          TIER {fighter.gym_tier}
        </div>
      </div>
      
      <div className="grid grid-cols-2 gap-2 text-sm">
        <div className="flex justify-between border-b border-gray-700 pb-1">
          <span className="text-gray-500">Reach</span>
          <span>{fighter.reach}"</span>
        </div>
        <div className="flex justify-between border-b border-gray-700 pb-1">
          <span className="text-gray-500">SLpM</span>
          <span>{fighter.slpm}</span>
        </div>
        <div className="flex justify-between border-b border-gray-700 pb-1">
          <span className="text-gray-500">TD Def</span>
          <span>{fighter.td_def}%</span>
        </div>
        <div className="flex justify-between border-b border-gray-700 pb-1">
          <span className="text-gray-500">Accuracy</span>
          <span>{fighter.striking_accuracy}%</span>
        </div>
      </div>
    </div>
  );
};

export default FighterCard;
