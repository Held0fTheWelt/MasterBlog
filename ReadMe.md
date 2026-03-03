# Basic Blog Application using Flask

Einfache Blog-Anwendung mit Flask. Blog-Posts werden in einer JSON-Datei gespeichert. Die App unterstützt Anzeigen, Hinzufügen, Bearbeiten, Löschen und Liken von Posts.

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

## Funktionen

| Route | Beschreibung |
|-------|--------------|
| `/` | Startseite – alle Blog-Posts mit Like-, Update- und Delete-Button |
| `/add` | Formular zum Anlegen eines neuen Posts (GET), Speichern per POST |
| `/update/<post_id>` | Formular zum Bearbeiten eines Posts (GET), Aktualisierung per POST |
| `/delete/<post_id>` | Post löschen, Weiterleitung zur Startseite |
| `/like/<id>` | Like-Zähler des Posts um 1 erhöhen, Weiterleitung zur Startseite |

## Projektstruktur

- `app.py` – Flask-App mit allen Routen (index, add, update, delete, like)
- `data/blog_posts.json` – Speicher für Blog-Posts (id, author, title, content, likes)
- `templates/index.html` – Startseite mit Liste aller Posts
- `templates/add.html` – Formular zum Anlegen eines Posts
- `templates/update.html` – Formular zum Bearbeiten eines Posts
- `static/style.css` – Stylesheet