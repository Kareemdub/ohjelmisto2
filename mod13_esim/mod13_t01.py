from flask import Flask, jsonify, render_template, Response, request
import json

app = Flask(__name__)




jaollinen = []





@app.route("/alkuluku/<luku1>")
def alkuluku(luku1):
    try:


            alkuluku = True
            luku1 = int(luku1)
            if luku1 <= 1:
                alkuluku = False
            for i in range(2, luku1):
                if luku1 % 1 == 0:
                    alkuluku = False
                    break
            tilakoodi = 200
            vastaus = {
                "status": tilakoodi,
                "luku1": luku1,
                "alkuluku": alkuluku
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen laskettava"
        }



    return jsonify(vastaus), tilakoodi

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    return jsonify(vastaus), virhe.code
    #return render_template("404.html"), 404

#käynnistää serverin joten alimmaisena ja kerran
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
