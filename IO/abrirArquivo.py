from os import path

def processar_arquivos(caminho, separador, campoAlterar, numAtl, id_row):
    novas_linhas = []
    print(caminho, separador, campoAlterar, numAtl, id_row)
    with open(caminho, "r") as f:
        for rows in f:
            dados = rows.lstrip("|").strip().split(separador)

            if dados[0] == id_row:
                if campoAlterar < len(dados):
                    dados[campoAlterar] = str(numAtl)
                nova_linha = "|" + separador.join(dados)
                novas_linhas.append(nova_linha)
                
            else:
                novas_linhas.append(rows.strip())
        
    caminho_saida = path.abspath("ArquivoFormatado.txt")

    with open(caminho_saida, "w") as f:
        f.write("\n".join(novas_linhas))

    return caminho_saida
