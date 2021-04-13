from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")  # página de inicio
def Welcome():
    p = "Para seguir escribe /play en la url! "
    return render_template("playground2.html", numOfSqu = 0, new_color = None, phrase = p)

@app.route("/play")  # para ver 3 cuadros celestes
def Square3():
    phrase = " Ahora escribe '/play/(número de cuadros que quieres ver)' en la url"
    return render_template("playground2.html", numOfSquare=3, new_color="lightblue",phrase = phrase)

@app.route("/play/<int:num>")  # para ver otra x cantidad de cuadros
def repeatedSquare(num):
    phrase = "Ahora escribe /play/(número de cuadros que quieres ver)/color'en la url'"
    return render_template("playground2.html", numOfSquare=num, new_color="lightblue",phrase = phrase)


@app.route('/play/<int:num>/<color>')  # para ver  x cantidad de cuadros y color diferente
def coloredSquare(num, color):
    phrase = "Fin"
    return render_template("playground2.html", numOfSquare=num, new_color= color, phrase= phrase)


if __name__=="__main__":   
    app.run(debug=True)  