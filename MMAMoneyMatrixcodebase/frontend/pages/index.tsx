import React from 'react';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <header className="max-w-6xl mx-auto text-center mb-16">
        <h1 className="text-6xl font-black text-red-600 mb-4">MMA MONEY MATRIX</h1>
        <p className="text-xl text-gray-400">The most advanced UFC fight simulator engine.</p>
      </header>

      <main className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        <Link href="/import" className="group p-8 border border-gray-800 rounded-xl hover:border-red-600 transition-all bg-gray-800/50">
          <h2 className="text-2xl font-bold mb-2 group-hover:text-red-500">Fighter Import →</h2>
          <p className="text-gray-400">Ingest real-time UFC stats and normalize fighter profiles.</p>
        </Link>

        <Link href="/matchup" className="group p-8 border border-gray-800 rounded-xl hover:border-red-600 transition-all bg-gray-800/50">
          <h2 className="text-2xl font-bold mb-2 group-hover:text-red-500">Matchup Runner →</h2>
          <p className="text-gray-400">Run Monte Carlo simulations with style and gym modifiers.</p>
        </Link>
      </main>

      <section className="max-w-6xl mx-auto mt-20">
        <h3 className="text-xl font-semibold mb-6 border-b border-gray-800 pb-2">Core Engines</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {['Monte Carlo', 'Scoring Model', 'Gym Tier Bonus', 'AI Interpretation'].map((engine) => (
            <div key={engine} className="p-4 bg-gray-800 rounded-lg text-center text-sm font-medium">
              {engine}
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
