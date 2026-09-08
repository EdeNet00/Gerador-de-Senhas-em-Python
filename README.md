# Gerador-de-Senhas-em-Python

Um gerador de senhas desenvolvido com Python, Flask, Flask-CORS, HTML, CSS e JavaScript.
O projeto permite que o usuário escolha o tamanho da senha e quais tipos de caracteres deseja utilizar: letras, números e símbolos. A senha é gerada pelo backend em Python e enviada para a interface através de uma API.


# Funcionalidades:
1. Escolher o tamanho da senha.
2.Utilizar letras maiúsculas e minúsculas.
3.Utilizar números.
4. Utilizar símbolos.
5. Gerar uma senha aleatória.
6. Informar ao usuário caso nenhuma opção de caractere seja selecionada.
7. Comunicação entre JavaScript e Python através de uma API REST.
8.Utilização de CORS para permitir a comunicação entre frontend e backend.



# Tecnologias utilizadas:
# Backend
Python 3
Flask
Flask-CORS
Random

# Frontend
HTML5
CSS3
JavaScript


# A estrutura recomendada para o projeto é:
projeto senhas/
1. │
2. ├── senha.py
3. ├── index.html
4. ├── script.js
5. └── README.md

# senha.py
É o arquivo responsável pelo backend da aplicação.
Ele utiliza Flask para criar o servidor e disponibiliza a rota:

# POST /gerar
Essa rota recebe as configurações enviadas pelo JavaScript, gera uma senha aleatória e retorna o resultado.

# index.html
É a página principal da aplicação.

# Nela estão:
Campo para definir o tamanho da senha.
Opção para utilizar letras.
Opção para utilizar números.
Opção para utilizar símbolos.
Botão para gerar a senha.
Área onde a senha gerada é exibida.
O arquivo também contém o código CSS responsável pelo visual da página.

# script.js
É responsável pela interação da página com o backend.

Quando o usuário clica no botão GERAR SENHA, o JavaScript coleta as opções selecionadas e envia uma requisição POST para o servidor Flask.

# Instalação no terminal
1. Verifique se o Python está instalado
python --version

3. Instale o Flask
python -m pip install flask

5. Instale o Flask-CORS
python -m pip install flask-cors

Ou instale os dois de uma vez:
python -m pip install flask flask-cors

# Como executar:
1. Abra a pasta do projeto
Abra a pasta projeto senhas no VS Code.

2. Inicie o servidor
No terminal, execute:

python senha.py
Se tudo estiver funcionando corretamente, aparecerá:
* Running on http://127.0.0.1:5000
  
3. Abra o index.html
Abra o arquivo index.html no navegador.

# O JavaScript irá se comunicar com o servidor Flask através do endereço:

http://127.0.0.1:5000


# O funcionamento ocorre da seguinte maneira:

Usuário
   ↓
index.html
   ↓
script.js
   ↓
API Flask
   ↓
senha.py
   ↓
Geração da senha
   ↓
Resposta JSON
   ↓
script.js
   ↓
Senha exibida na tela



1. Usuário escolhe as configurações
O usuário informa o tamanho da senha e escolhe se deseja utilizar:

Letras.
Números.
Símbolos.



2. script.js envia os dados
O JavaScript utiliza fetch() para enviar uma requisição POST para:
http://127.0.0.1:5000/gerar


Os dados são enviados em formato JSON:

{
    "tamanho": 12,
    "letras": true,
    "numeros": true,
    "simbolos": true
}
3. senha.py recebe os dados
O Flask recebe as informações:

dados = request.json
Depois, o programa verifica quais tipos de caracteres foram selecionados.

4. A senha é gerada
O programa utiliza o módulo random para escolher caracteres aleatoriamente.

Os caracteres disponíveis são:
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*;:()-_=+[]{}"

5. A senha é enviada para o frontend
Depois de gerar a senha, o Flask retorna um JSON:

{
    "senha": "A8@kP2#xLm91"
}

O script.js recebe a resposta e exibe a senha no index.html.


# API:
POST /gerar
Endpoint responsável por gerar uma nova senha.

Requisição
{
    "tamanho": 12,
    "letras": true,
    "numeros": true,
    "simbolos": true
}
Resposta de sucesso
{
    "senha": "aB8@xP2#Lm91"
}
Resposta de erro
Caso nenhuma opção seja selecionada:

{
    "erro": "Escolha pelo menos uma opção."
}
Nesse caso, a API retorna:

400 Bad Request

# CORS
O projeto utiliza Flask-CORS para permitir a comunicação entre o frontend e o backend.

No arquivo senha.py:

from flask_cors import CORS
app = Flask(__name__)
CORS(app)


# Interface
A interface possui:

. Tema relacionado a segurança.
. Fundo com gradiente.
. Layout centralizado.
. Botão para gerar a senha.
. Área para exibir a senha.
. Mensagem de erro caso ocorra algum problema.
. Layout responsivo.
. Observação

OBS:
Este projeto foi desenvolvido com finalidade educacional, demonstrando a comunicação entre um frontend em HTML/JavaScript e um backend em Python utilizando Flask.
Para sistemas que exigem alto nível de segurança, recomenda-se utilizar métodos de geração de números aleatórios apropriados para fins criptográficos.
👨‍💻
