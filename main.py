from flask import Flask, request, jsonify
import fitz  # PyMuPDF
import os

app = Flask(__name__)

# Garante que a pasta 'pdfs' existe
if not os.path.exists("pdfs"):
    os.makedirs("pdfs")

def extrair_texto_pdf(caminho_arquivo):
    texto = ""
    with fitz.open(caminho_arquivo) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

@app.route("/buscar")
def buscar():
    palavra = request.args.get("palavra", "").lower()
    if not palavra:
        return jsonify({"erro": "Palavra não informada"}), 400

    resultados = []

    for nome_arquivo in os.listdir("pdfs"):
        if nome_arquivo.endswith(".pdf"):
            caminho = os.path.join("pdfs", nome_arquivo)
            texto = extrair_texto_pdf(caminho)
            if palavra in texto.lower():
                partes = texto.lower().split(palavra)
                trecho = partes[0][-60:] + palavra + partes[1][:60] if len(partes) > 1 else palavra
                resultados.append({
                    "nome": nome_arquivo,
                    "trecho": trecho,
                    "link_pdf": f"https://buscabg-backend.onrender.com/pdfs/{nome_arquivo}"
                })

    return jsonify(resultados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
