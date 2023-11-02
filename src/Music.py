class Music:   
    def __init__(self, title, author):
        self.title = title
        self.author = author
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
    def get_part1(self):
        return self.part1loc

    def get_part2(self):
        return self.part2loc
    
    def get_part3(self):
        return self.part3loc

    
t1 = Music("서른즈음에","김광석")

t1.set_partlocs("1ban", "2ban", "3ban")

print(t1.get_part2())