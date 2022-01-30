
def number_of_diverse_group(N,S):
    fmap = {}

    if N == 1:
        return 1

    for idx,ch in enumerate(S):
        if ch not in fmap:
            fmap[ch] = []
        fmap[ch].append(idx)

    output = 1
    for key, value in fmap.items():
        output *= len(value)

    output += N
    return output

def test_cases_1():
    N = 1
    S = "a"
    output  = 1
    assert output == number_of_diverse_group(N,S)

def test_cases_2():
    N = 2
    S = "ba"
    output  = 3
    assert output == number_of_diverse_group(N,S)

def test_cases_3():
    N = 5
    S = "abaab"
    output  = 11
    assert output == number_of_diverse_group(N,S)


test_cases_1()
test_cases_2()
test_cases_3()