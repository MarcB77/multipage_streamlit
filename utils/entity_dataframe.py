import pandas as pd


def create_df():
    entities = {
        "PERSON":"Personen",
        "ORG":"Bedrijven, agentschappen, instellingen, enz.",
        "ORDINAL":"'eerste', 'tweede', enz.",
        "CARDINAL":"Cijfers die niet onder een ander type vallen.",
        "QUANTITY":"Metingen, zoals gewicht of afstand.",
        "DATE":"Absolute of relatieve datums of perioden.",
        "TIME":"Tijd kleiner dan een dag.",
        "PERCENT":"Percentage, inclusief %.",
        "NORP":"Nationaliteiten of religieuze of politieke groeperingen.",
        "FAC":"Gebouwen, luchthavens, snelwegen, bruggen, enz.",
        "GPE":"Landen, steden, staten.",
        "LOC":"Non-GPE-locaties, bergen, wateren.",
        "PRODUCT":"Voorwerpen, voertuigen, voedsel, enz. (Geen services.)",
        "EVENT":"Genoemde orkanen, veldslagen, oorlogen, sportevenementen, enz.",
        "WORK_OF_ART":"Titels van boeken, liedjes, enz.",
        "LAW":"Genoemde documenten omgezet in wetten.",
        "LANGUAGE":"Elke benoemde taal.",
        "MONEY":"Geldwaarden, inclusief eenheid."
    }
    return pd.DataFrame.from_dict(entities)