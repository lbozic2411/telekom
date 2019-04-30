from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ponuda")
def ponuda():
    return render_template("ponuda.html")

@app.route("/naruci", methods=["POST"])
def naruci():
    ime = request.form.get("ime")
    telefon = request.form.get("telefon")
    adresa = request.form.get("adresa")
    model = request.form.get("model")
    tarifa = request.form.get("tarifa")

    return render_template("naruci.html", ime=ime, telefon=telefon, adresa=adresa, model=model, tarifa=tarifa)



if __name__ == '__main__':
    app.run()
