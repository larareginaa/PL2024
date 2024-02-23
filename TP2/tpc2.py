import sys
import re


def cabecalho(match):
    return f"<h{len(match.group(1))}>{match.group(2)}</h{len(match.group(1))}>"

def lista(match):
    return f"<ol>\n\t{"\n\t".join([i for i in match.group(1).split('\n')])}\n</ol>"


def conversor(md):
    
    md = re.sub(r'(#+) +(.+)', cabecalho, md) # Cabeçalhos   
    md = re.sub(r'\*\*(.+)\*\*', r'<b>\1</b>', md) # Negrito
    md = re.sub(r'\*(.+)\*', r'<i>\1</i>', md) # Itálico
    md = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', md, flags=re.MULTILINE) # Lista numerada
    md = re.sub(r'(<li>.+</li>)+', lista, md, flags=re.DOTALL | re.MULTILINE) # Lista numerada
    md = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', md) # Imagem
    md = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', md) # Link

    return md


if __name__ == "__main__":

    with open(sys.argv[1], 'r') as fr: html = conversor(fr.read())
    fr.close()

    with open(sys.argv[2], 'w') as fw: fw.write(html)
    fw.close()
