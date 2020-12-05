import datetime
dt_now = datetime.datetime.now()

while True :
    year = input("あなたの生まれた年を入力してください:")
    if year.isdigit() :
        year = dt_now.year - int(year)
        year2 = year - 1
        break

    else :
        print("不正な値です。正確な値を入力してください。")

while True :
    month = input("あなたの生まれた月を入力してください:")
    if month.isdigit() :
        if int(month) < dt_now.month :
            age = year
            break

        elif int(month) == dt_now.month :
            while True :
                day = input("あなたの生まれた日を入力してください:")
                if day.isdigit() :
                    if int(day) <= dt_now.day :
                        age = year
                        break

                    else :
                        age = year2
                        break

                else :
                      print("不正な値です。正確な値を入力してください。")

        elif int(month) > dt_now.month :
            age = year2
            break

    else :
        print("不正な値です。正確な値を入力してください。")

    break

if age >= 20 :
    print(str(age) + "歳のあなたのチケット料金は500円です。")

elif 12 <= age < 20 :
    print(str(age) + "歳のあなたのチケット料金は300円です。")

elif age < 12 :
    print(str(age) + "歳のあなたのチケット料金は無料です。")
