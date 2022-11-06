import random

def game():
	while True:
		user=input("가위, 바위, 보 중 하나를 입력하세요 : ")
		if user=='가위':
			if random.choice(["가위","바위","보"])=="가위":
				return False
			elif random.choice(["가위","바위","보"])=="바위":
				return False
			else:
				return True
		if user=='바위':
			if random.choice(["가위","바위","보"])=="가위":
				return True
			elif random.choice(["가위","바위","보"])=="바위":
				return False
			else:
				return False
		if user=='보':
			if random.choice(["가위","바위","보"])=="가위":
				return False
			elif random.choice(["가위","바위","보"])=="바위":
				return True
			else:
				return False
		print("** 이상한 값을 입력했군요! 가위, 바위, 보 중 하나를 입력하세요!")


print("게임을 시작합니다! 상금 100만원을 획득하세요.")
user_money = 50000

print("현재 당신의 소지금은 {}원 입니다.".format(str(user_money)))

print("3판의 게임을 시작합니다.")
for i in range(1,4):
	betting_money=int(input("{}번째 게임입니다. 배팅 금액을 입력하세요. : ".format(str(i))))

	while True:
		if(betting_money > user_money):
			print("현재 당신의 소지금은 {}원 입니다.".format(str(user_money)))
			print("당신의 소지금보다 큰 금액을 걸 수는 없습니다.")

			betting_money=int(input("{}번째 게임입니다. 배팅 금액을 입력하세요. : ".format(str(i))))
		else:
			print("{}원을 걸었습니다. 게임을 시작합니다.".format(str(betting_money)))
			break

	res = game()

	if(res):
		print("게임을 이겼습니다. 베팅 금액을 받습니다.")
		user_money += betting_money
		print("현재 당신의 소지금은 {}원 입니다.".format(str(user_money)))
	else:
		print("게임에서 졌습니다. 베팅 금액이 차감됩니다.")
		user_money -= betting_money
		print("현재 당신의 소지금은 {}원 입니다.".format(str(user_money)))

	if(user_money<=0):
		print("당신은 파산하였습니다.")
		print("게임을 종료합니다...")
		exit()


print("3판의 게임이 모두 끝났습니다.")
print("당신의 최종 상금은 {}원입니다.".format(str(user_money)))

if(user_money > 1000000):
	print("WOW... 당신은 타고난 해커군요. :)")
else:
	print("고정 관념을 깨고 새로운 시선으로 바라보세요!")


