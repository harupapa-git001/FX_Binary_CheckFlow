value1 = 0
value2 = 0
value3 = 0
value4 = 0

fibo1 = input('高値を入力してください')
fibo2 = input('安値を入力してください')

value1 = (float(fibo1) - float(fibo2)) + float(fibo1)
value2 = ((float(fibo1) - float(fibo2)) * 3.236) + float(fibo1)
value3 = float(fibo2) - (float(fibo1) - float(fibo2))
value4 = float(fibo2) - ((float(fibo1) - float(fibo2)) * 3.236)
#def target2():
#    fibo *= 4.236
print("\n")
print("上昇[↑]フィボナッチ2.0の値は{}です".format(value1))
print("上昇[↑]フィボナッチ4.236の値は{}です".format(value2))
print("\n")
print("下落[↓]フィボナッチ2.0の値は{}です".format(value3))
print("下落[↓]フィボナッチ4.236の値は{}です".format(value4))