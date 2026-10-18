# Git é um jardim

[![Git é um jardim](guia/assets/banner.jpg)](https://inematds.github.io/git-jardineiro/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

Este é um guia grátis que explica o Git usando a história de um jardineiro. O Git é a ferramenta que guarda cada versão de um projeto, como fotos de um jardim tiradas ao longo do tempo. Serve para quem programa, para quem trabalha com agentes de IA e para quem só quer parar de perder arquivos. Aqui você aprende seis comandos (clone, commit, branch, worktree, merge e push), cada um com um desenho, uma explicação simples e os comandos prontos para copiar. Para praticar, basta ter o Git instalado.

## 📖 Guia de uso

Guia completo (landing + 6 páginas explicativas): **https://inematds.github.io/git-jardineiro/guia/**

## 🎬 Vídeos

- Explicativo 16:9 (3 min): https://github.com/inematds/git-jardineiro/releases/download/video-v1.0.0/git-jardineiro-16x9.mp4
- Reel 9:16 (31 s): https://github.com/inematds/git-jardineiro/releases/download/video-v1.0.0/git-jardineiro-reel.mp4
- Players no guia: https://inematds.github.io/git-jardineiro/guia/#video

O roteiro e o roteiro visual estão em `video/`.

## Os 6 passos

1. **Clone** — Trazer o jardim pra casa: O clone copia o projeto e toda a história dele para o seu computador. (https://inematds.github.io/git-jardineiro/guia/clone/)
2. **Commit** — Tirar a foto do jardim: Edite, escolha o que entra e tire a foto. O commit salva no seu computador. (https://inematds.github.io/git-jardineiro/guia/commit/)
3. **Branch** — Testar uma ideia nova: Branch é uma etiqueta que anda junto com os seus commits novos. (https://inematds.github.io/git-jardineiro/guia/branch/)
4. **Worktree** — Dois canteiros ao mesmo tempo: Worktree é outra pasta do mesmo projeto, aberta em outra branch. (https://inematds.github.io/git-jardineiro/guia/worktree/)
5. **Merge** — Juntar as mudanças: Merge junta duas histórias num commit novo. (https://inematds.github.io/git-jardineiro/guia/merge/)
6. **Push** — Compartilhar com a equipe: Push leva os seus commits para o remoto. Agora a equipe pode pegar. (https://inematds.github.io/git-jardineiro/guia/push/)

| | |
|---|---|
| `git clone <url> jardim` | trazer o projeto e a história para o seu computador |
| `git status` | ver o que mudou e o que está na bandeja |
| `git add .` | pôr as mudanças na bandeja (área de preparo) |
| `git commit -m "frase"` | tirar a foto: salvar a versão no seu computador |
| `git switch -c flores` | criar a etiqueta flores e trabalhar nela |
| `git worktree add ../jardim-main main` | abrir outra pasta, em outra branch |
| `git merge flores` | juntar a branch flores na branch atual |
| `git push origin main` | levar as suas fotos para a estufa |
| `git fetch` | baixar a história nova da estufa, sem juntar |
| `git pull` | baixar e já juntar na sua branch |

## Para editar o guia

O texto mora em `src/<idioma>.json`; o HTML sai de `python3 src/build.py`.

Projetos e cursos gratuitos: https://inema.club
