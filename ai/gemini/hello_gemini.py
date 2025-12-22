"""
Minimaler Beispiel-Client für die Gemini Developer API (Python SDK).

Dieses Skript demonstriert den kleinstmöglichen, nachvollziehbaren Einstieg
in die Nutzung von Gemini über das offizielle Google GenAI Python SDK.
Es liest einen API-Key aus der Umgebungsvariable `GEMINI_API_KEY`,
sendet einen einfachen Text-Prompt an ein Gemini-Modell
und gibt die textuelle Antwort in der Konsole aus.

Ziel dieses Beispiels ist nicht funktionale Vollständigkeit,
sondern Transparenz und Reproduzierbarkeit:
- kein Prompt-Framework
- keine Streaming-Logik
- keine Persistenz oder Fehlerbehandlung

Das Skript dient als technischer Referenz- und Startpunkt
für weiterführende Experimente (z. B. Prompt-Varianten,
Drift-Tests oder API-Vergleiche).
"""

from google import genai

def main() -> None:
    # Liest GEMINI_API_KEY automatisch aus der Umgebung
    client = genai.Client()

    prompt = "Gib mir bitte drei Stichpunkte, was ein CIO 2026 priorisieren sollte."
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print(resp.text)

if __name__ == "__main__":
    main()
