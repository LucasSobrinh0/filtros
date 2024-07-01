# Abrir o arquivo 'users' para leitura ('r' indica leitura)
with open('users', 'r') as arquivo:
    # Abrir o arquivo 'users_updated' para escrita ('a' indica acrescentar)
    with open('users_updated', 'a') as arquivo_atualizado:
        # Iterar sobre cada linha do arquivo
        for linha in arquivo:
            # Dividir a linha sempre que encontrar a sequência ',,+55'
            partes = linha.split(',,+55')

            # Iterar sobre cada parte resultante da divisão
            for parte in partes:
                # Filtrar apenas os caracteres que são dígitos
                numeros = ''.join(filter(str.isdigit, parte))

                # Verificar se há números após a separação
                if numeros:
                    # Escrever os números no arquivo 'users_updated'
                    arquivo_atualizado.write(numeros + '\n')
    
    print('Usuários atualizados')

