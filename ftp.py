#!/usr/bin/env python3
import os

def proverka(date): #нужна в случае, если ввод из терминала

    if len(date) != 3 and isinstance(date, list):
        return 0
    try:
        for i in range(3):
            date[i] = int(date[i])
    except ValueError:
        return 0

    a, b, c = date[0], date[1], date[2]
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if c < 1 or c > 3000 or b < 1 or b > 12 or a < 1 or a > 31: return 0

    visokos = 0
    if c % 4 == 0:
        visokos = 1
        if c % 100 == 0 and c % 400 != 0:
            visokos = 0
    if visokos == 1: month[1] = 29

    if a > month[b-1]: return 0
    return 1

def ftp():
    print(" ______     _________   ______     ")
    print("/_____/\   /________/\ /_____/\    ")
    print("\::::_\/_  \__.::.__\/ \:::_ \ \   ")
    print(" \:\/___/\    \::\ \    \:(_) \ \  ")
    print("  \:::._\/     \::\ \    \: ___\/  ")
    print("   \:\ \        \::\ \    \ \ \    ")
    print("    \_\/         \__\/     \_\/    ")
    print("                                   ")

    date1 = [2019, 1, 1] 
    date2 = [2023, 3, 13]


    #если даты нужно вводить из терминала, нужно раскомментировать блок ниже

    #flag = 0
    #while flag != 1:
    #    date1 = list(input("Введите дату начала архива (включительно) в формате [day month year]: ").split())
    #    if proverka(date1) == 0: 
    #        print("Вы где-то ошиблись, попробуйте ещё раз")
    #    else:
    #        flag = 1
    #
    #flag = 0
    #while flag != 1:
    #    date2 = list(input("Введите дату конца архива (включительно) в формате [day month year]: ").split())
    #    if proverka(date2) == 0: 
    #        print("Вы где-то ошиблись, попробуйте ещё раз")
    #    else:
    #        flag = 1
    #
    #for i in range(3):
    #    date1[i], date2[i] = int(date1[i]), int(date2[i])
    #
    #
    #if (   date2[2] < date1[2]   ) or (   date2[2] == date1[2] and date2[1] < date1[1]   ) or (   date2[2] == date1[2] and date2[1] == date1[1] and date2[0] < date1[0]   ):
    #    print("Неверный порядок дат")
    #    exit()

    #конец блока




    #a = os.popen("""lftp -e "find -l;bye" ftp://ftp.glonass-iac.ru""")  # эта строка не работает, если файлов много, как в случае с сервером глонасса

    #lftp -e "find -l;bye" ftp://ftp.glonass-iac.ru &> files.txt # в случае, если строка выше не работает, копируем эту в терминал, она создает файл
    #files.txt с выводом строки выше и заполняется со временем. Из терминала прогресса видно не будет, поэтому нужно проверять состояние строки с помощью 
    #команды wc -l files.txt (она покажет, сколько строк в файле), команду эту нужно вставлять в другом терминале. Затем мы прерываем изначальную команду
    #с помощью Ctrl+C (2 раза) и удаляем слово Прерывание (или Interrupt) в созданном файле в конце файла с помощью терминального текстового редактора 
    # (Nano, например), так как терминальные редакторы могут открывать файлы с огромным количеством строк (в случае с глонасс их будет от 80 до 90 тысяч).
    #После этого программа заработает. Это временный костыль, пока не придумал, как исправить это
    a = open("files.txt")
    list_of_files = list()
    for line in a:
        spisok = line.strip().split(" ")
        spisok = [ i for i in spisok if i!=" " and i !=""] 
        q = str(" ".join(spisok[5:]))
        spisok = spisok[0:5]
        spisok.append(q)
        list_of_files.append(spisok)
    list_of_files = list_of_files[1:]
    a.close()
    for i in range(len(list_of_files)):
        date_of_cuerrent_file = list_of_files[i][3].split("-")
        for j in range(3): date_of_cuerrent_file[j] = int(date_of_cuerrent_file[j])
        if list_of_files[i][0][0] != "d":
            if date_of_cuerrent_file[0] >= date1[0] and date_of_cuerrent_file[0] <= date2[0]:
                if date_of_cuerrent_file[1] >= date1[1] and date_of_cuerrent_file[1] <= date2[1]:
                    if date_of_cuerrent_file[2] >= date1[2] and date_of_cuerrent_file[2] <= date2[2]:
                        ourpath = list_of_files[i][5]
                        ftppath = "\""+ourpath[2:]+"\""
                        ourpath = "\""+ourpath+"\""
                        print(f"wget ftp://ftp.glonass-iac.ru/{ftppath}  -P {ourpath}")
                        #os.system(f"wget ftp://ftp.glonass-iac.ru/{ftppath}  -P {ourpath}") # эта строка отправляет запрос на скачивание файла
                        #пример запроса: wget ftp://ftp.glonass-iac.ru/ARCHIV_KOC/123 -P ./ARCHIV_KOC/123

if __name__ == "__main__":
    ftp()
