"""
Minimaler technischer Referenzfall: JSON-Konfiguration einlesen und auswerten.

Das Skript zeigt bewusst nur die Kernschritte (lesen, interpretieren, ausgeben)
und verzichtet auf Frameworks oder Zusatzlogik, um als klarer Startpunkt
für ähnliche Konfigurationsfälle zu dienen.
"""

from __future__ import annotations

import json
from pathlib import Path


def load_config(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def format_message(greeting: str, features: list[str]) -> str:
    message = greeting
    if "uppercase" in features:
        message = message.upper()
    if "exclaim" in features:
        message = f"{message}!"
    return message


def main() -> None:
    config_path = Path(__file__).with_name("sample_config.json")
    config = load_config(config_path)

    greeting = str(config.get("greeting", "Hallo Welt"))
    repeat = int(config.get("repeat", 1))
    features = list(config.get("features", []))

    message = format_message(greeting, features)

    for index in range(repeat):
        print(f"{index + 1}/{repeat}: {message}")


if __name__ == "__main__":
    main()
