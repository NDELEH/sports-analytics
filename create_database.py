import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('sports.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Players (
        player_id INTEGER PRIMARY KEY,
        name TEXT,
        team_id INTEGER,
        sport TEXT,
        rating REAL,
        position TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teams (
        team_id INTEGER PRIMARY KEY,
        name TEXT,
        sport TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Matches (
        match_id INTEGER PRIMARY KEY,
        team1_id INTEGER,
        team2_id INTEGER,
        score_team1 INTEGER,
        score_team2 INTEGER,
        date DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Injuries (
        injury_id INTEGER PRIMARY KEY,
        player_id INTEGER,
        start_date DATE,
        end_date DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Suspensions (
        suspension_id INTEGER PRIMARY KEY,
        player_id INTEGER,
        start_date DATE,
        end_date DATE
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
