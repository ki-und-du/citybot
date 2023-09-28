# citybot (Arbeitstitel)

Achtung: diese erste Version stellt erstmal nur einen API-Endpoint zur Verfügung, der eine Antwort auf eine Frage liefert. Die Antwort wird von OpenAI generiert. Ansonsten kann das Programm noch nichts.

## Du hast den Code ausgecheckt - sehr gut! Aber was jetzt?
1. Benenne .env-example um in .env

2. Gehe in Deinen OpenAPI-Account und erzeuge Dir einen API-Key (https://platform.openai.com/account/api-keys). 

3. Füge ihn im .env file an die richtige Stelle ein.

4. Lege Dir in Python ein virtual environment an
`python -m venv venv`

5. Installiere alle benötigten Libraries aus dem requirements.txt file
`pip install -r requirements.txt`

6. Starte die Anwendung
`python main.py`

7. Nach ein paar Sekunden müsstest Du über http://127.0.0.1:8001/docs die API-Dokumentation sehen. Dort kannst Du auch gleich die API ausprobieren.

## Wie geht es weiter?
- Einrichtung einer öffentlichen URL für eine dev-sandbox
- Fertigstellen des automatischen Deployments für künftige Releases
- Aufsetzen eines Frontends
- Aufsetzen einer Datenbank
- Umsetzen weiterer User-Stories

## Du hast Fragen oder die Installation klappt bei Dir nicht?
Melde Dich einfach per Email oder Slack bei mir. Ich helfe Dir gerne weiter.