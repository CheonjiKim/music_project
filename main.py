import time
from src.game_out import *
from src.game_in import *
from src.music_data import korpop_track, ballad_track, pop_track, hiphop_track

# 장르의 순서는 다음과 같다: 
all_tracks = [korpop_track, ballad_track, pop_track, hiphop_track]
points_for_genres = [4, 5, 6, 4]




#korpop이 선택되었다고 치자 일단은.
track = korpop_track



#일단 lovelee라고 치자
song = track[0]
part = [song.get_part1(), song.get_part2(), song.get_part3()]
# 배열에서 노래 하나를 선택하고, 그 노래를 배열에서 제거한다.
# 러브리로 테스트하고나서는 실전에선 이걸 써야해 song = take_a_randomsong_from_track(track)


score = 0 # 이게 10점에 도달해야 한다.
time.sleep(2)
print("=========================")
print("지금부터 게임을 시작합니다.")
print("=========================")
time.sleep(2)
print()

# 이 while문에서 게임이 진행된다.
while(score < 10):
    print_genres()
    genre_idx = get_genre_idx()
    track = all_tracks[genre_idx]
    point = points_for_genres[genre_idx]
    
    score += play_round(track, point)
    

# 승패 판정
if(score >= 10):
# 결국 스코어가 10이 넘어야 이긴다.
    end_win_game()
else:
# 이 구문에 걸리는 경우는 사실 없을 것이다. while문에서 10점 도달할 때까지 빠져나오지 못하기 때문이다.
#   while문에서 10점 도달할 때까지 빠져나오지 못하기 때문이다. 
    end_lose_game()


