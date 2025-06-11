import csv

def ler_csv_e_mostrar(arquivo_csv):
    try:
        with open(arquivo_csv, mode='r', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile, delimiter=';')

            for linha in leitor:
                print(f"Nome: {linha['nome-completo']}")
                print(f"Endereço: {linha['endereco']}")
                print(f"CEP: {linha['cep']}")
                print(f"Data de Nascimento: {linha['data-nascimento']}")
                print(f"Sexo: {linha['sexo']}")
                print('-' * 50)

    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

ler_csv_e_mostrar("file.csv")

