import random
import winsound
import time

def input_guess():
    guess = input("이 곡의 제목을 입력하세요 : ")
    print()
    guess = guess.replace(" ", "").strip().lower() # 공백제거, 소문자화
    return guess

def is_guess_correct(title, guess):
    # 유저가 입력한 제목의 띄어쓰기와 대소문자 차이를 확인할 필요가 있다.
    # 대소문자 차이나, 띄어쓰기 차이 때문에 오답이 될 수는 없기 때문이다.
    # 아래 if문은 위에서 언급한 차이를 수긍하도록 한다.
    if(title.replace(" ", "").strip().lower() == guess.replace(" ", "").strip().lower()):
        return True
    else: return False
    
def take_a_randomsong_from_track(tr):
    rand_idx = random.randint(0, len(tr))
    song = tr[rand_idx]
    tr.remove(song)
    return song

def end_lose_game():
    print("========================")
    print("패배하셨습니다. 게임을 종료합니다.")
    print("========================")
    exit()
    
def end_win_game():
    print("========================")
    print("목표 점수에 도달하셨습니다.")
    print("승리하셨습니다. 게임을 종료합니다.")
    print("========================")
    exit()

def play_round(track, point):
# 해당 장르의 트랙과, 그 장르의 기본 포인트를 매개변수로 넣는다.
# 세 번 음악을 틀고 그때마다 제목을 물어본다. 음악을 못 맞출 때마다 1점씩 깎는다.
# 음악을 맞히면 그에 맞는 점수를 반환한다.
# 세 번의 기회가 끝나면 패배 선언한다.
    if (track == []):
        print("해당 장르 트랙의 모든 곡을 사용했습니다.")
        
    song = take_a_randomsong_from_track(track)
    part = [song.get_part1(), song.get_part2(), song.get_part3()]
    chance = 3
    i = 0
    
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
            return point
        else: # 정답을 맞히지 못한 경우
            point -= 1
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
                lose_game(score)
        time.sleep(2)
    return point