#-*- coding:utf-8 -*-
import requests
import json
import re
import argparse
import random
import os
import sys
import chardet
from urllib.parse import quote,unquote,quote_plus
from time import sleep
#from collections import deque

os.environ['NO_PROXY'] = 'www.paperyy.com'

config = {
	# 可自由配置的选项
	'maxnum' : 2,	# 指定一个账号的最大降重次数
	'reponame' : 'repo.txt',	# 报告记录文件
	'sentencename' : 'sentence.txt',	# 待降重文本文件
	'cutlength': 400,	# 指定每次降重的字数，最大为400字

	# paperyy的降重url
	'url_reduce' : 'https://www.paperyy.com/api/v1/reduce/reduce-sentence/',
	'headers_reduce' : {
		'Host': 'www.paperyy.com',
		'Content-Length': '',
		'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
		'Accept': 'application/json, text/javascript, */*',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Sec-Ch-Ua-Mobile': '?0',
		'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10',
		'Sec-Ch-Ua-Platform': '"Windows"',
		'Origin': 'null',
		'Sec-Fetch-Site': 'cross-site',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'close'
	},
	'data_reduce' : {
		'sentence':''
	},
	
	# 抓包测试时使用
	'proxies':{
		'http':'http://127.0.0.1:8080',
		'https':'http://127.0.0.1:8080'
	},
	
	#'proxies' : { "http": None, "https": None}
}

def logo():
	print("[+] 欢迎使用降重程序")
	logo = '''\
            _____                      _______           
           /\    \                    /  \    \          
          /  \____\                  /    \    \         
         /    |   |                 /      \    \        
        /     |   |                /        \    \       
       /      |   |               /   /--\   \    \      
      /   /|  |   |              /   /    \   \    \     
     /   / |  |   |             /   /    / \   \    \    
    /   /  |  |___|______      /   /____/   \   \____\   
   /   /   |        \    \    |   |    |     |   |    |  
  /   /    |         \____\   |   |____|     |   |    |  
  \  /    / -----/   /    /    \   \    \   /   /    /   
   \/____/      /   /    /      \   \    \ /   /    /    
               /   /    /        \   \    /   /    /     
              /   /    /          \   \__/   /    /      
             /   /    /            \        /    /       
            /   /    /              \      /    /        
           /   /    /                \    /    /         
          /   /    /                  \  /____/          
          \  /    /                    --                
           \/____/                              v1.2.3   
 '''
	print(logo)
	print("[+] 降重程序启动")

# 检查打开的文本编码
def checkCode(str):
	adchar = chardet.detect(str)
	# 由于windows系统的编码可能为Windows-1254,打印后是乱码,因此不直接用adchar['encoding']编码
	#if adchar['encoding'] is not None:
	# str = str.decode(adchar['encoding'], "ignore")
	if adchar['encoding'] == 'gbk' or adchar['encoding'] == 'GBK' or adchar['encoding'] == 'GB2312':
		str = str.decode('GB2312', "ignore")
	else:
		str = str.decode('utf-8', "ignore")
	return str

# 读取记录
def readRepo(filename):
	print("[+] 读取报告")
	if os.path.isfile(filename):
		#with open(filename, 'r', encoding='utf-8') as f:
		with open(filename, 'rb') as f:	# 以二进制的形式读取文本
			global repo
			repo = f.read() #f.readlines()	# 二进制的文本
			repo = checkCode(repo)	# 检查编码并返回解码后的字符串
			repo = repo.splitlines()	# 去除回车，返回列表
			#print(repo)
	else:
		print("[-] 报告记录文件不存在")
		f = open(filename,'w')
		f.close()
		print("[+] 已创建报告记录文件，请向文件内写入指定内容")
		print("[+] 例如：https://report3.paperyy.com/20220101/3-aaaaaaaa-7777-8888-9999-111111111111/report.zip")
		os.system("pause")
		sys.exit(1)

# 读取文本
def readSentence(filename, length):
	print("[+] 读取文本")
	if os.path.isfile(filename):
		with open(filename, 'rb') as f:
			global sentencelines
			sentence = f.read()
			sentence = checkCode(sentence)
			sentence = sentence.splitlines()	# 去除回车，返回列表
			sentence = ''.join(sentence)	# 将列表拼接成一行，可能多于400字
			sentencelines = cutSentence(sentence, length)	# 按照长度为400分割字符串
	else:
		print("[-] 待降重文件不存在")
		f = open(filename,'w')
		f.close()
		print("[+] 已创建待降重文件，请向文件内写入指定内容")
		print("[+] 例如：欢迎使用批量降重工具，这个文本是用于降重的内容")
		os.system("pause")
		sys.exit(1)
	
# 按照指定长度分割字符串
def cutSentence(sentence, length): 
	array = re.findall('.{'+str(length)+'}', sentence) # 都为400字的列表
	array.append(sentence[(len(array)*length):]) # 最后小于400字的部分也添加进列表
	return array

# 写入降重文件
def writeReduceSentence(reduceSentence):
	print("[+] 写入降重文件")
	with open('reduceSentence.txt', 'a+') as f:
		f.write(reduceSentence)

# 写入未降重文件
def writeNotReduceSentence(reduceSentence):
	print("[+] 写入未降重文件")
	with open('notReduceSentence.txt', 'w+') as f:
		f.write(reduceSentence)

# 每次只降重400字
def getTranslation(sentence, repoId):
	config['data_reduce']['sentence'] = sentence
	url = config['url_reduce'] + str(repoId)
	#response = requests.post(url = url , headers = config['headers_reduce'], data = config['data_reduce'], timeout=(10,20), verify=False, proxies = config['proxies'])	#用于抓包测试
	response = requests.post(url = url , headers = config['headers_reduce'], data = config['data_reduce'], timeout=(10,20))	#data = json.dumps(data)
	#response = '{"code":-2004,"msg":"每篇报告仅支持免费体验2次","data":"2","time":1600000000000}'
	#response = '{"code":0,"msg":"降重成功","data":"哈哈哈","time":1600000000000}'
	if response.status_code == 200:
		response = response.text
		code = json.loads(response)['code']
		msg = json.loads(response)['msg']
		if code == 0:
			print("[+] " + str(msg))
			reduceSentence = json.loads(response)['data']
			print("[+] 已降重文本为")
			reduceSentence = unquote(reduceSentence, encoding="utf-8") # 将url编码转中文
			print(reduceSentence)
			writeReduceSentence(reduceSentence)
			sentencelines.pop(0)	# 降重成功则弹出最开头的文本
		else:
			print("[-] " + str(msg))
	else:
		print("[-] 请求降重失败")

# 写入编码文件，测试
def writeTemp(temp):
	with open('temp.txt', 'a+') as f:
		f.write(temp)

if __name__ == '__main__':
	logo()
	maxnum = int(config['maxnum'])	# 指定一个账号的最大降重次数，实际此时取num和sentencelines列表个数中的较小者
	reponame = str(config['reponame'])	# 报告记录文件
	sentencename = str(config['sentencename'])	# 文本文件
	readRepo(reponame)	# 读取报告
	readSentence(sentencename, int(config['cutlength']))	# 待降重文本，返回列表sentencelines，按照长度为400分割字符串
	i = 1	# 从1开始，用于显示第几次降重
	flagSentencelines = 1	# 判断是否还有内容,1为有
	for repoline in repo:	# 获取报告中的记录号
		if not sentencelines:	# 如果没有降重的内容则退出
			break
		repoline = repoline.strip()
		repoline = re.search(r'(\d+)\/(.*)\/report.zip', repoline, re.I)
		if repoline:
			repoline = str(repoline.group(2))
			print("[+] 记录号：" + repoline)
			num = maxnum	# 重置查询次数
			for temp in range(0,maxnum):	# 取两次
				if not sentencelines:	# 如果没有降重的内容则退出
					break
				line = sentencelines[0]	# 每次只取最开头
				sleep(random.uniform(1,3))  # 强制等待,随机1~3秒再执行下一步
				if num > 0:
					print("[+] 第" + str(i) + "次降重")
					#print(sentencelines)
					print("[+] 待降重文本为")
					print(line)
					#line = quote(line, safe="") # 将中文转url编码， 例如转成%EA,不转特殊字符,safe=""代表量/都编码
					#writeTemp(line)	# 写入编码后的文件
					#config['headers_reduce']['Content-Length'] = str(len(line))	# 计算文本长度
					#line = quote_plus(line) # 将中文转url编码， 例如转成%EA, 会将空格转为+
					#line = line.replace('+', '%20')	# 将空格编码为%20
					#print("[+] 编码后文本长度: " + config['headers_reduce']['Content-Length'])
					getTranslation(line, repoline)	# 降重文本
				else:
					break
				num -= 1
				i += 1
		else:
			print("[-] 报告记录无效")
	if sentencelines:	# 有未降重的内容则退出
		reduceSentence = ''.join(sentencelines)
		writeNotReduceSentence(reduceSentence) # 将没有降重的文本写入文件
	print("[+] 结束")
	os.system("pause")
