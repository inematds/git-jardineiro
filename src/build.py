#!/usr/bin/env python3
"""Gera o guia (landing + 6 páginas explicativas) em PT/EN/ES a partir de src/<lang>.json.

  python3 src/build.py        -> guia/index.html, guia/<conceito>/index.html, guia/en/..., guia/es/...
O texto mora só nos JSON; o HTML, o CSS e os gráficos de commits saem daqui. Vídeos: src/videos.json (opcional).
"""
import html, json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SRC = RAIZ / "src"
SLUG = "git-jardineiro"
REPO = f"https://github.com/inematds/{SLUG}"
SITE = f"https://inematds.github.io/{SLUG}/guia/"
LANGS = ["pt", "en", "es"]
CSS = (SRC / "base.css.html").read_text()
EXTRA_CSS = """<style>
  .concepts{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  @media(max-width:820px){.concepts{grid-template-columns:1fr 1fr}} @media(max-width:540px){.concepts{grid-template-columns:1fr}}
  .cc{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;color:var(--txt);transition:border-color .2s,transform .2s}
  .cc:hover{border-color:var(--amb);transform:translateY(-2px)}
  .cc img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
  .cc .t{padding:14px 16px 16px} .cc h3{font-size:1.05rem;margin:.25em 0 .3em} .cc p{color:var(--mut);font-size:.9rem;margin:0}
  .ill{margin:0 0 26px;border-radius:16px;overflow:hidden;border:1px solid var(--line)} .ill img{width:100%;display:block}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:22px} @media(max-width:820px){.two{grid-template-columns:1fr}}
  .box{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px}
  .box h3{font-size:1rem;margin-bottom:.5em} .box p{color:var(--mut);margin:.2em 0 .8em}
  .tip{border-left:3px solid var(--amb);background:rgba(250,204,21,.08);padding:12px 16px;border-radius:0 10px 10px 0;margin:18px 0 0}
  .graph{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;overflow-x:auto}
  .graph svg{display:block;min-width:520px;width:100%;height:auto}
  .graph .n{opacity:0;animation:pop .45s ease-out forwards} .graph .e{stroke-dasharray:200;stroke-dashoffset:200;animation:draw .6s ease-out forwards}
  @keyframes pop{from{opacity:0;transform:scale(.6)}to{opacity:1;transform:scale(1)}} @keyframes draw{to{stroke-dashoffset:0}}
  @media(prefers-reduced-motion:reduce){.graph .n,.graph .e{animation:none;opacity:1;stroke-dashoffset:0}}
  table.cola{width:100%;border-collapse:collapse;font-size:.92rem} table.cola td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
  table.cola td:first-child{font-family:"JetBrains Mono",monospace;color:var(--amb2);white-space:nowrap} @media(max-width:600px){table.cola td:first-child{white-space:normal;overflow-wrap:anywhere}}
  .pager{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:34px}
  .vids{display:grid;grid-template-columns:2fr 1fr;gap:20px;align-items:start} @media(max-width:820px){.vids{grid-template-columns:1fr}}
  .vids video{width:100%;border-radius:14px;border:1px solid var(--line);background:#000;display:block}
  .vids .v916 video{max-width:360px;margin:0 auto}
  .vids h3{font-size:1rem;margin:0 0 .6em} .vids p{margin:.6em 0 0;font-size:.88rem}
  .bignum{font-family:Sora;font-weight:800;font-size:3.2rem;color:var(--amb);line-height:1}
</style>"""
COR = {"main": "#FACC15", "side": "#a78bfa", "remote": "#38bdf8"}


def esc(s):
    return html.escape(s, quote=False)


def grafico(g, txt):
    """SVG do histórico: main em cima, branch lateral embaixo; nós aparecem em sequência."""
    dx, x0, ym, ys = 110, 50, 50, 135
    pos, ordem = {}, []
    side = g.get("side", [])
    for i, n in enumerate(g["main"]):
        pos[n] = (x0 + i * dx, ym)
    if side:
        bx = pos[g["from"]][0]
        for i, n in enumerate(side):
            pos[n] = (bx + (i + 1) * dx * (0.9 if g.get("into") else 1), ys)
        if g.get("into"):
            pos[g["into"]] = (max(pos[side[-1]][0], pos[g["main"][-2]][0]) + dx, ym)
    w = max(p[0] for p in pos.values()) + 120
    h = ys + 60 if side else ym + 60
    if g.get("remote"):
        h += 70
    out, es, t = [], [], 0.0
    def edge(a, b, cor):
        nonlocal t
        (x1, y1), (x2, y2) = pos[a], pos[b]
        d = f"M{x1},{y1} L{x2},{y2}" if y1 == y2 else f"M{x1},{y1} C{(x1 + x2) / 2},{y1} {(x1 + x2) / 2},{y2} {x2},{y2}"
        es.append(f'<path class="e" d="{d}" stroke="{cor}" stroke-width="4" fill="none" style="animation-delay:{t:.2f}s"/>')
    def node(n, cor):
        nonlocal t
        x, y = pos[n]
        lab = esc(g["labels"].get(n, ""))
        out.append(f'<g class="n" style="animation-delay:{t:.2f}s;transform-origin:{x}px {y}px"><circle cx="{x}" cy="{y}" r="17" fill="{cor}"/>'
                   f'<text x="{x}" y="{y + 5}" text-anchor="middle" font-family="Sora" font-weight="800" font-size="15" fill="#1a1206">{n}</text>'
                   f'<text x="{x}" y="{y + 38}" text-anchor="middle" font-family="Inter" font-size="13" fill="currentColor" opacity=".75">{lab}</text></g>')
        t += 0.35
    main = g["main"][:-1] if g.get("into") else g["main"]
    for i, n in enumerate(main):
        if i:
            edge(main[i - 1], n, COR["main"])
        node(n, COR["main"])
    if side:
        edge(g["from"], side[0], COR["side"])
        for i, n in enumerate(side):
            if i:
                edge(side[i - 1], n, COR["side"])
            node(n, COR["side"])
    if g.get("into"):
        edge(main[-1], g["into"], COR["main"]); edge(side[-1], g["into"], COR["side"])
        node(g["into"], COR["main"])
    # rótulos das branches
    def tag(n, nome, cor, dy):
        x, y = pos[n]
        wl = 14 + 8.5 * len(nome)
        out.append(f'<g class="n" style="animation-delay:{t:.2f}s"><rect x="{x + 24}" y="{y - 13 + dy}" width="{wl}" height="24" rx="6" fill="none" stroke="{cor}" stroke-width="2"/>'
                   f'<text x="{x + 24 + wl / 2}" y="{y + 4 + dy}" text-anchor="middle" font-family="Sora" font-weight="600" font-size="13" fill="{cor}">{esc(nome)}</text></g>')
    tag(g["main"][-1], "main", COR["main"], -34)
    if side and not g.get("into"):
        tag(side[-1], g["side_name"], COR["side"], 34)
    if g.get("remote"):
        x = pos[g["main"][-1]][0]
        y = h - 32
        out.append(f'<g class="n" style="animation-delay:{t + .3:.2f}s"><path d="M{x},{ym + 22} L{x},{y - 14}" stroke="{COR["remote"]}" stroke-width="3" stroke-dasharray="6 6" fill="none"/>'
                   f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-family="Sora" font-weight="600" font-size="14" fill="{COR["remote"]}">{esc(txt["remote"])}</text></g>')
    return f'<svg viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-label="{esc(" → ".join(g["main"]))}" style="color:var(--txt)">{"".join(es + out)}</svg>'


def pre(cmds):
    linhas = []
    for c, r in cmds:
        if c.startswith("#"):
            linhas.append(f'<span class="c">{esc(c)}</span>')
        else:
            linhas.append(f'<span class="k">{esc(c)}</span>' + (f'  <span class="c"># {esc(r)}</span>' if r else ""))
    return "<pre>" + "\n".join(linhas) + "</pre>"


def pagina(d, lang, sub, corpo, titulo, desc, secoes):
    """sub = caminho dentro do idioma ('' ou 'clone/')."""
    prof = (0 if lang == "pt" else 1) + (1 if sub else 0)
    up = "../" * prof
    def em(l):  # link para a mesma página em outro idioma
        return up + ("" if l == "pt" else f"{l}/") + sub
    seletor = "".join(f'<a{" class=\"on\"" if l == lang else ""} href="{em(l) or "./"}">{l.upper()}</a>' for l in LANGS)
    alt = "".join(f'<link rel="alternate" hreflang="{"pt-BR" if l == "pt" else l}" href="{SITE}{"" if l == "pt" else l + "/"}{sub}">' for l in LANGS)
    home = up + ("" if lang == "pt" else f"{lang}/")
    links = "".join(f'<a class="sec" href="{home}#{a}">{esc(t)}</a>' for a, t in secoes)
    return f"""<!DOCTYPE html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{html.escape(desc)}">
{alt}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
{CSS}
{EXTRA_CSS}
</head>
<body>
<nav><div class="wrap">
  <a class="brand" href="{home or './'}"><span class="emoji">🌱</span> {esc(d['title'])}</a>
  <span class="sep">|</span>
  <span class="clubpro">
    <a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a>
    <span class="sep">-</span>
    <a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a>
  </span>
  <div class="links">
    {links}
    <span class="lang">{seletor}</span>
    <button class="tgl" id="themeToggle" aria-label="{esc(d['nav']['tema'])}" title="{esc(d['nav']['tema'])}">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">{esc(d['nav']['github'])}</a>
  </div>
</div></nav>
{corpo}
<footer>
  <div class="wrap">
    {"".join(f'<div class="pill">{esc(s)}</div>' for s in d['footer']['stack'])}
    <p style="margin-top:18px">{esc(d['title'])} · {esc(d['footer']['nota'])} ·
      <a href="{REPO}">inematds/{SLUG}</a> ·
      <a href="https://inema.club">INEMA.CLUB</a></p>
  </div>
</footer>
<script>
  (function(){{
    var KEY='{SLUG}-theme';
    var b=document.body, t=document.getElementById('themeToggle');
    try{{ if(localStorage.getItem(KEY)==='light'){{ b.classList.add('light'); t.textContent='☀️'; }} }}catch(e){{}}
    t.addEventListener('click',function(){{
      var light=b.classList.toggle('light');
      t.textContent=light?'☀️':'🌙';
      try{{ localStorage.setItem(KEY, light?'light':'dark'); }}catch(e){{}}
    }});
  }})();
</script>
</body>
</html>
"""


def construir(lang, videos):
    d = json.loads((SRC / f"{lang}.json").read_text())
    base = RAIZ / "guia" / ("" if lang == "pt" else lang)
    a0 = "assets/" if lang == "pt" else "../assets/"
    sfx = "" if lang == "pt" else f"-{lang}"
    nav = d["nav"]
    secoes = [("oque", nav["oque"]), ("passos", nav["passos"])] + ([("video", nav["video"])] if videos else []) + [("cola", nav["cola"])]
    o, f, cs = d["oque"], d["fluxo"], d["conceitos"]
    cards = "".join(f'<div class="card"><h3>{e} {esc(t)}</h3><p>{esc(x)}</p></div>' for e, t, x in o["cards"])
    flow = '<span class="arr">→</span>'.join(f'<span>{i + 1} · {esc(c["nome"])}</span>' for i, c in enumerate(cs))
    ccs = "".join(f'<a class="cc" href="{c["slug"]}/"><img src="{a0}{c["img"]}" alt="{html.escape(c["img_alt"])}" loading="lazy">'
                  f'<div class="t"><span class="chip">{esc(d["passo"])} {i + 1}</span><h3>{esc(c["nome"])} — {esc(c["titulo"])}</h3><p>{esc(c["resumo"])}</p></div></a>'
                  for i, c in enumerate(cs))
    vid = ""
    if videos:
        v = d["video"]
        vid = f"""<section id="video"><div class="wrap">
  <span class="chip">{esc(v['chip'])}</span>
  <h2>{esc(v['h2'])}</h2>
  <p class="sub">{esc(v['sub'])}</p>
  <div class="vids">
    <div><h3>{esc(v['longo'])}</h3><video controls preload="metadata" playsinline poster="{a0}{videos['poster']}"><source src="{videos['longo']}" type="video/mp4"></video>
      <p><a href="{videos['longo']}">{esc(v['baixar'])}</a>{f' · <a href="{videos["yt_longo"]}">YouTube</a>' if videos.get('yt_longo') else ''}</p></div>
    <div class="v916"><h3>{esc(v['reel'])}</h3><video controls preload="metadata" playsinline><source src="{videos['reel']}" type="video/mp4"></video>
      <p><a href="{videos['reel']}">{esc(v['baixar'])}</a>{f' · <a href="{videos["yt_reel"]}">YouTube</a>' if videos.get('yt_reel') else ''}</p></div>
  </div>
</div></section>"""
    cl = d["cola"]
    cola = "".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for a, b in cl["linhas"])
    h = d["hero"]
    corpo = f"""
<header class="hero" id="top">
  <div class="glow"></div>
  <div class="wrap">
    <div>
      <span class="chip">{esc(h['chip'])}</span>
      <h1>{h['h1']}</h1>
      <p class="lead">{esc(h['lead'])}</p>
      <div class="cta">
        <a class="btn" href="#passos">{esc(h['cta1'])}</a>
        <a class="btn ghost" href="{REPO}" target="_blank" rel="noopener">{esc(h['cta2'])}</a>
      </div>
    </div>
    <figure><img src="{a0}banner{sfx}.jpg" alt="{html.escape(h['alt'])}"></figure>
  </div>
</header>
<section id="resumo" class="resumo"><div class="wrap">
  <span class="chip">{esc(d['resumo_chip'])}</span>
  <p>{esc(d['resumo'])}</p>
</div></section>
<section id="oque"><div class="wrap">
  <span class="chip">{esc(o['chip'])}</span>
  <h2>{esc(o['h2'])}</h2>
  <p class="sub">{esc(o['sub'])}</p>
  <figure style="margin:0 0 26px;border-radius:16px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 80px -30px #000"><img src="{a0}banner-grade{sfx}.jpg" alt="{html.escape(o['alt_grade'])}" loading="lazy" style="width:100%;display:block"></figure>
  <div class="grid g3">{cards}</div>
  <figure class="ill" style="margin-top:26px"><img src="{a0}{o['img']}" alt="{html.escape(o['img_alt'])}" loading="lazy"></figure>
</div></section>
<section id="passos"><div class="wrap">
  <span class="chip">{esc(f['chip'])}</span>
  <h2>{esc(f['h2'])}</h2>
  <p class="sub">{esc(f['sub'])}</p>
  <div class="flow" style="margin-bottom:26px">{flow}</div>
  <div class="concepts">{ccs}</div>
</div></section>
{vid}
<section id="cola"><div class="wrap">
  <span class="chip">{esc(cl['chip'])}</span>
  <h2>{esc(cl['h2'])}</h2>
  <p class="sub">{esc(cl['sub'])}</p>
  <div class="box"><table class="cola">{cola}</table></div>
  <p class="tip"><strong>{esc(cl['frase'])}</strong></p>
  <figure class="ill" style="margin-top:26px"><img src="{a0}{d['fim']['img']}" alt="{html.escape(d['fim']['alt'])}" loading="lazy"></figure>
  <h3 style="margin-top:8px">{esc(d['fim']['h2'])}</h3><p class="mut">{esc(d['fim']['texto'])}</p>
</div></section>
"""
    base.mkdir(parents=True, exist_ok=True)
    (base / "index.html").write_text(pagina(d, lang, "", corpo, f"{d['title']} — {d['tagline']}", d["meta"], secoes))
    a1 = "../" + a0
    for i, c in enumerate(cs):
        ant = f'<a class="btn ghost" href="../{cs[i - 1]["slug"]}/">{esc(d["anterior"])} {esc(cs[i - 1]["nome"])}</a>' if i else f'<a class="btn ghost" href="../">{esc(nav["voltar"])}</a>'
        prox = f'<a class="btn" href="../{cs[i + 1]["slug"]}/">{esc(d["proximo"])} {esc(cs[i + 1]["nome"])} →</a>' if i + 1 < len(cs) else f'<a class="btn" href="../#cola">{esc(cl["h2"])} →</a>'
        corpo = f"""
<header class="hero" id="top" style="border-bottom:none"><div class="glow"></div>
  <div class="wrap" style="grid-template-columns:1fr;padding-bottom:20px">
    <div><span class="chip">{esc(d['passo'])} {i + 1} / {len(cs)} · {esc(c['nome'])}</span>
      <h1>{esc(c['nome'])}: <span class="amb">{esc(c['titulo'].lower())}</span></h1>
      <p class="lead" style="max-width:60ch">{esc(c['resumo'])}</p></div>
  </div>
</header>
<section style="padding-top:10px"><div class="wrap">
  <figure class="ill"><img src="{a1}{c['img']}" alt="{html.escape(c['img_alt'])}"></figure>
  <div class="two">
    <div class="box"><span class="chip">{esc(d['metafora'])}</span><p style="color:var(--txt);font-size:1.05rem;margin-top:.6em">{esc(c['metafora'])}</p></div>
    <div class="box"><span class="chip">{esc(d['na_pratica'])}</span>{''.join(f'<p>{esc(p)}</p>' for p in c['texto'])}</div>
  </div>
  <h3 style="margin:30px 0 12px">{esc(d['comandos'])}</h3>
  {pre(c['cmds'])}
  <p class="tip"><strong>{esc(d['dica'])}:</strong> {esc(c['dica'])}</p>
  <h3 style="margin:30px 0 12px">{esc(d['grafico'])}</h3>
  <div class="graph">{grafico(c['graph'], d['graph_txt'])}</div>
  <div class="pager">{ant}{prox}</div>
</div></section>
"""
        p = base / c["slug"]; p.mkdir(exist_ok=True)
        (p / "index.html").write_text(pagina(d, lang, c["slug"] + "/", corpo, f"{c['nome']} — {c['titulo']} · {d['title']}", c["resumo"], secoes))


if __name__ == "__main__":
    vf = SRC / "videos.json"
    videos = json.loads(vf.read_text()) if vf.exists() else None
    for l in LANGS:
        if (SRC / f"{l}.json").exists():
            construir(l, videos); print("ok", l)
