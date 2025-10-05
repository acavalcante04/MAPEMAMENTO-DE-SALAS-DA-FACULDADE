# MAPEMAMENTO-DE-SALAS-DA-FACULDADE
Projeto de implementação de conecimento e aprendizagem com finalidade em resolver um problema de localização e organização de salas da faculdade dos desenvolvedores do projeto 

# 📌 Sistema Web de Localização Interna via QR Code

## 📖 Visão Geral
Este projeto tem como objetivo desenvolver um sistema web responsivo para **localização interna** em ambientes educacionais, utilizando **QR Codes** como pontos de referência.  
Alunos e visitantes poderão escanear QR Codes posicionados nos blocos da instituição para encontrar rotas até suas salas.  
A administração (professores, coordenação e diretoria) terá acesso a um painel de controle completo para gerenciamento.

---

## 🎯 Objetivos
- Facilitar a **localização de salas e blocos** por meio de QR Codes.
- Disponibilizar **rotas claras** até o destino.
- Permitir que professores e coordenação cadastrem **aulas e reservas de salas**.
- Garantir que a diretoria possa gerenciar **blocos, salas ativas/inativas** e reservas.
- Oferecer uma solução **simples, escalável e acessível via navegador**.

---

## 🛠️ Tecnologias
### Frontend
- HTML5, CSS3, JavaScript
- Framework: React.js (planejado)
- Mapas: Leaflet.js
- QR Code: qrcode.js ou jsQR
- Estilização: Bootstrap ou Tailwind

### Backend
- Python + FastAPI
- Autenticação: JWT (JSON Web Token), bcrypt para hash de senhas

### Banco de Dados
- PostgreSQL (produção)
- SQLite (testes locais)

### Infraestrutura
- Hospedagem: Netlify/Heroku (frontend) e Heroku/AWS (backend)
- Geração de QR Codes: python-qrcode (backend) ou qrcode.js (frontend)

---

## 👥 Perfis de Usuário

### 🔹 Visitante/Aluno
- Escaneia QR Code para identificar ponto de origem
- Visualiza o **mapa com rotas**
- Consulta **aulas em andamento**

### 🔹 Professor
- Login no sistema
- Pode cadastrar aulas e reservar salas

### 🔹 Coordenação
- Permissões iguais às dos professores
- Pode também reservar salas para outros professores

### 🔹 Diretoria
- Acesso administrativo avançado
- Gerencia **blocos (criar/remover)**
- Ativa ou desativa **salas**
- Pode reservar salas para professores

---

## ⚙️ Funcionalidades
- Escaneamento de QR Codes
- Exibição de rotas no mapa
- Consulta de aulas em andamento
- Login e autenticação com níveis de acesso
- Cadastro de salas, blocos e horários
- Importação de horários via CSV
- Reserva de salas

---

## 📐 Arquitetura
- **Frontend (React.js)** → interface responsiva para público e admins
- **Backend (FastAPI ou Node.js)** → API para rotas, salas e autenticação
- **Banco de Dados (PostgreSQL)** → gerenciamento de salas, blocos, usuários e horários
- **Mapas (Leaflet.js)** → exibição de rotas e localização interna

---
