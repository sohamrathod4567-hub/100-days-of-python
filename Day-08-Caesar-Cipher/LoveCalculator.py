def calculate_love_score(name1, name2):
    combined = (name1 +name2).lower()
    true = 0
    love = 0


    for t in combined:
        if t == "t":
            true+= 1

        if t == "r":
            true+=1
        if t == "u":
            true+= 1
        print(t)
        if t == "e":
            true+=1
        if t == "l":
            love+= 1

        if t == "o":
            love+=1
        if t == "v":
            love+= 1
        print(t)
        if t == "e":
            love+=1
        score = str(true) + str(love)
        print(score)


calculate_love_score("KanyeWest", "KimKardashinan")