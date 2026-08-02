# MMAMoneyMatrix Architecture

## 🧠 System Overview
MMAMoneyMatrix is a high-fidelity MMA fight simulator that combines statistical ingestion, style-based interaction modeling, and Monte Carlo simulations to predict fight outcomes with PS5-quality visual feedback.

## 🏗️ Core Modules

### 1. Matchup Logic Engine (`backend/engines/matchup_engine.py`)
- **Fight Geometry Object**: Calculates the mathematical relationship between two fighters based on reach, pace, grappling, and striking differentials.
- **Style Interaction**: Applies modifiers based on the interaction of specific martial arts styles (e.g., Wrestler vs. Striker).

### 2. Monte Carlo Simulation Engine (`backend/engines/monte_carlo.py`)
- **Iteration Logic**: Runs 10,000+ simulations per matchup to stabilize probability curves.
- **Outcome Mapping**: Distributes wins across KO/TKO, Submission, and Decision based on fighter archetypes and chaos factors.

### 3. Scoring & Judging Model (`backend/engines/scoring.py`)
- **Judge Bias Matrices**: Simulates different judging styles (Striking-heavy, Grappling-heavy, Balanced).
- **Round-by-Round Aggregation**: Calculates 10-9, 10-8, and 10-7 scores to determine decision outcomes.

### 4. Style & Roster System (`styles/` and `data/fighters/`)
- **Hierarchical Styles**: 27 sub-styles across 9 major categories.
- **Fighter Profiles**: Realistic attributes including gender, ethnicity, and "Street-Fighter" style gi variants.
- **OVR Ratings**: Computed overall ratings based on normalized performance metrics.

## 🗄️ Data Schema
- **Fighters**: Bio, stats, style tags, and gym tier.
- **Fights**: Historical data and context modifiers (short notice, altitude).
- **Styles**: Impact vectors for striking, grappling, and pace.

## 🎨 Visual & UI Strategy
- **PS5 Realism**: High-fidelity avatars and stadium lighting.
- **Live Odds Legs**: Dynamic payout panels that update as simulations run.
- **Simulation Flash**: Visual energy bursts during the computation phase to signal engine activity.
