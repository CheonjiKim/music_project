import time
from src.game_out import *
from src.game_in import *
from src.music_data import korpop_track, ballad_track, pop_track, hiphop_track

# 장르의 순서는 다음과 같다: 
all_tracks = [korpop_track, ballad_track, pop_track, hiphop_track]
points_for_genres = [4, 5, 6, 4] # 기본값은 [4, 5, 6, 4]이다.


# song = take_a_randomsong_from_track(track)
# part = [song.get_part1(), song.get_part2(), song.get_part3()]
# 배열에서 노래 하나를 선택하고, 그 노래를 배열에서 제거한다.




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
    default_point = points_for_genres[genre_idx]
    
    gained_point = play_round(track, default_point)
    if (gained_point == "null"):
        # 해당 트랙의 노래를 모두 소진한 경우
        # while문 시작으로 안내하여 다른 곡을 선택하도록 한다.
        continue
    score += gained_point
    time.sleep(2)
    print("획득한 점수:", score)
    

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


