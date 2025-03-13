import pandas as pd

df = pd.read_csv("data/processed/processed_ufc.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by="date", ascending=True)

fighter_elo = {}
BASE_ELO = 1500
def get_elo(fighter):
    return fighter_elo.get(fighter, BASE_ELO)

def update_elo(fighter1, fighter2, result, k=32):
    elo1 = get_elo(fighter1)
    elo2 = get_elo(fighter2)

    expected1 = 1 / (1 + 10 **((elo2 - elo1) / 400))
    expected2= 1 / (1 + 10 ** ((elo1 - elo2) / 400))

    if result == "win":
        newelo1 = elo1 + k * (1 - expected1)
        newelo2 = elo2 + k * (0 - expected2)
    
    elif result == "draw":
        newelo1 = elo1 + k * (0.5 - expected1)
        newelo2 = elo2 + k * (0.5 - expected2)

    else:
        newelo1, newelo2 = elo1, elo2

    fighter_elo[fighter1] = newelo1
    fighter_elo[fighter2] = newelo2
    
    return elo1, newelo1, elo2, newelo2

fight_results = []

for index, row in df.iterrows():
    winner = row["fighter_1"]
    loser = row["fighter_2"]

    winner_before, winner_after, loser_before, loser_after = update_elo(winner, loser, row["result"])

    fight_results.append([
        row["event"], row["date"],
        winner, winner_before, winner_after,
        row["method"], row["round"],
        loser, loser_before, loser_after
    ])

elo_df = pd.DataFrame(fight_results, columns=[
    "event", "date",
    "fighter_1", "fighter_1_elo_before", "fighter_1_elo_after",
    "method", "round",
    "fighter_2", "fighter_2_elo_before", "fighter_2_elo_after"
])
df_final_elo = pd.DataFrame(fighter_elo.items(), columns=["fighter", "final_elo"])
elo_df.to_csv("data/processed/fight_elo_change.csv", index=False)
df_final_elo.to_csv("data/processed/final_elo.csv")