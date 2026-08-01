# MMAMoneyMatrix
An advanced UFC fight simulator powered by real statistical ingestion, style interaction modeling, Monte Carlo simulation, round-by-round scoring, judge bias matrices, gym tier bonuses, underdog realism, and AI interpretation.

This project aims to be the most complete public MMA prediction engine ever built.

---

## 🔥 Features

### **1. Fighter Data Ingestion System**
- Pulls structured data from UFC Stats, UFC.com profiles, and UFC Record Book.
- Supports AI-assisted extraction for unstructured pages.
- Normalizes height, reach, accuracy, defense, control time, and more.
- Computes derived metrics:
  - Strike differential  
  - Grappling differential  
  - Power index  
  - Cardio index  
  - Momentum index  
  - Damage tolerance index  
- Supports manual overrides for weight class changes, gym moves, regional fights.

---

## 🧩 **2. Relational Database (Postgres/Supabase)**

### **fighters table**
Stores:
- Bio  
- Career stats  
- Striking metrics  
- Grappling metrics  
- Style tags  
- Gym tier  
- Underdog level  
- Derived metrics  

### **fights table**
Stores:
- Opponent  
- Result/method  
- Round/time  
- Fight stats  
- Damage indices  
- Pace/dominance ratings  
- Context (short notice, altitude, injury notes)

### **styles table**
Stores style definitions + impact vectors.

---

## 🧠 **3. Matchup Logic Engine**
Creates a “Fight Geometry Object” describing:
- Range control  
- Pace control  
- Grappling advantage  
- Striking advantage  
- Chaos factor  
- Cardio advantage  
- Early/late round advantage  
- Finish threat  
- Vulnerability  
- Gym tier modifier  
- Context modifier  

This object feeds directly into the Monte Carlo engine.

---

## 🎲 **4. Monte Carlo Simulation Engine**
Simulates thousands of fights using:
- Adjusted stats  
- Style interactions  
- Probability curves  
- Damage models  
- Control models  
- Grappling threat models  
- Pace & pressure models  
- Finish probability engine  

Outputs:
- Win probability  
- Method probability (KO/SUB/DEC)  
- Round probability  
- Confidence intervals  
- Decision breakdowns  

---

## 🧨 **5. Scoring & Judging Model**
Models real UFC judging:
- 10–9, 10–8, 10–7 scoring  
- Judge bias matrices (striking-heavy, grappling-heavy, control-heavy)  
- Unanimous, split, majority decisions  
- Draws  
- Round-by-round aggregation  

---

## 🏆 **6. Bonus Layer**
### **Gym Tier Bonus**
- Tier S: +4–7%  
- Tier A: +2–3%  
- Tier B: −1–3%

### **Underdog Bonus**
- Mild: +3%  
- Medium: +5%  
- Strong: +6%  
- Heavy: +7%

Applied after simulation, before normalization.

---

## 🤖 **7. AI Interpretation Layer**
Generates:
- Matchup summary  
- Probability drivers  
- Style interactions  
- Scenario analysis  
- Betting edge (optional)  

---

## 💻 **8. Frontend (Next.js)**
Pages:
- Fighter import  
- Fighter profile  
- Matchup runner  
- Matchup results  
- Method breakdown  
- Confidence ranges  
- Scenario analysis  

Components:
- FighterImport  
- FighterCard  
- FighterProfile  
- MatchupRunner  
- MatchupResult  
- MethodBreakdown  
- ConfidenceRanges  
- ScenarioPanel  
- ProbabilityChart  
- LoadingSimulation  

---

## 🔧 **9. Backend API (Flask or Node)**

Endpoints:
- `POST /api/import-fighter`
- `GET /api/get-fighter`
- `GET /api/get-history`
- `POST /api/run-simulation`
- `POST /api/matchup/scenario`

---

## 🚀 **10. Getting Started**

### **Clone the repo**
```bash
git clone https://github.com/mmamoneymatrix/MMAMoneyMatrix.git
cd MMAMoneyMatrix
## Backend Setup (Flask Example)

### 1. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
http://localhost:5000
backend/
    app.py
    engines/
        matchup_engine.py
        monte_carlo.py
        scoring.py
        bonuses.py
    models/
        fighter.py
        fight.py
    routes/
        import_fighter.py
        run_simulation.py
        get_fighter.py
        get_history.py
    requirements.txt
Flask
Flask-Cors
requests
numpy
pandas
scipy
supabase
