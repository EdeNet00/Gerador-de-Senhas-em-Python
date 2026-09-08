const botao = document.getElementById("botao");

botao.addEventListener("click", gerarSenha);

async function gerarSenha() {

    const tamanho = Number(document.getElementById("tamanho").value);
    const letras = document.getElementById("letras").checked;
    const numeros = document.getElementById("numeros").checked;
    const simbolos = document.getElementById("simbolos").checked;

    try {

        const resposta = await fetch("http://127.0.0.1:5000/gerar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                tamanho: tamanho,
                letras: letras,
                numeros: numeros,
                simbolos: simbolos
            })
        });

        const dados = await resposta.json();

        if (dados.erro) {
            document.getElementById("mensagem").textContent = dados.erro;
            return;
        }

        document.getElementById("senha").textContent = dados.senha;
        document.getElementById("mensagem").textContent = "";

    } catch (erro) {

        document.getElementById("mensagem").textContent =
            "Não foi possível conectar ao Python.";

        console.error(erro);
    }
}
