import random

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
