import { useState } from "react";

export default function MatchupPage() {
  const [fighterA, setFighterA] = useState("");
  const [fighterB, setFighterB] = useState("");
  const [result, setResult] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Use env var if provided, otherwise fall back to localhost:8000
  const API_BASE = (process.env.NEXT_PUBLIC_API_URL as string) || "http://localhost:8000";

  async function runSimulation() {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await fetch(`${API_BASE}/api/run_simulation`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          fighterA,
          fighterB,
          simulations: 5000,
        }),
      });

      if (!res.ok) {
        const errBody = await res.json().catch(() => null);
        throw new Error(errBody?.detail || res.statusText || "Request failed");
      }

      const data = await res.json();
      setResult(data);
    } catch (err: any) {
      setError(err.message || "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>MMA Money Matrix — Matchup Simulator</h1>

      <input
        placeholder="Fighter A"
        value={fighterA}
        onChange={(e) => setFighterA(e.target.value)}
        style={{ marginRight: 8 }}
      />

      <input
        placeholder="Fighter B"
        value={fighterB}
        onChange={(e) => setFighterB(e.target.value)}
      />

      <div style={{ marginTop: 12 }}>
        <button onClick={runSimulation} disabled={loading || !fighterA || !fighterB}>
          {loading ? "Running…" : "Run Simulation"}
        </button>
      </div>

      {error && <div style={{ color: "red", marginTop: 12 }}>{error}</div>}

      {result && (
        <pre style={{ marginTop: 20 }}>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}
