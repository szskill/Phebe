import json
import random
import requests
from pathlib import Path


def random_fact():
    factfile = Path("facts.json")
    if not factfile.exists():
        facts = requests.get(
            "https://randomwordgenerator.com/json/facts.json",
            headers={
                "referrerPolicy": "strict-origin-when-cross-origin",
            },
        ).json()["data"]
        factfile.write_text(json.dumps(facts))
    facts = json.loads(factfile.read_text())
    fact = random.choice(facts)
    text = fact["fact"]
    source = fact["source_url"]
    return text, source


text, source = random_fact()
print(text)
print("From: " + source)
