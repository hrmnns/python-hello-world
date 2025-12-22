# Gemini – Basis-Skripte

Dieses Verzeichnis enthält **minimale Python-Basisskripte für die Kommunikation mit Google Gemini**
über die **Gemini Developer API**.

Die Skripte dienen als **technische Einstiegspunkte und Referenzen**, um:
- den Zugriff auf Gemini herzustellen,
- verfügbare Modelle zu identifizieren,
- einfache Prompts über die API abzusetzen,
- Antworten reproduzierbar in der Konsole zu verarbeiten.

Der Fokus liegt auf **Transparenz, Nachvollziehbarkeit und Minimalität** –
nicht auf Feature-Vollständigkeit oder produktivem Einsatz.

## Zielsetzung des Verzeichnisses

Dieses Verzeichnis stellt eine **Grundlage für weitere Experimente** dar, z. B.:

- Prompt-Varianten und Prompt-Design
- Drift-Experimente und Modellvergleiche
- API-Tests und technische Evaluierungen
- Vergleich SDK ↔ REST
- Dokumentation des jeweils verfügbaren Modellangebots

Alle Skripte sind bewusst:
- klein gehalten
- gut lesbar
- ohne versteckte Abhängigkeiten
- ohne Persistenz oder komplexe Konfiguration

## Voraussetzungen

- Python 3.9 oder neuer
- Gesetzte Umgebungsvariable `GEMINI_API_KEY`
- Installierte Python-Abhängigkeiten

```bash
pip install -U google-generativeai
```

### API-Key setzen

**Windows (PowerShell):**
```powershell
setx GEMINI_API_KEY "DEIN_API_KEY"
```

**macOS / Linux:**
```bash
export GEMINI_API_KEY="DEIN_API_KEY"
```

## Enthaltene Skripte

### `hello_gemini.py`

Minimaler **Hello-World-Client** für Gemini unter Verwendung des
offiziellen Python SDK.

**Funktion:**
- Baut eine Verbindung zur Gemini API auf
- Sendet einen einfachen Text-Prompt
- Gibt die textuelle Antwort in der Konsole aus

**Aufruf:**
```bash
python hello_gemini.py
```

**Einsatzgebiet:**
- Schnellster Einstieg
- Funktionsprüfung der API
- Referenz für weitere Skripte


### `hello_gemini_rest.py`

Minimaler Zugriff auf die Gemini API **ohne SDK**, über einen
direkten HTTP-Request (REST).

**Funktion:**
- Expliziter Request-Aufbau
- Direkte Verarbeitung der API-Antwort
- Keine Abstraktion durch Client-Bibliotheken

**Aufruf:**
```bash
python hello_gemini_rest.py
```

**Einsatzgebiet:**
- Debugging
- Verständnis der API-Struktur
- Vergleich SDK ↔ REST
- Technische Dokumentation

### `gemini_list_models.py`

Hilfsskript zur **Auflistung aller aktuell verfügbaren Gemini-Modelle**.

**Funktion:**
- Abfrage der API nach allen zugänglichen Modellen
- Ausgabe der Modellnamen in der Konsole

**Aufruf:**
```bash
python gemini_list_models.py
```

**Einsatzgebiet:**
- Modellübersicht
- Auswahl geeigneter Modelle für Experimente
- Dokumentation der Modellverfügbarkeit zu einem bestimmten Zeitpunkt
- Vorbereitung von Drift- oder Vergleichstests

## Abgrenzung / Nicht-Ziele

Dieses Verzeichnis enthält **keine**:

- Prompt-Frameworks
- CLI-Tools oder Argument-Parser
- Streaming-Implementierungen
- Fehler- oder Retry-Logik
- Konfigurationsdateien
- Persistente Speicherung von Ergebnissen

Diese Aspekte sind bewusst ausgelagert und können
auf Basis dieser Skripte ergänzt werden.

## Einordnung

Die hier enthaltenen Skripte bilden den **technischen Unterbau**
für alle weiteren Arbeiten mit Gemini in diesem Projekt.

Sie sind als **stabile Referenz** gedacht, auf der
strukturierte Experimente, Vergleiche und Dokumentationen
aufbauen können.
