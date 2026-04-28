import mysql.connector
from conexao import conectar

def exibir_tabela_formatada(colunas, dados):
    """Formata e exibe uma tabela em texto"""
    if not dados:
        return
    
    # Calcular largura das colunas
    larguras = [len(str(col)) for col in colunas]
    for linha in dados:
        for i, valor in enumerate(linha):
            larguras[i] = max(larguras[i], len(str(valor)))
    
    # Cabeçalho
    linha_sep = "+" + "+".join("-" * (l + 2) for l in larguras) + "+"
    print(linha_sep)
    print("| " + " | ".join(f"{col:<{larguras[i]}}" for i, col in enumerate(colunas)) + " |")
    print(linha_sep)
    
    # Dados
    for linha in dados:
        print("| " + " | ".join(f"{str(valor):<{larguras[i]}}" for i, valor in enumerate(linha)) + " |")
    print(linha_sep)

def visualizar_tabelas():
    """Exibe todos os dados das tabelas de forma organizada"""
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        
        # Tabelas a visualizar
        tabelas = ['planos', 'unidades', 'clientes', 'franquias']
        
        for tabela in tabelas:
            print("\n" + "="*80)
            print(f"📊 TABELA: {tabela.upper()}")
            print("="*80)
            
            # Buscar dados
            cursor.execute(f"SELECT * FROM {tabela}")
            colunas = [desc[0] for desc in cursor.description]
            dados = cursor.fetchall()
            
            if dados:
                print(f"\n✅ {len(dados)} registro(s) encontrado(s)\n")
                exibir_tabela_formatada(colunas, dados)
            else:
                print(f"\n⚠️  Nenhum dado na tabela {tabela}\n")
        
        cursor.close()
        conn.close()
        print("\n" + "="*80)
        print("✅ Visualização concluída!")
        print("="*80)
        
    except Exception as e:
        print(f"❌ Erro: {e}")

def contar_registros():
    """Mostra a quantidade de registros em cada tabela"""
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        
        print("\n" + "="*80)
        print("📈 CONTAGEM DE REGISTROS")
        print("="*80 + "\n")
        
        tabelas = ['planos', 'unidades', 'clientes', 'franquias']
        
        for tabela in tabelas:
            cursor.execute(f"SELECT COUNT(*) FROM {tabela}")
            count = cursor.fetchone()[0]
            print(f"  • {tabela:12} : {count:3} registro(s)")
        
        cursor.close()
        conn.close()
        print("\n" + "="*80 + "\n")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

def visualizar_tabela_especifica(nome_tabela):
    """Visualiza uma tabela específica"""
    
    try:
        conn = conectar()
        cursor = conn.cursor()
        
        print("\n" + "="*80)
        print(f"📊 TABELA: {nome_tabela.upper()}")
        print("="*80)
        
        cursor.execute(f"SELECT * FROM {nome_tabela}")
        colunas = [desc[0] for desc in cursor.description]
        dados = cursor.fetchall()
        
        if dados:
            print(f"\n✅ {len(dados)} registro(s) encontrado(s)\n")
            print(tabulate(dados, headers=colunas, tablefmt="grid"))
        else:
            print(f"\n⚠️  Nenhum dado na tabela\n")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    print("\n🎯 VISUALIZADOR DE DADOS - FITLENS")
    print("="*80)
    
    # Mostrar contagem
    contar_registros()
    
    # Mostrar todos os dados
    visualizar_tabelas()
