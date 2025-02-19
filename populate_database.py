import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('sports.db')
cursor = conn.cursor()

# Delete existing data from Teams and Players tables
cursor.execute("DELETE FROM Teams")
cursor.execute("DELETE FROM Players")

# Insert sample teams
teams = [
    (1, 'Lakers', 'basketball'),
    (2, 'Warriors', 'basketball'),
    (3, 'Barcelona', 'soccer'),
    (4, 'Real Madrid', 'soccer')
]
cursor.executemany('INSERT INTO Teams VALUES (?, ?, ?)', teams)

# Insert sample players for basketball
basketball_players = [
    (1, 'LeBron James', 1, 'basketball', 95.0, 'Forward'),
    (2, 'Anthony Davis', 1, 'basketball', 90.0, 'Forward'),
    (3, 'Russell Westbrook', 1, 'basketball', 85.0, 'Guard'),
    (4, 'Carmelo Anthony', 1, 'basketball', 80.0, 'Forward'),
    (5, 'Dwight Howard', 1, 'basketball', 75.0, 'Center'),
    (6, 'Stephen Curry', 2, 'basketball', 95.0, 'Guard'),
    (7, 'Klay Thompson', 2, 'basketball', 90.0, 'Guard'),
    (8, 'Draymond Green', 2, 'basketball', 85.0, 'Forward'),
    (9, 'Andrew Wiggins', 2, 'basketball', 80.0, 'Forward'),
    (10, 'James Wiseman', 2, 'basketball', 75.0, 'Center'),
    # Add more players to reach 15 per team
    (11, 'Player 11', 1, 'basketball', 70.0, 'Guard'),
    (12, 'Player 12', 1, 'basketball', 70.0, 'Forward'),
    (13, 'Player 13', 1, 'basketball', 70.0, 'Center'),
    (14, 'Player 14', 1, 'basketball', 70.0, 'Guard'),
    (15, 'Player 15', 1, 'basketball', 70.0, 'Forward'),
    (16, 'Player 16', 2, 'basketball', 70.0, 'Guard'),
    (17, 'Player 17', 2, 'basketball', 70.0, 'Forward'),
    (18, 'Player 18', 2, 'basketball', 70.0, 'Center'),
    (19, 'Player 19', 2, 'basketball', 70.0, 'Guard'),
    (20, 'Player 20', 2, 'basketball', 70.0, 'Forward')
]
cursor.executemany('INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?)', basketball_players)

# Insert sample players for soccer
soccer_players = [
    (21, 'Lionel Messi', 3, 'soccer', 94.0, 'Forward'),
    (22, 'Sergio Aguero', 3, 'soccer', 88.0, 'Forward'),
    (23, 'Gerard Pique', 3, 'soccer', 85.0, 'Defender'),
    (24, 'Sergio Busquets', 3, 'soccer', 87.0, 'Midfielder'),
    (25, 'Marc-Andre ter Stegen', 3, 'soccer', 89.0, 'Goalkeeper'),
    (26, 'Cristiano Ronaldo', 4, 'soccer', 95.0, 'Forward'),
    (27, 'Karim Benzema', 4, 'soccer', 90.0, 'Forward'),
    (28, 'Sergio Ramos', 4, 'soccer', 88.0, 'Defender'),
    (29, 'Luka Modric', 4, 'soccer', 89.0, 'Midfielder'),
    (30, 'Thibaut Courtois', 4, 'soccer', 91.0, 'Goalkeeper'),
    # Add more players to reach 22 per team
    (31, 'Player 31', 3, 'soccer', 80.0, 'Defender'),
    (32, 'Player 32', 3, 'soccer', 80.0, 'Midfielder'),
    (33, 'Player 33', 3, 'soccer', 80.0, 'Forward'),
    (34, 'Player 34', 3, 'soccer', 80.0, 'Goalkeeper'),
    (35, 'Player 35', 3, 'soccer', 80.0, 'Defender'),
    (36, 'Player 36', 3, 'soccer', 80.0, 'Midfielder'),
    (37, 'Player 37', 3, 'soccer', 80.0, 'Forward'),
    (38, 'Player 38', 3, 'soccer', 80.0, 'Goalkeeper'),
    (39, 'Player 39', 3, 'soccer', 80.0, 'Defender'),
    (40, 'Player 40', 3, 'soccer', 80.0, 'Midfielder'),
    (41, 'Player 41', 4, 'soccer', 80.0, 'Defender'),
    (42, 'Player 42', 4, 'soccer', 80.0, 'Midfielder'),
    (43, 'Player 43', 4, 'soccer', 80.0, 'Forward'),
    (44, 'Player 44', 4, 'soccer', 80.0, 'Goalkeeper'),
    (45, 'Player 45', 4, 'soccer', 80.0, 'Defender'),
    (46, 'Player 46', 4, 'soccer', 80.0, 'Midfielder'),
    (47, 'Player 47', 4, 'soccer', 80.0, 'Forward'),
    (48, 'Player 48', 4, 'soccer', 80.0, 'Goalkeeper'),
    (49, 'Player 49', 4, 'soccer', 80.0, 'Defender'),
    (50, 'Player 50', 4, 'soccer', 80.0, 'Midfielder')
]
cursor.executemany('INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?)', soccer_players)

# Commit changes and close
