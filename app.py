from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

dados_pessoais = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        if nome and email and telefone:
            dados_pessoais.append({
                'nome': nome,
                'email': email,
                'telefone': telefone
            })
            return redirect(url_for('listar'))
    return render_template('cadastrar.html')

@app.route('/listar')
def listar():
    return render_template('listar.html', dados=dados_pessoais)

if __name__ == '__main__':
    app.run(debug=True)
