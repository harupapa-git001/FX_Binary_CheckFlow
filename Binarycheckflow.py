#バイナリーチェックフロー
ans = ""

text1 = input("通貨ペアを入力してください")
text2 = input("取引種別を入力してください")


while ans != "y":
  print("事前チェック:5分足にフラクタルレンジ はありませんか？")
  ans = input("はい:y いいえ:n >")
  
  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break


while ans != "y":
  print("1.5分足の遅行スパンは抜けていますか？(レベルは大丈夫ですか？)")
  ans = input("はい:y いいえ:n >")
  
  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("2.5分足のフラクタルアッパーロワーはついていますか?")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("3.5分足の直近波動にグランビル材料がありますか？")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("4.5分足のろうそく足が適正レベルですか？")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("5.5分足のBB1.618のスクィーズは大丈夫ですか？")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    print("\n5分足にバーティカルラインを引いてください\n")
    print("\n1分足バーティカルラインから5本カウントしてください")
    ans = ""
    break

while ans != "y":
  print("事前チェック:1分足にフラクタルレンジ はありませんか？")
  ans = input("はい:y いいえ:n >")
  
  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("6.1分足の遅行スパンは抜けていますか？(レベルは大丈夫ですか？)")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("7.1分足のフラクタルアッパーロワーはついていますか?")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("8.1分足の直近波動にグランビル材料がありますか？")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break
  
while ans != "y":
  print("9.1分足のろうそく足が適正レベルですか？")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("10.1分足のBB1.618のスクィーズは大丈夫ですか？")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    ans = ""
    break

while ans != "y":
  print("11.選択した通貨ペアと判定時間は大丈夫ですか？")
  ans = input("はい:y いいえ:n >")

  if ans != "n" and ans != "y":
    print("入力が正しくありません")
  elif ans == "n":
    print("もう一度")
  else:
    print("{}の{}を取引してください".format(text1, text2))
    ans = ""
    break
