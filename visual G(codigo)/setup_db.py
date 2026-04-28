import mysql.connector
from mysql.connector import Error

def criar_banco_dados():
    """Cria o banco de dados e popula com dados iniciais"""
    try:
        # Conecta ao MySQL sem especificar banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        cursor = conexao.cursor()
        
        # Cria o banco de dados
        cursor.execute("DROP DATABASE IF EXISTS fitlens_db")
        cursor.execute("CREATE DATABASE fitlens_db")
        cursor.execute("USE fitlens_db")
        
        # Cria tabelas
        print("Criando tabelas...")
        
        cursor.execute("""
            CREATE TABLE planos (
                id_plano INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                preco DECIMAL(10,2) NOT NULL,
                descricao TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE unidades (
                id_unidade INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(50),
                cidade VARCHAR(100),
                estado VARCHAR(50)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE clientes (
                id_cliente INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                telefone VARCHAR(20),
                plano_id INT,
                FOREIGN KEY (plano_id) REFERENCES planos(id_plano)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE franquias (
                id_franquia INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                telefone VARCHAR(20),
                cidade_interesse VARCHAR(100)
            )
        """)
        
        # Insere dados iniciais
        print("Inserindo dados iniciais...")
        
        cursor.execute("""
            INSERT INTO planos (nome, preco, descricao) VALUES
            ('Plano Base', 115.00, 'Acesso completo à musculação, suporte dos professores, ambiente climatizado'),
            ('Plano Plus', 150.00, 'Tudo do Plano Base + Avaliação física mensal + Acesso a aulas especiais'),
            ('Plano Premium', 200.00, 'Tudo do Plus + Personal Trainer + Suplementação')
        """)
        
        cursor.execute("""
            INSERT INTO unidades (nome, cidade, estado) VALUES
            ('Unidade Betim', 'Betim', 'MG'),
            ('Unidade Belo Horizonte', 'Belo Horizonte', 'MG'),
            ('Unidade Contagem', 'Contagem', 'MG')
        """)
        
        conexao.commit()
        cursor.close()
        conexao.close()
        
        print("✓ Banco de dados criado com sucesso!")
        print("✓ Base de dados: fitlens_db")
        print("✓ Usuário: root")
        print("✓ Senha: 1234")
        
    except Error as e:
        print(f"✗ Erro ao criar banco de dados: {e}")

if __name__ == "__main__":
    criar_banco_dados()
