# 🚀 UserManager - CRUD de Usuários com Django

![Django](https://img.shields.io/badge/Django-4.0-green) ![Python](https://img.shields.io/badge/Python-3.9-blue) ![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)

UserManager é uma aplicação web simples para gerenciar usuários. Permite **criar, listar, editar e excluir** usuários de forma intuitiva, utilizando **Django** e **SQLite**.

---

## 📌 Tecnologias Utilizadas  
- 🐍 **Python 3.x**  
- 🎯 **Django 4.x**  
- 💾 **SQLite**  
- 🎨 **HTML + Bootstrap**  

---

## 📂 Como Configurar e Rodar o Projeto  

### 🔹 **1️⃣ Clonar o Repositório**  
```bash
git clone https://github.com/seu-usuario/UserManager.git
cd UserManager
```
### 🔹 2️⃣ Criar e Ativar o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```
### 🔹 3️⃣ Criar o Banco de Dados
```bash
python manage.py migrate
```
### 🔹 4️⃣ Criar um Superusuário (para acessar o Django Admin)
```bash
python manage.py createsuperuser
```
### 🔹 5️⃣ Rodar o Servidor
```bash
python manage.py runserver
```
📌 Acesse a aplicação em: http://127.0.0.1:8000/

---

## 🛠 Funcionalidades
- ✅ Criar usuários
- ✅ Listar usuários cadastrados
- ✅ Editar usuários
- ✅ Excluir usuários
- ✅ Autenticação via Django Admin

---

## 👤 Autor
Desenvolvido por Alvaro Ito

