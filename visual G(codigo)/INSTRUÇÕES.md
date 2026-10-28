# Configuração do FitLens

## Iniciar o site

1. Configure o MySQL e crie as tabelas e os dados iniciais:

   ```bash
   python setup_db.py
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:

   ```bash
   python app.py
   ```

4. Abra **http://localhost:5000**. O Flask serve a página principal (`index.html`) e a API; não é necessário iniciar um segundo servidor HTTP.

## Páginas

| Endereço | Conteúdo |
|---|---|
| `/` | Site FitLens |
| `/admin/login` | Acesso administrativo |
| `/admin/dashboard` | Painel administrativo (requer login) |

O arquivo `projeto fitleean.html` é uma versão anterior; use a página servida em `/` para acessar os recursos atuais.

## Rotas da API

| Rota | Método | Função |
|---|---|---|
| `/planos` | GET | Lista os planos |
| `/unidades` | GET | Lista as unidades |
| `/clientes` | GET | Lista os cadastros usados na página principal |
| `/matricula` | POST | Cadastra uma matrícula |
| `/matricula/<id_cliente>` | PUT / DELETE | Atualiza ou exclui uma matrícula |
| `/franquia` | POST | Registra interesse em franquia |

## Problemas comuns

- **Erro de conexão com o banco:** confira se o MySQL está em execução e se as configurações em `conexao.py` correspondem ao seu ambiente.
- **Dependência ausente:** execute `pip install -r requirements.txt` no ambiente Python usado para iniciar o Flask.
- **Dados não carregam:** confirme que o servidor Flask está em execução e consulte o terminal para verificar erros da API ou do banco.
