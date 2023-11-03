from src.Music import Music

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
love_lee = Music("Love Lee", "악동뮤지션(AKMU)", 2023)
get_a_guitar = Music("Get A Guitar", "라이즈(RIIZE)", 2023)
i_am = Music("I AM", "아이브(IVE)", 2023)

# Ballad
to_tell_to_breakup = Music("헤어지자 말해요", "박재정", 2023)
things_that_i_thought_as_love = Music("사랑이라 믿었던 것들은", "서동현(BIG Naughty)", 2023)
all_your_moments = Music("너의 모든 순간", "성시경", 2014)

# Pop
i_dont_think_that_i_like_her = Music("I Don't Think That I Like Her", "Charlie Puth", 2022)
steal_the_show = Music("Steal The Show", "Lauv", 2023)
closer = Music("Closer", "The Chainsmokers", 2016)

# Hiphop
smoke = Music("Smoke", "다이나믹 듀오 & 이영지", 2023)
sae_bbing = Music("새삥", "지코(ZICO)", 2022)
shut_down = Music("Shut Down", "블랙핑크(BLACKPINK)", 2022)


# track
korpop_track = [love_lee, get_a_guitar, i_am]
ballad_track = [to_tell_to_breakup, things_that_i_thought_as_love, all_your_moments]
pop_track = [i_dont_think_that_i_like_her,steal_the_show, closer]
hiphop_track = [smoke, sae_bbing, shut_down]

# 음원 파일 연결 작업
love_lee.set_partlocs("src/music/love_lee_001.wav","src/music/love_lee_002.wav","src/music/love_lee_003.wav")
all_your_moments.set_partlocs("src/music/all_your_moments_001.wav", "src/music/all_your_moments_002.wav", "src/music/all_your_moments_003.wav")
to_tell_to_breakup.set_partlocs("src/music/to_tell_to_breakup_001.wav","src/music/to_tell_to_breakup_002.wav","src/music/to_tell_to_breakup_003.wav")