class Music:
    #self는 매개변수가 아니다.
    #self는 Java의 this 키워드라고 생각해라.

    def __init__(self, title, author, rel_year):
        self.title = title
        self.author = author
        self.rel_year = rel_year
        self.part1_name = ""
        self.part2_name = ""
        self.part3_name = ""
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    
    def set_song_files(self, p1, p2, p3):
    # wav 파일의 경로를 입력하는 메소드이다.
        DEFALUT_ROUTE = "src/music/" # main.py가 있는 위치를 기준으로 음원 파일은 src/music에 있다.
        self.part1_name = DEFALUT_ROUTE + p1
        self.part2_name = DEFALUT_ROUTE + p2
        self.part3_name = DEFALUT_ROUTE + p3
        return;
    
    def get_rel_year(self):
        return self.rel_year

    def get_part1(self):
        return self.part1_name

    def get_part2(self):
        return self.part2_name
    
    def get_part3(self):
        return self.part3_name