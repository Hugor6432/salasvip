# P1 - Sistema de Reserva de Salas

Sistema Django com CRUD de Salas e Reservas, com validação de conflito de horário.

## Requisitos

- Python 3.8+
- VS Code (opcional)

## Como Rodar (Windows)

### 1. Extrair ZIP

Descompacte `P1_Django_Reservas.zip`

### 2. Abrir no VS Code

File → Open Folder → Selecione `P1_Django_Reservas`

### 3. Abrir Terminal

Pressione: `Ctrl + `

Ou: Terminal → New Terminal

### 4. Executar Comandos (COPIAR E COLAR)

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 5. Acessar

Site: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

## Credentials

Username: admin
Password: admin123

## Para Parar

Pressione: Ctrl + C

## Funcionalidades P1

✅ CRUD Salas
✅ CRUD Reservas  
✅ Validação de Conflito de Horário
✅ Status: Pendente/Confirmada/Cancelada
✅ Recorrência: Única/Diária/Semanal/Mensal
✅ Admin Django
✅ Interface com Bootstrap
