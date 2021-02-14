fractal = input("フラクタルのアッパーロワーの数値を入力してください")
trend = input("フラクタルの確定した上限下限のレートを入寮してください")
value = input("アッパーロワーから何本目の終値の判定か入力してください:2より大きい数")

rate = 0

if int(value) > 2 :
    rate = float(fractal) - (((float(fractal) - float(trend)) / 2) * int(value))
    print("{}本目のラインのレートは{}です".format(value, rate))
else:
    print("2より大きい数字を入力してください")
