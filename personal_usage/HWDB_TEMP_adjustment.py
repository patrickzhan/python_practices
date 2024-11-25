ANT5 = list(map(int, "-143 -132 -121 -110 -99 -88 -77 -66 -55 -44 -33 -22 -11 0 11 22 33 44 55 66 77 88 99 110 121 132 143 154 165 176 187 198 209 220".split()))
ANT6 = list(map(int, "-126 -116 -107 -97 -87 -78 -68 -58 -49 -39 -29 -19 -10 0 10 19 29 39 49 58 68 78 87 97 107 116 126 136 146 155 165 175 184 194".split()))
temp_list = list(range(-400, 1300, 50))
LENGTH = len(temp_list)

def TEMP_COMP(ANT):
    new_ANT = [0 for _ in range(LENGTH)]
    for i in range(LENGTH):
        if i < len(ANT):  # Ensure we don't access out-of-bounds indices
            new_ANT[i] = [temp_list[i], ANT[i]]
        else:
            new_ANT[i] = [temp_list[i], None]  # Use `None` if ANT has fewer elements
    return new_ANT
print(TEMP_COMP(ANT5))
print(TEMP_COMP(ANT6))
