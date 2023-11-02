# 유저에게 장르를 물어보고, 유저의 선택을 반환하는 함수
# 최초 게임 시작 시 쓰이는 함수이다.
def print_genres():
    genres = ["Kpop", "발라드", "팝송", "힙합"]
    for i in range(len(genres)):
        print(i, ":", genres[i])
    print()

def get_genre_num():
    genres = ["Kpop", "발라드", "팝송", "힙합"]
    #에러 처리 구문
    try :
        num = int(input("원하는 장르를 선택하세요: "))
        genres[num]
        # if not(0 <= num and num <= 3):
        #     print("장르를 잘못 입력하셨습니다. 다시 입력하세요.")
        #     return get_genre_num()
    except:
        print()
        print("장르를 잘못 입력하셨습니다. 다시 입력하세요.")
        return get_genre_num()
    print()    
    print(genres[num], "장르를 선택하셨습니다.")
    return num

def load_tracks(selected_genre_num):
    genres = ["Kpop", "발라드", "팝송", "힙합"]
    return "dictionary"