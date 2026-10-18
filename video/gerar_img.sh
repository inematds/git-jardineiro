#!/usr/bin/env bash
# uso: gerar_img.sh <nome> "<cena>" [texto]   -> media/<nome>.png (Codex image_gen pela assinatura)
set -u
cd "$(dirname "$0")"
nome=$1; cena=$2; texto=${3:-}
mkdir -p media logs
rm -f "media/$nome.png"
ESTILO="Ilustração em aquarela com contorno fino de nanquim, estilo livro ilustrado sofisticado, traço limpo e detalhado. \
Luz de dia NEUTRA e fria-clara (nada de tom amarelado, dourado, sépia ou pôr do sol), céu azul claro, verdes frescos, flores roxas, \
rosas e brancas. Personagem fixo em todas as cenas: jardineiro de uns 45 anos, barba curta grisalha, chapéu de palha, camisa \
clara de manga dobrada, avental verde-escuro. Composição horizontal 16:9, assunto principal centralizado com respiro nas bordas."
if [ -n "$texto" ]; then
  REGRA="Escreva DENTRO da arte, grande, legível e com a grafia EXATA (português, com acentos), só este texto: $texto. Nenhum outro texto."
else
  REGRA="SEM NENHUM TEXTO: nada de letras, palavras, números, placas ou etiquetas escritas."
fi
pedido="Use sua ferramenta de geração de imagem (image_gen) para criar UMA imagem no maior formato HORIZONTAL (paisagem) disponível \
e salve o PNG em media/$nome.png dentro deste diretório. Não edite nenhum outro arquivo.

$ESTILO

Cena: $cena

$REGRA"
timeout 900 codex exec --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox - <<<"$pedido" > "logs/img-$nome.log" 2>&1
if [ -s "media/$nome.png" ]; then
  python3 ~/projetos/refazvideo/ferramentas/cor_neutra.py corrigir "media/$nome.png"
  echo "OK $nome"
else
  echo "FALHOU $nome (ver logs/img-$nome.log)"
fi
