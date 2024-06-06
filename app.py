from flask import *
from deck import Deck
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        #x = ListofCards

        pass
    return render_template('main.html')
@app.route("/start_game", methods=['GET', 'POST'])
def start_game():
    #call sashas function for a dictionary of cards
    return jsonify({"Heart": 3, "Spade": 4})
if __name__ == "__main__":
    app.run(debug=True)