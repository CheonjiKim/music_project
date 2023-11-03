import time
import winsound
from src.game_pre import *
from src.game_in import *
from src.music_data import korpop_track, ballad_track, pop_track, hiphop_track

# 장르의 순서는 다음과 같다: 
all_tracks = [korpop_track, ballad_track, pop_track, hiphop_track]

print_genres()
track = all_tracks[get_genre_idx()]


#korpop이 선택되었다고 치자 일단은.
track = korpop_track

chance = 3
score = 0

#일단 lovelee라고 치자
song = track[0]

# 배열에서 노래 하나를 선택하고, 그 노래를 배열에서 제거한다.
# 러브리로 테스트하고나서는 실전에선 이걸 써야해 song = take_a_randomsong_from_track(track)


part = [song.get_part1(), song.get_part2(), song.get_part3()]

i = 0

time.sleep(2)
print("=========================")
print("게임을 시작합니다.")
print("=========================")
print()
time.sleep(2)


while(chance > 0):
    print("(♪ 곡의 일부 재생중 ♪)")
    winsound.PlaySound(part[i], 0) # 재생
    guess_title = input_guess()
    song_title = song.get_title()
    correct = is_guess_correct(song_title, guess_title)
    time.sleep(1)
    if (correct): 
        score += 1
        print("정답을 맞혔습니다!")
        print("해당 곡은", song.get_author(), "의", song.get_title(), "입니다.")
        break
    else: # 정답을 맞히지 못한 경우
        chance -= 1
        i += 1
        
        print("정답이 아닙니다. 기회가 하나 차감됩니다.")
        print("남은 기회 수:", chance)
        print()
        if(chance > 0):
            time.sleep(1)
            print("(해당 곡의 다른 부분을 재생합니다.)")
            print()
        else:
            print("기회를 모두 소진하였습니다.")
            print("해당 곡은", song.get_author(), "의", song.get_title(), "입니다.")
            print()
    time.sleep(2)

if(score >= 1):
    print("축하합니다. 승리하셨습니다!")
    exit()

if(chance <= 0):
    print("패배하셨습니다.")
    exit()


