#!/usr/bin/env python3
"""Roteiro visual v2 do vídeo git-jardineiro (1 bloco, 9 cenas) -> visual/pt-b01.json.
Confere se cada deixa (at / *_at) existe, em ordem, na fala da própria cena."""
import json, re, sys, unicodedata
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
M = str(OUT / "media") + "/"
rot = json.loads((OUT / "roteiro/pt.json").read_text())


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s).split())


def img(nome, at, label, focus=(0.5, 0.5), zoom=(1.0, 1.06), prev=None, **kw):
    s = {"type": "media", "at": at, "src": M + nome, "focus": list(focus), "zoom": list(zoom), "label": label, "calm": True}
    if prev:
        s.update(cont=True, **{"from": {"focus": list(prev[0]), "zoom": prev[1]}})
    s.update(kw)
    return s


def node(i, label, col, row, at, icon=None):
    n = {"id": i, "label": label, "col": col, "row": row, "at": at}
    if icon:
        n["icon"] = icon
    return n


S = {}
S["1"] = {"header": False, "shots": [
    {"type": "hook", "at": "@start", "text": "Git explicado como um **jardim**", "src": M + "01-capa-hook.png"},
    {"type": "keyword", "at": "Esses seis comandos", "text": "6 comandos", "sub": "o **coração** do Git", "sub_at": "coração do Git"},
    img("02-dicionario.png", "pensar num jardim", "o Git é um **jardim**"),
    {"type": "timeline", "at": "Neste vídeo eu explico", "events": [
        {"label": "Clone", "sub": "trazer pra casa", "at": "trazer o jardim"},
        {"label": "Commit", "sub": "a foto", "at": "tirar a foto"},
        {"label": "Branch", "sub": "ideia nova", "at": "testar uma ideia"},
        {"label": "Worktree", "sub": "dois canteiros", "at": "dois canteiros"},
        {"label": "Merge", "sub": "juntar", "at": "juntar tudo"},
        {"label": "Push", "sub": "compartilhar", "at": "compartilhar com a equipe"}]},
    img("09-ciclo.png", "no fim eu mostro", "no fim: **o ciclo completo**"),
]}
S["2"] = {"shots": [
    {"type": "fields", "at": "Primeiro, o dicionário", "title": "Dicionário do jardineiro", "fields": [
        {"label": "Jardim", "value": "projeto", "at": "O jardim é"},
        {"label": "Plantas", "value": "arquivos", "at": "As plantas são"},
        {"label": "Foto", "value": "commit", "at": "Cada commit é"},
        {"label": "Etiqueta", "value": "branch", "at": "A branch é"},
        {"label": "Estufa", "value": "remoto (GitHub)", "at": "tem uma estufa"}]},
    img("02-dicionario.png", "repositório remoto", "a estufa = **repositório remoto**", focus=(0.62, 0.22), zoom=(1.15, 1.22)),
]}
S["3"] = {"shots": [
    img("03-clone.png", "Passo um", "**1 · Clone**"),
    img("03-clone.png", "vai até a estufa", "a estufa = **remoto**", focus=(0.2, 0.35), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    {"type": "terminal", "at": "O comando git clone", "title": "terminal", "lines": [
        {"type": "cmd", "text": "git clone <url-do-repo> jardim", "at": "git clone copia"},
        {"type": "out", "text": "Cloning into 'jardim'... done.", "at": "toda a história"},
        {"type": "cmd", "text": "cd jardim", "at": "aparece uma pasta"},
        {"type": "comment", "text": "# arquivos prontos pra editar", "at": "prontos pra editar"}]},
    img("03-clone.png", "Repare", "você mexe **na sua cópia**", focus=(0.78, 0.55), zoom=(1.15, 1.2)),
]}
S["4"] = {"shots": [
    img("04-commit.png", "Passo dois", "**2 · Commit**"),
    img("04-commit.png", "caminho de pedras", "editar = **plantar**", focus=(0.25, 0.7), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    {"type": "flow", "at": "Depois você escolhe", "nodes": [
        node("ed", "editar", 0, 1, "Depois você escolhe", "pencil"),
        node("add", "git add", 1, 1, "com git add", "check"),
        node("bd", "bandeja (preparo)", 2, 1, "numa bandeja", "box"),
        node("cm", "git commit", 3, 1, "Aí o git commit", "git"),
        node("hs", "histórico", 4, 1, "no seu histórico", "clock")],
     "edges": [{"from": "ed", "to": "add", "at": "com git add"}, {"from": "add", "to": "bd", "at": "numa bandeja"},
               {"from": "bd", "to": "cm", "at": "Aí o git commit"}, {"from": "cm", "to": "hs", "at": "no seu histórico"}]},
    {"type": "terminal", "at": "O git status", "title": "terminal", "lines": [
        {"type": "cmd", "text": "git status", "at": "O git status"},
        {"type": "cmd", "text": "git add .", "at": "o que mudou"},
        {"type": "cmd", "text": "git commit -m \"Adiciona o caminho\"", "at": "a qualquer momento"}]},
    {"type": "statement", "at": "E atenção", "text": "Commit **não envia** nada", "then": {"text": "salva **só no seu computador**", "at": "salva só no"}},
]}
S["5"] = {"shots": [
    img("05-branch.png", "Passo três", "**3 · Branch**"),
    img("05-branch.png", "Bateu uma ideia", "uma **ideia nova**", focus=(0.62, 0.22), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    {"type": "terminal", "at": "Com git switch", "title": "terminal", "lines": [
        {"type": "cmd", "text": "git switch -c flores", "at": "Com git switch"},
        {"type": "comment", "text": "# etiqueta nova: flores (HEAD → flores)", "at": "cria uma etiqueta"}]},
    {"type": "flow", "at": "Cada foto nova", "nodes": [
        node("A", "A · inicial", 0, 1, "Cada foto nova"),
        node("B", "B · main", 1, 1, "Cada foto nova"),
        node("D", "D · flores", 2, 2, "faz a etiqueta"),
        node("E", "E · flores", 3, 2, "andar junto")],
     "edges": [{"from": "A", "to": "B", "at": "Cada foto nova"}, {"from": "B", "to": "D", "at": "faz a etiqueta"},
               {"from": "D", "to": "E", "at": "andar junto"}]},
    img("05-branch.png", "Se a ideia", "não deu certo? **é só voltar**", focus=(0.5, 0.6), zoom=(1.05, 1.12)),
]}
S["6"] = {"shots": [
    img("06-worktree.png", "Passo quatro", "**4 · Worktree**"),
    img("06-worktree.png", "a cerca quebrou", "urgência: **a cerca**", focus=(0.82, 0.45), zoom=(1.18, 1.22), prev=((0.5, 0.5), 1.06)),
    {"type": "terminal", "at": "Em vez de largar", "title": "terminal", "lines": [
        {"type": "cmd", "text": "git worktree add ../jardim-main main", "at": "uma segunda pasta"},
        {"type": "cmd", "text": "cd ../jardim-main", "at": "na outra você"},
        {"type": "comment", "text": "# conserta a cerca na main", "at": "conserta a cerca"}]},
    {"type": "compare", "at": "As duas usam", "left": {"title": "jardim/ → flores", "at": "As duas usam", "tone": "neutral", "lines": [
        {"text": "plantando flores", "at": "mesma história"}, {"text": "bandeja própria", "at": "cada uma tem"}]},
     "right": {"title": "jardim-main/ → main", "at": "mesma história", "tone": "neutral", "lines": [
        {"text": "consertando a cerca", "at": "cada uma tem"}, {"text": "bandeja própria", "at": "própria bandeja"}]},
     "verdict": {"text": "um **agente de IA** numa pasta, você na outra", "at": "agente de IA"}},
]}
S["7"] = {"shots": [
    img("07-merge.png", "Passo cinco", "**5 · Merge**"),
    {"type": "terminal", "at": "Agora você volta", "title": "terminal", "lines": [
        {"type": "cmd", "text": "git switch main", "at": "volta pra main"},
        {"type": "cmd", "text": "git merge flores", "at": "roda git merge"}]},
    {"type": "flow", "at": "O Git junta", "nodes": [
        node("A", "A", 0, 1, "O Git junta"), node("B", "B", 1, 1, "O Git junta"), node("C", "C · cerca", 2, 1, "duas histórias"),
        node("D", "D · flores", 2, 2, "duas histórias"), node("E", "E · flores", 3, 2, "duas histórias"),
        node("M", "M · merge", 4, 1, "commit novo", "git")],
     "edges": [{"from": "A", "to": "B", "at": "O Git junta"}, {"from": "B", "to": "C", "at": "duas histórias"},
               {"from": "B", "to": "D", "at": "duas histórias"}, {"from": "D", "to": "E", "at": "duas histórias"},
               {"from": "C", "to": "M", "at": "commit novo"}, {"from": "E", "to": "M", "at": "liga os dois"}]},
    {"type": "steps", "at": "Às vezes as duas", "goal": "Conflito? **sem pânico**", "steps": [
        {"title": "escolha como fica", "at": "você escolhe"}, {"title": "git add", "at": "faz git add"},
        {"title": "git commit", "at": "e git commit"}], "done_at": "e pronto"},
    img("07-merge.png", "teste o jardim", "merge feito ≠ **merge testado**", focus=(0.5, 0.7), zoom=(1.12, 1.18)),
]}
S["8"] = {"shots": [
    img("08-push.png", "Passo seis", "**6 · Push**"),
    {"type": "terminal", "at": "O git push leva", "title": "terminal", "lines": [
        {"type": "cmd", "text": "git push origin main", "at": "O git push leva"},
        {"type": "out", "text": "main -> main", "at": "atualiza a branch"}]},
    img("08-push.png", "Agora a equipe", "a equipe **recebe**", focus=(0.72, 0.45), zoom=(1.15, 1.22)),
    {"type": "compare", "at": "o caminho de volta", "left": {"title": "git fetch", "at": "git fetch baixa", "tone": "neutral", "lines": [
        {"text": "só **baixa** a história", "at": "história nova da"}]},
     "right": {"title": "git pull", "at": "git pull baixa", "tone": "good", "lines": [
        {"text": "baixa **e junta**", "at": "já junta"}]}},
    {"type": "statement", "at": "Guarde esta frase", "text": "Commit salva **em casa**", "then": {"text": "Push **compartilha**", "at": "push compartilha", "replace": False}},
]}
S["9"] = {"shots": [
    img("09-ciclo.png", "Juntando tudo", "o **ciclo** de todo dia"),
    {"type": "timeline", "at": "você clona uma", "events": [
        {"label": "clone", "sub": "uma vez", "at": "clona uma vez"},
        {"label": "commit", "sub": "o tempo todo", "at": "tira fotos"},
        {"label": "branch", "sub": "cada ideia", "at": "testa ideias"},
        {"label": "worktree", "sub": "duas frentes", "at": "abre um worktree"},
        {"label": "merge", "sub": "juntar", "at": "junta com merge"},
        {"label": "push", "sub": "compartilhar", "at": "compartilha com push"}]},
    img("09-ciclo.png", "É o ciclo", "de quem programa **e de quem usa IA**", focus=(0.5, 0.6), zoom=(1.08, 1.15)),
    img("10-guia.png", "O guia completo", "**inema.club** · guia grátis", zoom=(1.0, 1.05)),
]}

# conferência das deixas
erros = []
for k, sc in S.items():
    fala = norm(rot[int(k) - 1]["speech"])
    for sh in sc["shots"]:
        def ver(v):
            if v in ("@start",) or v is None:
                return
            c, _, n = v.partition("#")
            if norm(c) not in fala:
                erros.append(f"cena {k}: deixa '{v}' não está na fala")
        def anda(o):
            if isinstance(o, dict):
                for kk, vv in o.items():
                    if (kk == "at" or kk.endswith("_at")) and isinstance(vv, str):
                        ver(vv)
                    else:
                        anda(vv)
            elif isinstance(o, list):
                for x in o:
                    anda(x)
        anda(sh)
for k, sc in S.items():
    t = rot[int(k) - 1]
    sc.setdefault("takeaway", t["takeaway"])
(OUT / "visual/pt-b01.json").write_text(json.dumps({"block": "pt-b01", "scenes": S}, ensure_ascii=False, indent=1))
print("\n".join(erros) or "deixas OK", "| cenas", len(S), "| shots", sum(len(s["shots"]) for s in S.values()))
sys.exit(1 if erros else 0)
