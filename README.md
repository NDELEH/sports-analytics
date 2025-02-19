# Sports Analytics Dashboard

This project is a **Sports Analytics Dashboard** that allows users to predict match scores and player performance for basketball and soccer. Users can select teams, view pre-selected players, and remove players from the lineup before predicting the match outcome.

---

## Features

- **Team Selection**: Choose from 10 teams (5 basketball and 5 soccer teams).
- **Player Selection**:
  - For **basketball**, each team comes with 5 pre-selected players (2 Guards, 2 Forwards, and 1 Center).
  - For **soccer**, each team comes with 11 pre-selected players (1 Goalkeeper, 4 Defenders, 4 Midfielders, and 2 Forwards).
- **Match Prediction**: Predict the match score based on the selected players' ratings.
- **Player Exclusion**: Remove players from the lineup due to injuries or suspensions.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the interactive web dashboard.
- **SQLite**: For storing player, team, and match data.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For machine learning-based predictions (future implementation).

---

## Setup Instructions

### Prerequisites

1. **Python 3.7 or higher**: Install Python from [python.org](https://www.python.org/).
2. **Git**: Install Git from [git-scm.com](https://git-scm.com/).

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sports-analytics.git
   cd sports-analytics
