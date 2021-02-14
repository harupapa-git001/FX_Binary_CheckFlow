#一目改チェックフロー
ans = ""

while ans != "y":
  print("1.遅行スパンは根元から追跡して抜けていますか？")
  ans = input("はい:y いいえ:n ")
  
  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("2.フラクタルアッパーロワーはついていますか?")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("3.ろうそく足がアッパーロワーから2本確定していますか？")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("4.一目改のラインは引けましたか？")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("5.ろうそく足が適正レベルにありますか?")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("6.上位足の2本目のポイントと被りませんか?")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break
  
while ans != "y":
  print("7.2つ下の時間足の最小期待値は大丈夫ですか？")
  ans = input("はい:y いいえ:n ")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    print("取引してください")
    ans = ""
    break
