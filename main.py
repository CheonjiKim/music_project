from src.game_pre import *
from src.game_in import *
from src.music_data import korpop_track, ballad_track, pop_track, hiphop_track
import winsound as ws

# 장르의 순서는 다음과 같다: 
genres = ["Kpop", "발라드", "팝송", "힙합"]

#게임 시작
print_genres()
selected_genre_num = get_genre_num()
tracks = load_tracks(selected_genre_num)

part1 = korpop_track[0].get_part1()
ws.PlaySound(part1, 0)

