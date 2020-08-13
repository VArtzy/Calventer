# Calventer 1.0

# Configuration!
nilai = True # set calculator on/off (true/false)
nilai2 = True # loop (do not change this!)\
nilai3 = True # loop (do not change this!)
lang = "EN" # variable to change language


# do not enter this area!!!
# English
while nilai == True:
    print(" ") 
    if lang == "EN":
        input1 = input("Welcome to Calventer 1.0!\nThe super smart program calculator!\ntype 'next' to go in calculator!\nYour default Language is EN/english!\nSet you language, type 'lang'!\nfor exit for program, type 'exit'!\n\nInput : ")
        if "next" == input1:
            nilai = False
            nilai2 = True
            operation = input("What's the operation (+,-,*,:): ")
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
            if operation == "+":
                hasil = num1 + num2
            elif operation == "-":
                hasil = num1 - num2
            elif operation == "*":
                hasil = num1 * num2
            elif operation == ":":
                hasil = num1 / num2
            else:
                print("Invalid operation!, type (+,-,*,:)!!! ")
            print(" ")
            print("Answer of " + str(num1) + " " + str(operation) + " " + str(num2) + " is: " + str(hasil))
            print(" ")
            while nilai2 == True:
                playagain = input("Wanna play again? (yes/no): ")
                if playagain == "yes":
                    nilai = True
                    nilai2 = False
                elif playagain == "no":
                    nilai2 = False
                    print("Thanks to playing!!!")
                else:
                    nilai = True
                    print("Type yes or no you noob!!!!! ")
        elif "lang" == input1:
            nilai = False
            nilai3 = True
            print("Your Language now is:" + " " +lang)
            while nilai3 == True:
                changeinput = input("Change your Language? (yes/no): ")
                if changeinput == "yes":
                    sublang = input("Enter Your language (EN/IND/JAP): ")
                    if sublang == "EN":
                        lang = "EN"
                        print("Change language to " + lang)
                        nilai3 = False
                        nilai = True
                    elif sublang == "IND":
                        lang = "IND"
                        print("Change language to " + lang)
                        nilai3 = False
                        nilai = True
                    elif sublang == "JAP":
                        lang = "JAP"
                        print("Change language to " + lang)
                        nilai3 = False
                        nilai = True
                    else:
                        print("Type EN/IND//JAP you noob!!!!! ")
                        nilai3 = True
                elif changeinput == "no":
                    print(" ")
                    print("Ok")
                    nilai3 = False
                    nilai = True
                else:
                    print("Type yes or no you noob!!!!! ")
                    nilai3 = True
        elif "exit" == input1:
            print("Exit from programs!")
            nilai = False
        else:
            print(" ")
            print("Type 'next'/'lang'!, your key isn't valid!")
            print(" ")
    elif lang == "IND":
        input1 = input("Selamat datang di Calventer 1.0!\nProgram kalkulator yang sangat pintar!\nketik 'next' untuk ke dalam kalkulatornya!\nBahasamu sekarang IND/indonesian!\nset bahasa kamu dengan, tulis 'lang'!\nuntuk keluar dari program, ketik 'exit'!\n\nInput : ")
        if "next" == input1:
            nilai = False
            nilai2 = True
            operation = input("Operasi apa yang kamu pilih? (+,-,*,:): ")
            num1 = float(input("Angka Pertama: "))
            num2 = float(input("Angka Kedua: "))
            if operation == "+":
                hasil = num1 + num2
            elif operation == "-":
                hasil = num1 - num2
            elif operation == "*":
                hasil = num1 * num2
            elif operation == ":":
                hasil = num1 / num2
            else:
                print("Operation tidak diketahui!, ketik (+,-,*,:)!!! ")
            print(" ")
            print("Jawaban dari " + str(num1) + " " + str(operation) + " " + str(num2) + " adalah: " + str(hasil))
            print(" ")
            while nilai2 == True:
                playagain = input("Main lagi? (yes/no): ")
                if playagain == "yes":
                    nilai = True
                    nilai2 = False
                elif playagain == "no":
                    nilai2 = False
                    print("Terimakasih sudah bermain!!!")
                else:
                    nilai = True
                    print("ketik yes atau no noob!!!!! ")
        elif "lang" == input1:
            nilai = False
            nilai3 = True
            print("Bahasamu sekarang adalah:" + " " +lang)
            while nilai3 == True:
                changeinput = input("Ganti bahasamu? (yes/no): ")
                if changeinput == "yes":
                    sublang = input("Masukan bahasamu (EN/IND/JAP): ")
                    if sublang == "EN":
                        lang = "EN"
                        print("Berhasil ganti bahasa ke " + lang)
                        nilai3 = False
                        nilai = True
                    elif sublang == "IND":
                        lang = "IND"
                        print("Berhasil ganti bahasa ke " + lang)
                        nilai3 = False
                        nilai = True
                    elif sublang == "JAP":
                        lang = "JAP"
                        print("Berhasil ganti bahasa ke " + lang)
                        nilai3 = False
                        nilai = True
                    else:
                        print("ketik EN/IND//JAP kamu noob!!!!! ")
                        nilai3 = True
                elif changeinput == "no":
                    print(" ")
                    print("Baiklah")
                    nilai3 = False
                    nilai = True
                else:
                    print("ketik yes atau no kamu noob!!!!! ")
                    nilai3 = True
        elif "exit" == input1:
            print("Keluar dari programs!")
            nilai = False
        else:
            print(" ")
            print("Ketik 'next'/'lang'!, kata tidak valid!")
            print(" ")
    elif lang == "JAP":
        input1 = input("Calventer 1.0へようこそ！\n超スマートなプログラム計算機！\nタイプ 'next' 電卓に行く!\nデフォルトの言語は JAP/日本!\n言語を設定して入力 'lang'!\nプログラムの終了には 'exit'!\n\n入力 : ")
        if "next" == input1:
            nilai = False
            nilai2 = True
            operation = input("操作は何ですか (+,-,*,:): ")
            num1 = float(input("最初の番号: "))
            num2 = float(input("2番目の番号: "))
            if operation == "+":
                hasil = num1 + num2
            elif operation == "-":
                hasil = num1 - num2
            elif operation == "*":
                hasil = num1 * num2
            elif operation == ":":
                hasil = num1 / num2
            else:
                print("無効な操作！、タイプ (+,-,*,:)！！！ ")
            print(" ")
            print("の答え " + str(num1) + " " + str(operation) + " " + str(num2) + " です: " + str(hasil))
            print(" ")
            while nilai2 == True:
                playagain = input("また遊びたい？ (yes/no): ")
                if playagain == "yes":
                    nilai = True
                    nilai2 = False
                elif playagain == "no":
                    nilai2 = False
                    print("遊んでくれてありがとう!!!")
                else:
                    nilai = True
                    print("yesまたはnoと入力します ")
        elif "lang" == input1:
            nilai = False
            nilai3 = True
            print("あなたの言語は今です:" + " " +lang)
            while nilai3 == True:
                changeinput = input("言語を変更しますか？ (yes/no): ")
                if changeinput == "yes":
                    sublang = input("言語を入力してください (EN/IND/JAP): ")
                    if sublang == "EN":
                        lang = "EN"
                        print("言語をに変更 " + lang)
                        nilai3 = False
                        nilai = True
                    elif sublang == "IND":
                        lang = "IND"
                        print("言語をに変更 " + lang)
                        nilai3 = False
                        nilai = True
                    elif sublang == "JAP":
                        lang = "JAP"
                        print("言語をに変更 " + lang)
                        nilai3 = False
                        nilai = True
                    else:
                        print("タイプ EN/IND//JAP あなたは初心者!!!!! ")
                        nilai3 = True
                elif changeinput == "no":
                    print(" ")
                    print("OK")
                    nilai3 = False
                    nilai = True
                else:
                    print("タイプ yes または no あなたは初心者!!!!! ")
                    nilai3 = True
        elif "exit" == input1:
            print("プログラムを終了する!")
            nilai = False
        else:
            print(" ")
            print("タイプ 'next'/'lang'!、 キーが無効です！")
            print(" ")