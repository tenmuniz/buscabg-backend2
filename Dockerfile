# Use imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia tudo do projeto
COPY . .

# Instala dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expõe a porta usada pelo Flask
EXPOSE 10000

# Comando de inicialização
CMD ["python", "main.py"]
