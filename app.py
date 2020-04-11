from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('/Users/almostloverv/Desktop/953494FinalProject/leagueoflegends/LeagueofLegends.csv')

@app.route('/data', methods=['GET'])
def get_data():

    blue_win = data.bResult.sum().item()
    red_win = data.rResult.sum().item()

    result = {
        "blue win": blue_win ,
        "red win": red_win
    }

    return jsonify(result)



if __name__ == '__main__':
    app.run()
