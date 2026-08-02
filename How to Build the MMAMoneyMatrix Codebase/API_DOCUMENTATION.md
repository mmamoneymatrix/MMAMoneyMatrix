# MMAMoneyMatrix API Documentation

## Base URL
`http://localhost:5000/api`

## Endpoints

### 1. Run Simulation
**Endpoint**: `POST /run-simulation`
**Description**: Triggers the Monte Carlo engine to simulate a fight between two fighters.
**Request Body**:
```json
{
  "fighter_a": { ...fighter_stats... },
  "fighter_b": { ...fighter_stats... },
  "iterations": 10000
}
```
**Response**:
- `geometry`: The calculated Fight Geometry Object.
- `results`: Win probabilities, method breakdowns, and round distributions.

### 2. Import Fighter
**Endpoint**: `POST /import-fighter`
**Description**: Ingests fighter data from external sources (UFC Stats, ESPN) and normalizes it.
**Request Body**:
```json
{
  "url": "http://ufcstats.com/fighter-details/..."
}
```

### 3. Get Fighter
**Endpoint**: `GET /get-fighter/<id>`
**Description**: Retrieves a specific fighter profile and their generated stats from the database.

### 4. Get History
**Endpoint**: `GET /get-history/<id>`
**Description**: Fetches the fight history and performance trends for a specific fighter.
