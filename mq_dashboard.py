import streamlit as st
import subprocess

# Função para executar o script shell e capturar a saída
def executar_script(script_path):
    process = subprocess.Popen(script_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = ""
    for line in process.stdout:
        st.write(line.decode("ISO-8859-1"))  # Usar o codec ISO-8859-1
        output += line.decode("ISO-8859-1")
    process.wait()
    if process.returncode != 0:
        st.error(f"Erro ao executar o script: {process.stderr.read().decode('ISO-8859-1')}")
    return output

# Interface do Streamlit
st.title("Validação de Queue Managers - MQ")

if st.button("Executar Validação"):
    st.write("Executando script de validação MQ...")
    resultado = executar_script('./verifica_mq.sh')  # Caminho para o script shell
    st.write("Dados:")
    st.text(resultado)

