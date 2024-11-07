from flask import Flask, render_template #importa a biblioteca (módulo) flask, a classe Flask e a classe render_template

app = Flask(__name__) #cria o objeto app da classe Flask

@app.route("/") #decorator que indica a rota da aplicação ( "/" é basicamente a homepage)
def hello_world(): #função que retorna o texto "Hello World"
    return render_template('index.html') #executa o arquivo index.html

if __name__ == "__main__": #verifica se o arquivo é executado diretamente ou importado
  app.run(host="0.0.0.0", debug=True) #executa a aplicação