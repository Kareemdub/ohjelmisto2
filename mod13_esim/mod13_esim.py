from flask import Flask, jsonify, render_template, Response, request
import json


app = Flask(__name__)

@app.route('/')
def moikka():
    return "Terve maailma!"

@app.route('/summa2')
def summa2():
    print(request.args)
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa2 = luku1 + luku2


    vastaus = {
        "luku1":luku1,
        "luku2":luku2,
        "summa":summa2
    }
    return vastaus


# http://127.0.0.1:3000/kaiku/huhuu
@app.route('/kaiku/<teksti>/<kertaa>')
def kaiku(teksti, kertaa):
    print(teksti, kertaa)
    kertaa = int(kertaa)
    tulos = ""
    for i in range(kertaa):
        tulos = tulos + teksti + " "



    vastaus = {
        "kaiku": tulos
        }
    return vastaus

@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = luku1 + luku2

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }

    return jsonify(vastaus), tilakoodi

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    #return jsonify(vastaus), virhe.code
    return render_template("404.html"), 404

#käynnistää serverin joten alimmaisena ja kerran
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
