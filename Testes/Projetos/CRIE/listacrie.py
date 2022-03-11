from flask import Flask, render_template

# instancia flask no app
app = Flask(__name__)


@app.route("/crie")
def pagecrie():        
    return render_template("crie.html")



# executa no navegador
if __name__ == "__main__":
    app.run(debug=True)