# Hello World in Python mit VS Code und GitHub

Dieses Projekt wurde dazu genutzt, eine einfache **Hello World**-Anwendung in Python mit VS Code (Visual Studio Code) zu erstellen und anschließend in ein neues GitHub-Repository zu übertragen.

## Voraussetzungen

- Installiertes **Python** (https://www.python.org/downloads/)  
  → Bei der Installation **"Add Python to PATH"** aktivieren.
- Installiertes **Visual Studio Code** (https://code.visualstudio.com/)
- Installierte **Python-Erweiterung** in Visual Studio Code
- Installiertes **Git** (https://git-scm.com/downloads)
- GitHub-Account (https://github.com)

## Projekt in VS Code erstellen

1. Einen neuen Ordner anlegen, z. B.: ``python-hello-world``
2. Ordner in Visual Studio Code öffnen (`Datei → Ordner öffnen`)
3. Neue Datei `hello.py` anlegen
4. Inhalt einfügen: `print("Hello World")`

## Python-Interpreter in VS Code auswählen 
1. `Strg + Shift + P` drücken 
2. Python: Select Interpreter wählen
3. Python 3.x auswählen

## Programm ausführen
Entweder aus VS Code oder im Terminal via `python hello.py`
   
## Repository mit Git initialisieren
Im Terminal von Visual Studio Code ausführen:

```powershell
git init
git add .
git commit -m "Initial commit"
```

## Repository zu GitHub übertragen
Direkt über Visual Studio Code:

1. In VS Code auf Source Control (🔃) klicken
2. Button "Publish to GitHub" / "Zu GitHub veröffentlichen" auswählen
3. Repository-Namen vergeben
4. Privat oder Öffentlich auswählen

→ VS Code legt das Repository automatisch online an.

## Ergebnis
https://github.com/hrmnns/python-hello-world


