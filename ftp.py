#!/usr/bin/env python3
import os
import subprocess
from getpass import getpass

def proverka(date):

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

def generator(date1, date2): # date в формате [22, 5, 2000]
    #file = open("data.txt", "w")
    #for k in range(date1[2], date2[2]+1):
    #    for j in range(date1[1], date2[1]+1):
    #        for i in range(date1[0], date2[0]):
    #            testdata = [i, j, k]
    #            if proverka(testdata):
    #                file.write(f"{i}-{j}-{k}.txt\n")
    #file.close()
    dates = list()
    for i in range(date1[2], date2[2]+1):
        for j in range(1, 13):
            for k in range(1, 32):
                if i == date1[2] and (j < date1[1] or j == date1[1] and k < date2[0]):
                    continue
                if i == date2[2] and (j > date2[1] or j == date2[1] and k > date2[0]):
                    continue
                testdata = [k, j, i]
                if proverka(testdata):
                    dates.append(f"{k}-{j}-{i}.txt")

    return dates


def example_generator():
    return generator([30, 1, 1999], [25, 12, 2007])

def ftp():
    print(" ______     _________   ______     ")
    print("/_____/\   /________/\ /_____/\    ")
    print("\::::_\/_  \__.::.__\/ \:::_ \ \   ")
    print(" \:\/___/\    \::\ \    \:(_) \ \  ")
    print("  \:::._\/     \::\ \    \: ___\/  ")
    print("   \:\ \        \::\ \    \ \ \    ")
    print("    \_\/         \__\/     \_\/    ")
    print("                                   ")


    flag = 0
    while flag != 1:
        date1 = list(input("Введите дату начала архива (включительно) в формате [day month year]: ").split())
        if proverka(date1) == 0: 
            print("Вы где-то ошиблись, попробуйте ещё раз")
        else:
            flag = 1

    flag = 0
    while flag != 1:
        date2 = list(input("Введите дату конца архива (включительно) в формате [day month year]: ").split())
        if proverka(date2) == 0: 
            print("Вы где-то ошиблись, попробуйте ещё раз")
        else:
            flag = 1

    for i in range(3):
        date1[i], date2[i] = int(date1[i]), int(date2[i])


    if (   date2[2] < date1[2]   ) or (   date2[2] == date1[2] and date2[1] < date1[1]   ) or (   date2[2] == date1[2] and date2[1] == date1[1] and date2[0] < date1[0]   ):
        print("Неверный порядок дат")
        exit()

    dates = generator(date1, date2)

    user = input("Введите имя пользователя ftp сервера: ")
    password = getpass("Введите пароль: ")
    ipadress = input("Введите ip адрес сервера или домен: ")
    ftppath = input("Введите путь, по которому лежат файлы в папке пользователя(без / на конце): ")
    ourpath = input("Введите полный путь, в который скопируются файлы (можно нажать enter для текущей папки): ")
    if ourpath != "":
        ourpath = " -P "+ourpath

    #os.system("wget ftp://user:password@ftp.mydomain.com/path/file.ext -P /home/path")
    for i in dates:
        os.system(f"wget ftp://{user}:{password}@{ipadress}/{ftppath}/{i} {ourpath}")
        #subprocess.run(f"wget ftp://{user}:{password}@{ipadress}/{ftppath}/{i}{ourpath}")



if __name__ == "__main__":
    ftp()