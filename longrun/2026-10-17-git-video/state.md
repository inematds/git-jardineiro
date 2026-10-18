# Estado (17/10/2026 21:20)
- FEITO: repo inematds/git-jardineiro público, guia PT/EN/ES (landing + 6 páginas) via src/build.py, push (Pages Actions).
- FEITO: 9 ilustrações do vídeo em ~/projetos/output/explica-git-jardineiro/media/ (Codex, cor neutra); roteiro/pt.json (9 cenas, 3413 chars, 1 bloco); storyboard preview/storyboard.html; prepare v1 ok (v1/blocos/pt-b01.txt).
- FEITO: r7e edicoes/2026-10-17-git-jardim (roteiro + 7 imagens; imagem 2 sendo refeita: saiu mulher).
- ESPERANDO: "pode fazer" do Nei para o HeyGen (vídeo ~4,3 min + reel ~40 s). Sem isso, nada de avatar.
- PRÓXIMO: APROVADO_HEYGEN nos dois → heygen-studio.mjs (bloco pt-b01) + reel7etapas fazer → render v1 → visual v2 → render → src/videos.json + release → portal + Telegram INEMA.DEV.

## 17/10 22:15
- APROVADO pelo Nei ("pode gerar e me mande no v3 e coloque no projeto"). Vídeo enviado: HeyGen 33793dad8fcb454199e385ee87a10137 (manifest submitted). Reel: reel7etapas.py avatar rodando (pending).
- Visual v2 pronto: output/explica-git-jardineiro/visual/pt-b01.json (gerar_visual.py; deixas OK; validar_visual OK).
- Em fundo: baixa_blocos.sh (vídeo) e cadeia avatar→fazer (reel).
- Depois: render v1 (produce_blocks + wait_assembly) → v2 (setup_output, build_block 1 --strict, run_lane, assemble) → 720p → bot v3 (vídeo + reel) → release video-v1.0.0 no repo + src/videos.json + build + push → portal + Telegram INEMA.DEV.

## 17/10 23:45 — quase fechado
- Vídeo 16:9 (3min00s) renderizado, conferido em 24 quadros, no bot v3 (msg 1528) e na release video-v1.0.0; reel (31 s) aprovado nos portões, no bot v3 e na release.
- Guia com players (PT/EN/ES), push 3743e39. Portal d187a39 + inemabuscas 504c4e9 + inemapro a045f95/2540f63.
- Telegram INEMA.DEV: envio agendado para 23:57 (janela do sync).
- Sem YouTube (não pedido).
- 23:57 Telegram INEMA.DEV: tópico https://t.me/c/2389955773/7359 (15 msgs), MENU msg 7375.
