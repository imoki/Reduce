import os

# 读取文本
def readSentence(filename):
	print("[+] 读取文本")
	if os.path.isfile(filename):
		with open(filename, 'r', encoding='utf-8') as f:
			global sentence
			sentence = f.read().splitlines()	# 去除回车，返回列表
			sentence = ''.join(sentence)	# 将列表拼接成一行，可能多于400字
	else:
		print("[-] 待格式化降重文件不存在")
		f = open(filename,'w')
		f.close()
		print("[+] 已创建待格式化降重文件，请向文件内写入指定内容")
		os.system("pause")
		sys.exit(1)
		

# 写入编码文件
def writeFile(filename):
	print("[+] 格式化文本")
	with open(filename, 'w') as f:
		f.write(sentence)

if __name__ == '__main__':
	infilename = "待格式化降重文件.txt"
	outfilename = "已格式化降重文件.txt"
	readSentence(infilename)
	writeFile(outfilename)
	print("[+] 格式化完成")
	os.system("pause")