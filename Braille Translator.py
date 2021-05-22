
option = input("type 1 to run the program or type 2 to end the program:")
if option !="1" and option !="2":
    while option !="1" and option !="2":
        option=input("Wrong input \nType 1 to run the program or type 2 to end the program:")
if option=="2":
    print("Program ended")    
if option=="1":    
    while option=="1":
        in_braille = input("write any scentance:")
        in_braille = in_braille.replace(".","..**.*").replace(" "," ......").replace(","," ..*...")
        in_braille = in_braille.replace("a"," *..... ").replace("b"," *.*... ").replace("c"," **.... ").replace("d"," **.*.. ").replace("e"," *..*.. ").replace("f"," ***... ").replace("g"," ****.. ").replace("h"," *.**.. ").replace("i"," .**... ").replace("j"," .***.. ").replace("k"," *...*. ").replace("l"," *.*.*. ").replace("m"," **..*. ").replace("n"," **.**. ").replace("o"," *..**. ").replace("p"," ***.*. ").replace("q"," *****. ").replace("r"," *.***. ").replace("s"," .**.*. ").replace("t"," .****. ").replace("u"," *...** ").replace("v"," *.*.** ").replace("w"," .***.* ").replace("x"," **..** ").replace("y"," **.*** ").replace("z"," *..*** ")
        in_braille = in_braille.replace("A"," *..... ").replace("B"," *.*... ").replace("C"," **.... ").replace("D"," **.*.. ").replace("E"," *..*.. ").replace("F"," ***... ").replace("G"," ****.. ").replace("H"," *.**.. ").replace("I"," .**... ").replace("J"," .***.. ").replace("K"," *...*. ").replace("L"," *.*.*. ").replace("M"," **..*. ").replace("N"," **.**. ").replace("O"," *..**. ").replace("P"," ***.*. ").replace("Q"," *****. ").replace("R"," *.***. ").replace("S"," .**.*. ").replace("T"," .****. ").replace("U"," *...** ").replace("V"," *.*.** ").replace("W"," .***.* ").replace("X"," **..** ").replace("Y"," **.*** ").replace("Z"," *..*** ")
        print(in_braille)
        option = input("type 1 to run the program or type 2 to end the program:")
        if option !="1" and option !="2":
            while option !="1" and option !="2":
                option=input("Wrong input \nType 1 to run the program or type 2 to end the program:")  
        if option == "2":
            print("program ended")