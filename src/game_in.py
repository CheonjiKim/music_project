def get_guess():
    guess = input("이 곡의 제목을 입력하세요: ")
    print()
    guess = guess.replace(" ", "").strip().lower() # 공백제거, 소문자화
    return guess

def is_guess_correct(title, guess):
    # 유저가 입력한 제목의 띄어쓰기와 대소문자 차이를 확인할 필요가 있다.
    # 대소문자 차이나, 띄어쓰기 차이 때문에 오답이 될 수는 없기 떄문이다.
    # 아래 if문은 위에서 언급한 차이를 수긍하도록 한다.
    if(title.replace(" ", "").strip().lower() == guess.replace(" ", "").strip().lower()):
        return True
    else: return False


    


test1 = "a"
test2 = "  AbCd ".lower()
test3 = "안녕하세요 erETdf".lower()

genres = ["Kpop", "발라드", "팝송", "힙합"]

print_genres()
# a = get_genre_num()


