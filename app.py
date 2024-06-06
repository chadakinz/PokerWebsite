from flask import *
from deck import Deck
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        x = start_game()

        pass
    return render_template('main.html')
def start_game():
    deck = Deck()
    deck.shuffle()
    cards = deck.deal_cards(2)
    print(cards)
    return cards
if __name__ == "__main__":
    app.run(debug=True)