import sqlite3
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def train_model(sport):
    """
    Train a machine learning model to predict player performance.
    """
    # Load data
    conn = sqlite3.connect('sports.db')
    players_df = pd.read_sql_query(f"SELECT * FROM Players WHERE sport = '{sport}'", conn)

    # Encode categorical data (e.g., 'position')
    encoder = OneHotEncoder(sparse_output=False, drop='first')  # Use drop='first' to avoid multicollinearity
    encoded_positions = encoder.fit_transform(players_df[['position']])

    # Convert encoded positions to a DataFrame
    encoded_positions_df = pd.DataFrame(encoded_positions, columns=encoder.get_feature_names_out(['position']))

    # Combine encoded positions with other features
    X = pd.concat([players_df[['rating']], encoded_positions_df], axis=1)
    y = players_df['rating']  # Target (example)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    return model, encoder  # Return the encoder for use in prediction

def predict_match(team1_id, team2_id, team1_selected, team2_selected, sport):
    """
    Predict the match score for two teams based on selected players' ratings.
    """
    # Load team data
    conn = sqlite3.connect('sports.db')
    team1_players = pd.read_sql_query(f"SELECT * FROM Players WHERE team_id = {team1_id} AND sport = '{sport}'", conn)
    team2_players = pd.read_sql_query(f"SELECT * FROM Players WHERE team_id = {team2_id} AND sport = '{sport}'", conn)

    # Filter selected players
    team1_players = team1_players[team1_players['name'].isin(team1_selected)]
    team2_players = team2_players[team2_players['name'].isin(team2_selected)]

    # Calculate average rating for selected players
    team1_avg_rating = team1_players['rating'].mean()
    team2_avg_rating = team2_players['rating'].mean()

    # Simulate realistic scores based on sport
    if sport == 'basketball':
        # Basketball scores range between 100 and 150
        team1_score = int(np.clip(team1_avg_rating + np.random.normal(0, 10), 100, 150))
        team2_score = int(np.clip(team2_avg_rating + np.random.normal(0, 10), 100, 150))
    elif sport == 'soccer':
        # Soccer scores range between 0 and 5
        team1_score = int(np.clip(team1_avg_rating / 20 + np.random.normal(0, 1), 0, 5))
        team2_score = int(np.clip(team2_avg_rating / 20 + np.random.normal(0, 1), 0, 5))
    else:
        raise ValueError("Unsupported sport")

    return {"team1_score": team1_score, "team2_score": team2_score}
