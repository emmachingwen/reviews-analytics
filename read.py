data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)  
		count += 1  #count=count+1
		if count % 1000 == 0:  # %是求餘數的意思
			print(len(data)) 
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言平均長度為', sum_len/len(data))

#篩選
new = []
for d in data:  #意思就是把data清單裡面的東西一個一個拿出來，都叫d
	if len(d) < 100:
		new.append(d)  #長度小於100的都裝進新的清單裡 
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) #印出new清單裡的第一筆