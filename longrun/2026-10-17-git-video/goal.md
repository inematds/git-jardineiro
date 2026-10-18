# Goal — git-video

- **Início:** 2026-10-17 · **Agente:** Claude Code
- **Tetos:** render/transcrição com `systemd-run --user --scope -p MemoryMax=16G -p MemorySwapMax=0`

## Resultado
Repo `inematds/git-jardineiro` com guia PT/EN/ES (Git explicado como um jardim) + player do vídeo; explicavideo v2 PT
(~5 min, avatar do Nei, ilustrações próprias + animações dos comandos) e um reel r7e que divulga o conteúdo;
publicados no portal e no Telegram INEMA.DEV.

## Critérios de pronto (verificáveis)

**Função**
- [ ] `ls ~/projetos/output/explica-git-jardineiro/v2/final/*-pt.mp4` → existe; `ffprobe` duração 240–420 s
- [ ] `build_block.py N --strict` em cada bloco → 0 warnings; `hyperframes check` sem `content_overlap`
- [ ] frame 0 (`ffmpeg -frames:v 1`) mostra a capa do ganho com texto legível (conferido em recorte 3×)
- [ ] `ls ~/projetos/reel7etapas/edicoes/*git-jardim*/build/video.mp4` → existe; `reel7etapas.py validar` → aprovado
- [ ] `curl -sI https://inematds.github.io/git-jardineiro/guia/` (e `/guia/en/`, `/guia/es/`) → 200
- [ ] portal: `grep -n git-jardineiro ~/projetos/portal/src/data/*.ts` → card do projeto + vídeo; push no origin
- [ ] Telegram INEMA.DEV: id do tópico gravado em `progress.md` + entrada no MENU

**Regressão**
- [ ] guia: `scrollWidth - innerWidth` = 0 de 390 a 1920 px, servido por HTTP; todas as imagens `naturalWidth > 0` em PT/EN/ES

**Limite**
- [ ] HeyGen só depois de `APROVADO_HEYGEN` com o OK do Nei; nenhuma API além das liberadas (GitHub, Telegram, HeyGen leitura)
- [ ] nenhum MP4 commitado (`git ls-files | grep -c mp4` → 0); autor dos commits = inematds
- [ ] imagens sem texto desenhado, exceto capa/hero (texto conferido)

**Teste rápido por ciclo:** `ferramentas/validar_visual.py` + `build_block.py --strict`
**Teste completo no final:** folha de 11 quadros do 16:9 + folhas do r7e + medição do guia
