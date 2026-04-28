## 🔧 GUIA DE CONFIGURAÇÃO - FitLens Academy

### ✅ PASSO 1: Configure o MySQL e o Banco de Dados

1. **Abra o terminal Python do VS Code** (já está configurado na sua lista)
2. Execute o script de criar banco de dados:
   ```bash
   python setup_db.py
   ```

Isso vai:
- ✓ Criar o banco de dados `fitlens_db`
- ✓ Criar as tabelas (planos, unidades, clientes, franquias)
- ✓ Popular com dados iniciais

### ✅ PASSO 2: Instale as dependências Python

```bash
pip install flask flask-cors mysql-connector-python
```

### ✅ PASSO 3: Inicie o servidor Flask

```bash
python app.py
```

Você verá:
```
 * Running on http://localhost:5000
```

### ✅ PASSO 4: Abra o site

1. Abra seu navegador
2. Vá para: `http://localhost:5000`
3. ❌ **Isso vai dar erro!** Você precisa servir o HTML por HTTP

### ✅ PASSO 5: Serve o HTML (Em outro terminal)

Abra um **segundo terminal** PowerShell e execute:

```bash
python -m http.server 8000
```

Agora acesse: `http://localhost:8000/projeto%20fitleean.html`

---

## 📋 O que cada arquivo faz:

| Arquivo | Função |
|---------|--------|
| `app.py` | Backend Flask com 4 rotas de API |
| `conexao.py` | Configuração de conexão com MySQL |
| `setup_db.py` | Cria e popula o banco de dados |
| `projeto fitleean.html` | Frontend com integrações JavaScript |

---

## 🔗 Rotas da API (Backend)

| Rota | Método | O quê faz |
|------|--------|----------|
| `/planos` | GET | Lista todos os planos |
| `/unidades` | GET | Lista todas as unidades |
| `/matricula` | POST | Cadastra novo cliente |
| `/franquia` | POST | Registra interesse em franquia |

---

## 🧪 Testando a Integração

Acesse a página no navegador e teste:
1. **Planos** - Devem aparecer da linha: "Plano Base", "Plano Plus", "Plano Premium"
2. **Unidades** - Devem aparecer: "Unidade Betim", "Belo Horizonte", "Contagem"
3. **Formulário de Franquia** - Preencha e clique em "Enviar Interesse"

---

## 🐛 Se der erro:

### Erro: "Connection refused"
- ✓ MySQL está rodando?
- ✓ A senha é mesmo "1234"?

### Erro: "Module not found"
- ✓ Instalou tudo com `pip install`?

### Dados não aparecem no site
- ✓ O banco de dados foi criado com `python setup_db.py`?
- ✓ Os dois servidores (Flask + HTTP) estão rodando?
- ✓ Você usou a URL correta no navegador?

---

## 📱 Links importantes:

- **Backend**: http://localhost:5000
- **Frontend**: http://localhost:8000/projeto%20fitleean.html
- **API de Planos**: http://localhost:5000/planos
- **API de Unidades**: http://localhost:5000/unidades
