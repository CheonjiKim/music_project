from src.Music import Music
import winsound
# 음악들은 다음과 같이 구성된다.
""" Kpop
        love_lee
        get_a_guitar
        i_am
    Ballad
        to_tell_to_breakup
        things_that_i_thought_as_love
        all_your_moments
    Pop
        i_dont_think_that_i_like_her
        steal_the_show
        the_chainsmokers
    Hiphop
        smoke
        sae_bbing
        shut_down    
"""

#Kpop
love_lee = Music("Love Lee", "악동뮤지션(AKMU)")
get_a_guitar = Music("Get A Guitar", "라이즈(RIIZE)")
i_am = Music("I AM", "아이브(IVE)")
korpop_track = [love_lee, get_a_guitar, i_am]

# Ballad
to_tell_to_breakup = Music("헤어지자 말해요", "박재정")
things_that_i_thought_as_love = Music("사랑이라 믿었던 것들은", "서동현(BIG Naughty)")
all_your_moments = Music("너의 모든 순간", "성시경")
ballad_track = [to_tell_to_breakup, things_that_i_thought_as_love, all_your_moments]

# Pop
i_dont_think_that_i_like_her = Music("I Don't Think That I Like Her", "Charlie Puth")
steal_the_show = Music("Steal The Show", "Lauv")
closer = Music("Closer", "The Chainsmokers")
pop_track = [i_dont_think_that_i_like_her,steal_the_show, closer]

# Hiphop
smoke = Music("Smoke", "다이나믹 듀오 & 이영지")
sae_bbing = Music("새삥", "지코(ZICO)")
shut_down = Music("Shut Down", "블랙핑크(BLACKPINK)")
hiphop_track = [smoke, sae_bbing, shut_down]


# 음원 파일 연결 작업
love_lee.set_partlocs("src/music/love_lee_001.wav","src/music/love_lee_002.wav","src/music/love_lee_003.wav")

# winsound.PlaySound(love_lee.get_part1(), 0)
# print("파트 1 재생끝")
# winsound.PlaySound(love_lee.get_part2(), 0)
# print("파트 2 재생끝")
# winsound.PlaySound(love_lee.get_part3(), 0)
# print("파트 3 재생끝")