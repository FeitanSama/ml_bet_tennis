import os
import numpy as np
import pandas as pd

csv_aggregate_path = os.getcwd() + '/data/aggr'
csv_prep_path = os.getcwd() + '/data/prep'

df = pd.read_csv(csv_aggregate_path + '/aggr.csv')

df_under_50 = df[df['minutes'] <30]

df_stop = df[df['score'].str.contains("W/O")|df['score'].str.contains("RET")]
df = df.drop(df_stop.index.values)

df = df.drop(['Unnamed: 0','match_num','winner_seed','winner_entry','loser_seed',
            'loser_entry','score','minutes','w_ace','w_df','w_svpt','w_1stIn',
            'w_1stWon','w_2ndWon','w_SvGms','w_bpSaved','w_bpFaced','l_ace',
            'l_df','l_svpt','l_1stIn','l_1stWon','l_2ndWon',
            'l_SvGms','l_bpSaved','l_bpFaced'],axis=1)

df_commun = df[['tourney_id','tourney_name','surface','draw_size','tourney_level','tourney_date','best_of','round']]

df_player1 = df[['winner_id','winner_name','winner_hand','winner_ht','winner_ioc','winner_age','winner_rank','winner_rank_points']]
df_player1 = df_player1.rename(columns={
    "winner_id": "player_id",
    "winner_name": "player_name",
    "winner_hand": "player_hand",
    "winner_ht": "player_ht",
    'winner_ioc': "player_ioc",
    'winner_age': "player_age",
    'winner_rank': "player_rank",
    'winner_rank_points': "player_rank_points"
})
df_player1['target'] = 'win'

df_player2 = df[['loser_id','loser_name','loser_hand','loser_ht','loser_ioc','loser_age','loser_rank','loser_rank_points']]
df_player2 = df_player2.rename(columns={
    "loser_id": "player_id",
    "loser_name": "player_name",
    "loser_hand": "player_hand",
    "loser_ht": "player_ht",
    'loser_ioc': "player_ioc",
    'loser_age': "player_age",
    'loser_rank': "player_rank",
    'loser_rank_points': "player_rank_points"
})
df_player2['target'] = 'lose'

df_c_p1 = df_commun.join(df_player1)

df_c_p2 = df_commun.join(df_player2)

result = pd.concat([df_c_p1,df_c_p2])
result['tourney_date'] = pd.to_datetime(result['tourney_date'], format='%Y%m%d')
result = result.sort_values(by="tourney_date")

result.to_csv(csv_prep_path +'/prep.csv')

