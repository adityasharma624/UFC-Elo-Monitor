# UFC-Elo-Monitor  

**EloTracker** is a personal project designed to track and analyze UFC fighter rankings using an **Elo rating system**. It adjusts Elo based on fight outcomes, with **higher gains for early-round finishes** and **degradation for inactivity**. The project also maintains a **time-series of Elo changes** to visualize fighter progression over time.  

## Data Sources  
- **Kaggle Dataset**: [Every UFC Fight Ever](https://www.kaggle.com/datasets/trixster23/every-ufc-fight-ever/data)  
- **UFCStats Website**: [UFC Fight Records](http://ufcstats.com/statistics/events/completed?page=all)  

## Features Implemented  
- **Elo rating system**: Ratings update per fight, using a fixed **K=32**.  
- **Data cleaning & structuring**: Organized and processed fight records (**~10,000 fights, 2,500+ fighters** from **1993-2024**).  
- **Time-series tracking**: Maintains historical Elo changes.  
- **Basic visualizations**: Graphs for Elo progression and fighter comparisons.  

## Future Improvements  
1. **Fighter inactivity Elo decay** – Elo reduction for long inactivity.  
2. **Round-based K factor** – Higher impact for early-round finishes.  
3. **Underdog bonus** – Greater Elo gain for fighters winning with <30% probability.  
4. **Fight experience factor** – Adjust K-value based on experience level.  
5. **Weight class impact** – Elo adjustments when fighters switch weight classes.  

## How to Run  
1. Install dependencies:  
   ```sh
   pip install -r requirements.txt

2. Run Elo calculation script
    ```sh
    python src/elo_calc.py
    ```


## Scope
This keeps the **UFC-Elo-Monitor (EloTracker)** description upfront while maintaining clarity in features and functionality. Let me know if you want any tweaks!


