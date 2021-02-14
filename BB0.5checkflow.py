#BB0.5チェックフロー
ans = ""

while ans != "y":
  print("1.フラクタルレンジはありませんか?")
  ans = input("はい:y いいえ:n ")
  
  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("2.相場観の材料は大丈夫ですか？")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("3.波動の切り上げ切り下げはありますか?")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("4.フラクタルのアッパーロワーはありますか？")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("5.ろうそく足が6本以上経過しましたか？")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("6.グランビルの反発はありますか？?")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break
  
while ans != "y":
  print("7.BB0.5のターゲットは大丈夫ですか？")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    print("取引してください")
    ans = ""
    break
