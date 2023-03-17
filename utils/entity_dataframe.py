import pandas as pd


def create_df():
    entities = {
        "PERSON":"Personen",
        "ORG":"Bedrijven, agentschappen, instellingen, etc.",
        "ORDINAL":"'Eerste', 'Tweede', etc.",
        "CARDINAL":"Cijfers die niet onder een ander type vallen.",
        "QUANTITY":"Metingen, zoals gewicht of afstand.",
        "DATE":"Absolute of relatieve datums of perioden.",
        "TIME":"Tijd kleiner dan een dag.",
        "PERCENT":"Percentage, inclusief %.",
        "NORP":"Nationaliteiten of religieuze of politieke groeperingen.",
        "FAC":"Gebouwen, luchthavens, snelwegen, bruggen, etc.",
        "GPE":"Landen, steden, staten.",
        "LOC":"Non-GPE-locaties, bergen, wateren.",
        "PRODUCT":"Voorwerpen, voertuigen, voedsel, etc. (Geen services.)",
        "EVENT":"Genoemde orkanen, veldslagen, oorlogen, sportevenementen, etc.",
        "WORK_OF_ART":"Titels van boeken, liedjes, etc.",
        "LAW":"Genoemde documenten omgezet in wetten.",
        "LANGUAGE":"Elke benoemde taal.",
        "MONEY":"Geldwaarden, inclusief eenheid."
    }
    return pd.DataFrame({'Entiteiten': entities.keys(), 'Uitleg': entities.values()})