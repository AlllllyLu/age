driving = input('你有沒有開車經驗?')
if driving != '有' and driving != '沒有':
	print('請輸入 有/沒有')
	raise SystemExit
	
age = input ('請輸入年齡：')
age = int(age)
if driving == '有':
	if age >= 18:
		print('開車請注意安全')
	else:
		print('請勿無照駕駛') 
elif driving == '沒有':
	if age >= 18:
		print('可以考慮考駕照囉')
	else:
		print('再過幾年就可以考駕照囉')
else:
	print('請輸入 有/沒有')
