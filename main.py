import time
from src.game_functions import *
from src.music_data import korpop_track, ballad_track, pop_track, hiphop_track

# 장르의 순서는 다음과 같다: 
all_tracks = [korpop_track, ballad_track, pop_track, hiphop_track]
points_for_genres = [4, 5, 6, 4] # 기본값은 [4, 5, 6, 4]이다.


score = 0 # 이게 10점에 도달하면 승리한다.
time.sleep(1)
print("=========================")
print("지금부터 게임을 시작합니다.")
print("=========================")
time.sleep(1)
print()

# 이 while문에서 게임이 진행된다.

round_counter = 1
while(score < 10):
    print_genres()
    genre_idx = get_genre_idx()
    track = all_tracks[genre_idx]
    default_point = points_for_genres[genre_idx]
    
    time.sleep(1)
    print()
    print(f"======== # {round_counter}번째 라운드 시작 ========")
    print()
    round_counter += 1
    
    gained_point = play_round(track, default_point)    
    if (gained_point == "null"):
        # 해당 트랙의 노래를 모두 소진한 경우
        # while문 시작으로 안내하여 다른 곡을 선택하도록 한다.
        continue
    
    score += gained_point
    time.sleep(2)
    print()
    print("획득 점수:", gained_point)
    print("총점:", score)
    

# 승패 판정
if(score >= 10):
# 결국 스코어가 10이 넘어야 이긴다.
    print("========================")
    print("총 획득한 점수:", score)
    end_win_game()
else:
# 이 구문에 걸리는 경우는 사실 없을 것이다. while문에서 10점 도달할 때까지 빠져나오지 못하기 때문이다.
#   while문에서 10점 도달할 때까지 빠져나오지 못하기 때문이다.
    print("========================")
    print("총 획득한 점수:", score)
    end_lose_game()


