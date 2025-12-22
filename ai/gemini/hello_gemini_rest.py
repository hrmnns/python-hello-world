"""
Minimaler Beispiel-Client für die Gemini Developer API (REST).

Dieses Skript zeigt den direkten Zugriff auf die Gemini API
über einen einfachen HTTP-POST-Aufruf ohne Verwendung des
offiziellen SDK. Es nutzt die Umgebungsvariable `GEMINI_API_KEY`,
sendet einen einfachen Text-Prompt an ein Gemini-Modell
und gibt die Antwort unverändert in der Konsole aus.

Der Fokus liegt auf technischer Nachvollziehbarkeit:
- expliziter Request-Aufbau
- keine Abstraktion durch SDKs
- direkter Blick auf Request- und Response-Struktur

Das Beispiel ist bewusst minimal gehalten und dient
primär zu Lern-, Vergleichs- und Debugging-Zwecken,
nicht als produktionsreifer API-Client.
"""

import os
import requests

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-2.5-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

payload = {
    "contents": [
        {"parts": [{"text": "Schreibe einen kurzen, sachlichen Absatz über IT-Governance."}]}
    ]
}

r = requests.post(
    URL,
    headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
    json=payload,
    timeout=60,
)
r.raise_for_status()

data = r.json()
print(data["candidates"][0]["content"]["parts"][0]["text"])
