arquivo = open(
    "/workspaces/trilha-python-dio/05 - Manipulação de arquivos/novo.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()
