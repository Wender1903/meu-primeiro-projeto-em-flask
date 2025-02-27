# 📌 Flask Cálculo de Média  

Este é um pequeno projeto Flask que calcula a média final de um aluno com base nas seguintes notas:  
- **MAPs**: Média das Avaliações Parciais (AP1 e AP2).  
- **MPAI**: Média das Provas de Avaliação Integrada (PAI1, PAI2 e PAI3).  
- **PF**: Nota da Prova Final.  
- **MF**: Média Final, calculada com os seguintes pesos:
  - `MAPs * 30%`
  - `MPAI * 30%`
  - `PF * 40%`

## 🚀 Como funciona?
Ao acessar a rota `http://127.0.0.1:5000/`, o código cria um objeto **Aluno** com notas pré-definidas, calcula as médias e retorna os resultados em **JSON**.

## 🛠 Tecnologias utilizadas:
- Python  
- Flask  

## 📌 Como rodar o projeto?
1. Clone o repositório:  
   ```sh
   git clone https://github.com/Wender1903/meu-primeiro-projeto-em-flask.git
