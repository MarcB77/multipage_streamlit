import pandas as pd
from convert import prompt_instructions

if __name__ == "__main__":
    df = pd.read_csv("./data/opta_all_games.csv")
    prompt_df = pd.DataFrame()
    for game in df.GAME_ID.unique().tolist():
        df_game = df.query("GAME_ID == " + str(game))
        prompt_game_df = prompt_instructions(df=df_game)
        prompt_df = pd.concat([prompt_df, prompt_game_df])
    prompt_df.to_csv("converted_prompts/opta_converted_multi_games.csv")
