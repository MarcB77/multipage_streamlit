import pandas as pd
from prompt_utils.create_prompt import create_prompt


def goal_events(df: pd.DataFrame) -> list:
    """_summary_

    Args:
        df (pd.DataFrame): The original dataframe

    Returns:
        list: event_prompt
    """
    df_goals = df.query("EVENT_NAME == 'Goal'")
    goal_events = {
        "Team": df_goals.TEAM_NAME.values.tolist(),
        "Event period minute": df_goals.EVENT_PERIOD_MINUTE.values.tolist(),
    }

    event_prompt = [
        str(team)
        + " scoorde in minuut "
        + str(goal_events["Event period minute"][index])
        + ". "
        for index, team in enumerate(goal_events["Team"])
    ]
    return event_prompt


def get_home_away_team(
    df: pd.DataFrame,
) -> tuple[str, str, pd.DataFrame, pd.DataFrame]:
    """_summary_

    Args:
        df (pd.DataFrame): The original dataframe

    Returns:
        tuple[str, str, pd.DataFrame, pd.DataFrame]: home_team, away_team, dataframe of the home team, dataframe of the away team
    """
    get_home_team = df.query("TEAM_ID == HOME_TEAM")
    get_away_team = df.query("TEAM_ID != HOME_TEAM")

    home_team = get_home_team.TEAM_NAME.value_counts().index.tolist()
    away_team = get_away_team.TEAM_NAME.value_counts().index.tolist()
    return str(home_team[0]), str(away_team[0]), get_home_team, get_away_team


def get_score(
    home_team: str,
    away_team: str,
    get_home_team: pd.DataFrame,
    get_away_team: pd.DataFrame,
) -> dict:
    """_summary_

    Args:
        home_team (list): The team that plays home
        away_team (list): The team that visit the other team
        get_home_team (pd.DataFrame): Dataframe that originatas from function -> get_home_away_team
        get_away_team (pd.DataFrame): Dataframe that originatas from function -> get_home_away_team

    Returns:
        dict: dictionary with Teams and Goals
    """
    home_team_score = get_home_team.GOALS.value_counts().index.tolist()
    away_team_score = get_away_team.GOALS.value_counts().index.tolist()

    score_dict = {
        "Teams": [home_team, away_team],
        "Goals": [home_team_score[0], away_team_score[0]],
    }
    return score_dict


def get_winning_team(df: pd.DataFrame) -> tuple[str, str]:
    """_summary_

    Args:
        df (pd.DataFrame): The original dataframe

    Returns:
        tuple[str, str]: winning team name, losing team name
    """
    winning_team_df = df.sort_values(by="GOALS", ascending=False)
    winning_team = winning_team_df.TEAM_NAME.iloc[0]
    losing_team_df = df.sort_values(by="GOALS", ascending=True)
    losing_team = losing_team_df.TEAM_NAME.iloc[0]
    return str(winning_team), str(losing_team)


def get_possession_percentage(
    get_home_team: pd.DataFrame, get_away_team: pd.DataFrame
) -> tuple[str, str]:
    """_summary_

    Args:
        get_home_team (pd.DataFrame): Dataframe that originatas from function -> get_home_away_team
        get_away_team (pd.DataFrame): Dataframe that originatas from function -> get_home_away_team

    Returns:
        tuple[str, str]: home team possession percentage, away team possession percentage
    """
    home_team_possession = (
        get_home_team.POSSESSION_PERCENTAGE.value_counts().index.tolist()
    )
    away_team_possession = (
        get_away_team.POSSESSION_PERCENTAGE.value_counts().index.tolist()
    )
    return str(home_team_possession[0]), str(away_team_possession[0])


def prompt_instructions(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): The original dataframe

    Returns:
        pd.DataFrame: New dataframe with prompt instructions
    """
    event_prompt = goal_events(df=df)
    home_team, away_team, get_home_team_df, get_away_team_df = get_home_away_team(df=df)
    score_dict = get_score(
        home_team=home_team,
        away_team=away_team,
        get_home_team=get_home_team_df,
        get_away_team=get_away_team_df,
    )
    winning_team, losing_team = get_winning_team(df=df)
    home_team_possession, away_team_possession = get_possession_percentage(
        get_home_team=get_home_team_df, get_away_team=get_away_team_df
    )
    prompt = create_prompt(
        home_team=home_team,
        away_team=away_team,
        event_prompt=event_prompt,
        home_team_possession=home_team_possession,
        away_team_possession=away_team_possession,
        winning_team=winning_team,
        score_dict=score_dict,
    )
    prompt_df = pd.DataFrame(
        {
            "Prompt": prompt,
            "Completion": "Hier komt de gehele samenvatting die bij de wedstrijd hoort.",
        },
        index=[0],
    )
    return prompt_df


if __name__ == "__main__":
    df = pd.read_csv("data/opta_sample_data_2.csv")
    prompt_df = prompt_instructions(df=df)
    prompt_df.to_csv("converted_prompts/opta_converted.csv")
