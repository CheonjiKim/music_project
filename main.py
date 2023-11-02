from src.pre_game import *
from src.in_game import *

# 장르의 순서는 다음과 같다: 
genres = ["Kpop", "발라드", "팝송", "힙합"]

#게임 시작
print_genres()
selected_genre_num = get_genre_num()
tracks = load_tracks(selected_genre_num)

