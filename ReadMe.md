# Basic Blog Application using Flask

Einfache Blog-Anwendung mit Flask. Blog-Posts werden in einer JSON-Datei gespeichert und auf der Startseite angezeigt.

## Voraussetzungen

- Python 3
- Flask

## Installation

```bash
pip install -r requirements.txt
```

## Starten

```bash
python app.py
```

Die App läuft unter **http://localhost:5000/**.

## Projektstruktur

- `app.py` – Flask-App und Index-Route
- `data/blog_posts.json` – Speicher für Blog-Posts (author, title, content, id)
- `templates/index.html` – Startseite mit Liste aller Posts
- `static/style.css` – Stylesheet