def create_prompt(
    home_team: str,
    away_team: str,
    event_prompt: list,
    home_team_possession: str,
    away_team_possession: str,
    winning_team: str,
    score_dict: dict
) -> str:
    prompt = (
        """ Schrijf een wedstrijd samenvatting met minimaal 100 woorden en met maximaal 200 woorden over de tekst.
    Schrijf in de stijl van een sport verslaggever.
    tekst: 
    Wedstrijd: """
    + home_team
    + """ speelt thuis tegen """
    + away_team
    + """.
    Events: """
    + "".join(event_prompt)
    + """
    Balbezit: """
    + home_team
    + """ Had """
    + home_team_possession
    + """ procent balbezit en """
    + away_team
    + """ had """
    + away_team_possession
    + """ procent balbezit.
    Eindstand: """
    + winning_team
    + """ heeft gewonnen met """
    + str(score_dict["Goals"][0])
    + """-"""
    + str(score_dict["Goals"][1])
    + """."""
    )
    return prompt