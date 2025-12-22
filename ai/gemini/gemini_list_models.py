"""
gemini_list_models.py

Kleines Hilfsskript zur Auflistung aller über die Gemini Developer API
verfügbaren Modelle.

Das Skript fragt die Google-GenerativeAI-API nach allen aktuell
zugänglichen Modellen und gibt deren Namen in der Konsole aus.
Es dient als technisches Orientierungswerkzeug, um:

- verfügbare Modellnamen und Versionen zu identifizieren
- geeignete Modelle für Experimente oder Drift-Tests auszuwählen
- die tatsächliche Modellverfügbarkeit (z. B. Free Tier) zu prüfen
- Konfigurationen für weitere Skripte vorzubereiten

Ziel ist Transparenz über das aktuell nutzbare Modellangebot,
nicht eine vollständige Modell- oder Capability-Dokumentation.

Voraussetzungen:
- Umgebungsvariable `GEMINI_API_KEY` ist gesetzt
- Python-Paket `google-generativeai` ist installiert

Aufruf:
    python gemini_list_models.py

Ausgabe:
    Liste der verfügbaren Modellnamen (eine Zeile pro Modell)
"""


import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

for m in models:
    print(m.name)