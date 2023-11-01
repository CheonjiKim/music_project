
# 유저에게 장르를 물어보고, 유저의 선택을 반환하는 함수



def is_guess_correct(title, guess):
    # 유저가 입력한 제목의 띄어쓰기와 대소문자 차이를 확인할 필요가 있다.
    # 아래 if문은 위에서 언급한 차이를 수긍하도록 한다.
    if(title.replace(" ", "").strip().lower() == guess.replace(" ", "").strip().lower()):
        return True
    else: return False

# 최초 게임 시작 시 쓰이는 함수이다.
def get_genre_num():
    genres = ["Kpop", "발라드", "팝송", "힙합"]
    print("0: Kpop")
    print("1: 발라드")
    print("2: 팝송")
    print("3: 힙합")
    
    #에러 처리 구문
    try :
        num = int(input("원하는 장르를 선택하세요: "))
        genres[num]
    except:
        print("장르를 잘못 입력하셨습니다. 다시 입력하세요.")
        return get_genre_num()
        
    print(genres[num], "장르를 선택하셨습니다.")
    return num


test1 = "a"
test2 = "  AbCd ".lower()
test3 = "안녕하세요 erETdf".lower()

print(test3)


