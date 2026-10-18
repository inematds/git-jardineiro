# Git es un jardín

[![Git es un jardín](guia/assets/banner-es.jpg)](https://inematds.github.io/git-jardineiro/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Esta es una guía gratuita que explica Git con la historia de un jardinero. Git es la herramienta que guarda cada versión de un proyecto, como fotos de un jardín tomadas a lo largo del tiempo. Sirve para quien programa, para quien trabaja con agentes de IA y para quien solo quiere dejar de perder archivos. Aquí aprenderás seis comandos (clone, commit, branch, worktree, merge y push), cada uno con un dibujo, una explicación sencilla y los comandos listos para copiar. Para practicar, basta con tener Git instalado.

## 📖 Guía de uso

Guía completa (landing + 6 páginas explicativas): **https://inematds.github.io/git-jardineiro/guia/es/**

## 🎬 Videos

- Explicativo 16:9 (3 min, en portugués): https://github.com/inematds/git-jardineiro/releases/download/video-v1.0.0/git-jardineiro-16x9.mp4
- Reel 9:16 (31 s, en portugués): https://github.com/inematds/git-jardineiro/releases/download/video-v1.0.0/git-jardineiro-reel.mp4
- Reproductores en la guía: https://inematds.github.io/git-jardineiro/guia/es/#video

El guion y el guion visual están en `video/`.

## Los 6 pasos

1. **Clone** — Traer el jardín a casa: Clone copia el proyecto y toda su historia en tu computadora. (https://inematds.github.io/git-jardineiro/guia/es/clone/)
2. **Commit** — Tomar la foto del jardín: Edita, elige qué incluir y toma la foto. Commit la guarda en tu computadora. (https://inematds.github.io/git-jardineiro/guia/es/commit/)
3. **Branch** — Probar una idea nueva: Branch es una etiqueta que avanza junto con tus nuevos commits. (https://inematds.github.io/git-jardineiro/guia/es/branch/)
4. **Worktree** — Dos parcelas al mismo tiempo: Worktree es otra carpeta del mismo proyecto, abierta en otra branch. (https://inematds.github.io/git-jardineiro/guia/es/worktree/)
5. **Merge** — Unir los cambios: Merge une dos historias en un commit nuevo. (https://inematds.github.io/git-jardineiro/guia/es/merge/)
6. **Push** — Compartir con el equipo: Push lleva tus commits al remoto. Ahora el equipo puede obtenerlos. (https://inematds.github.io/git-jardineiro/guia/es/push/)

| | |
|---|---|
| `git clone <url> jardin` | traer el proyecto y su historia a tu computadora |
| `git status` | ver qué cambió y qué está en la bandeja |
| `git add .` | poner los cambios en la bandeja (área de preparación) |
| `git commit -m "frase"` | tomar la foto: guardar la versión en tu computadora |
| `git switch -c flores` | crear la etiqueta flores y trabajar en ella |
| `git worktree add ../jardin-main main` | abrir otra carpeta, en otra branch |
| `git merge flores` | unir la branch flores con la branch actual |
| `git push origin main` | llevar tus fotos al invernadero |
| `git fetch` | descargar la nueva historia del invernadero, sin unirla |
| `git pull` | descargar y unirla enseguida con tu branch |

## Para editar la guía

El texto vive en `src/<idioma>.json`; el HTML sale de `python3 src/build.py`.

Proyectos y cursos gratuitos: https://inema.club
