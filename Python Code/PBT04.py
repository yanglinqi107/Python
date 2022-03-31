#程序名称：PBT04.py
#程序功能：展示变量对应得地址随值变化
def main():
	score = 85
	print("score的地址 = ",id(score))
	score = 95
	print("score的地址 = ",id(score))
	score += 5
	print("score的地址 = ",id(score))
main()