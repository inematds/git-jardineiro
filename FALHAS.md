# FALHAS — git-jardineiro

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 17/10/2026 | `enrichment.json` do PRO regravado com `indent=2` (push de 212 mil linhas) | gravar compacto (`separators=(",",":")`) e olhar `git diff --stat` antes do publica.sh | prompt |
| 17/10/2026 | laço de espera do reel nunca saía: `pgrep -f "<cmd>"` achava o próprio bash que continha o texto | esperar pelo arquivo (`avatar.mp4`) ou pelo PID, nunca `pgrep -f` com o texto do próprio laço | prompt |
| 17/10/2026 | matei o http.server de outra sessão (porta 8791 ocupada) | porta livre (bind 0) e conferir `/proc/<pid>/cwd` antes de matar | prompt |
| 17/10/2026 | imagem 2 do reel saiu com uma mulher no lugar do jardineiro | descrever a pessoa por completo (HOMEM, idade, barba) em toda `cena` | prompt |
