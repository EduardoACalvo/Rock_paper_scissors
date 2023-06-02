from flask import Flask, render_template, request
import random


app = Flask(__name__)

@app.route('/')
def raiz():
  game = ['Rock', 'Paper', 'Scissors']
  player1= random.choice(game)
  player2= random.choice(game)

  return render_template('index.html', pl1=player1, pl2=player2)
  



if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80',debug='')


  #curl "https://api.open-meteo.com/v1/forecast?latitude=-38.72&longitude=-62.27&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"