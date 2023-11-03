class Music:   
    def __init__(self, title, author, rel_year):
        self.title = title
        self.author = author
        self.rel_year = rel_year
        self.part1loc = ""
        self.part2loc = ""
        self.part3loc = ""
        
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def set_partlocs(self, p1, p2, p3):
        self.part1loc = p1
        self.part2loc = p2
        self.part3loc = p3
        return;
    

    # 실제 main에서 사용할 메소드 세 개이다.
    # wav 파일의 경로를 반환한다.
    def get_rel_year(self):
        return self.rel_year

    def get_part1(self):
        return self.part1loc

    def get_part2(self):
        return self.part2loc
    
    def get_part3(self):
        return self.part3loc