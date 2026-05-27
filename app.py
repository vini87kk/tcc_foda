from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def cadastro():
    return render_template('cadastro.html')

@app.route('/dados')
def bancodedados():
    return render_template('bancodedados.html')

if __name__ == '__main__':
    
    app.run(debug=True , host='0.0.0.0')
