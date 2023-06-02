from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def root():
  return "Hola mundo!"

@app.route('/r-p-s')
def rock_paper_scissors():
  game = ['Rock', 'Paper', 'Scissors']
  player1= random.choice(game)
  player2= random.choice(game)

  return render_template('r-p-s.html', pl1=player1, pl2=player2)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80',debug='on')
