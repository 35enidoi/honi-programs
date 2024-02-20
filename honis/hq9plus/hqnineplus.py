def hqnineplus(code:str):
    coded = list(code)
    accumulator = 0
    for i in coded:
        if i == "H":
            print("Hello,world!")
        elif i == "Q":
            print(code)
        elif i == "9":
            for r in range(100):
                if r == 99:
                    print("No more bottles of beer on the wall, no more bottles of beer.")
                    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
                    continue
                print(99-r,"bottles of beer on the wall,",99-r,"bottles of beer.") 
                if r == 98:
                    bottlenum = "no more"
                else:
                    bottlenum = 98-r
                print(f"Take one down and pass it around, {bottlenum} bottles of beer on the wall.\n")
        elif i == "+":
            accumulator += 1