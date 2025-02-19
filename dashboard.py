import streamlit as st
import sqlite3
import pandas as pd
from model import predict_match
import time  # Import time to generate unique keys

st.title("Sports Analytics Dashboard")

# Sport selection
sport = st.selectbox("Select Sport", ["basketball", "soccer"])

# Team selection
conn = sqlite3.connect('sports.db')
teams_df = pd.read_sql_query(f"SELECT * FROM Teams WHERE sport = '{sport}'", conn)
team1 = st.selectbox("Select Team 1", teams_df['name'])
team2 = st.selectbox("Select Team 2", teams_df['name'])

# Load players for selected teams
team1_players = pd.read_sql_query(f"SELECT * FROM Players WHERE team_id = {teams_df[teams_df['name'] == team1]['team_id'].values[0]} AND sport = '{sport}'", conn)
team2_players = pd.read_sql_query(f"SELECT * FROM Players WHERE team_id = {teams_df[teams_df['name'] == team2]['team_id'].values[0]} AND sport = '{sport}'", conn)

# Function to display player selection by position
def select_players_by_position(players, sport, team_name, team_id):
    selected_players = []
    if sport == "basketball":
        positions = ["Guard", "Forward", "Center"]
        default_players_per_position = {"Guard": 2, "Forward": 2, "Center": 1}  # 5 players total
    elif sport == "soccer":
        positions = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
        default_players_per_position = {"Goalkeeper": 1, "Defender": 4, "Midfielder": 4, "Forward": 2}  # 11 players total

    for position in positions:
        position_players = players[players['position'] == position]
        # Default selection: top N players based on rating
        default_selection = position_players.sort_values(by='rating', ascending=False).head(default_players_per_position[position])['name'].tolist()
        selected = st.multiselect(
            f"Select {position}(s) for {team_name}",
            position_players['name'].tolist(),
            default=default_selection,  # Pre-select default players
            key=f"{team_id}_{position}_{time.time()}"  # Unique key with timestamp
        )
        selected_players.extend(selected)
    return selected_players

# Get team IDs
team1_id = teams_df[teams_df['name'] == team1]['team_id'].values[0]
team2_id = teams_df[teams_df['name'] == team2]['team_id'].values[0]

# Select players for Team 1
st.subheader(f"Select Players for {team1}")
team1_selected = select_players_by_position(team1_players, sport, team1, team1_id)

# Select players for Team 2
st.subheader(f"Select Players for {team2}")
team2_selected = select_players_by_position(team2_players, sport, team2, team2_id)

# Predict match outcome
if st.button("Predict Match"):
    if not team1_selected or not team2_selected:
        st.error("Please select players for both teams before predicting.")
    else:
        prediction = predict_match(team1_id, team2_id, team1_selected, team2_selected, sport)
        st.write(f"Predicted Score: {team1} {prediction['team1_score']} - {team2} {prediction['team2_score']}")
