from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    team1 = data.get('team1')
    team2 = data.get('team2')

    if not team1 or not team2:
        return jsonify({"error": "Нужно указать обе команды"}), 400

    # Заглушка: парсинг championat.com и расчет прогноза
    # Для простоты здесь статические данные
    result = {
        "match_info": {
            "date": "29 августа 2025, 17:30",
            "home_team": team1,
            "away_team": team2,
            "tournament": "Азербайджанская Премьер-лига"
        },
        "head_to_head": {
            "total_matches": 5,
            team1: {"wins": 3, "goals_scored": 10, "goals_conceded": 7},
            team2: {"wins": 2, "goals_scored": 7, "goals_conceded": 10}
        },
        "form": {
            team1: "Сбалансированная атака, сильны дома",
            team2: "Сильная оборона, но слабее в гостях"
        },
        "prediction": {
            "winner": team1,
            "total_over_under": "Тотал меньше 2.5",
            "btts": "Нет",
            "expected_score": "1:0 или 2:1"
        }
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
