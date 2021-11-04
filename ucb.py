import numpy as np
import random


np.random.seed(0)
n_arms = 7

# def sim(Agent, N=1000, T=1000, **kwargs):

# 	selected_arms =[[0 for _ in range(T)] for _ in range(T)]
# 	earned_rewards =[[0 for _ in range(T)] for _ in range(T)]

# 	for n in range(N):
# 		agent = Agent(**kwargs)
# 		for t in range(T):
# 			arm = agent.get_arm()
# 			reward = Env.react(arm)
# 			agent.sample(arm, reward)
# 			selected_arms[n][t] = arm
# 			earned_rewards[n][t] = reward
# 	return np.array(selected_arms), np.array(earned_rewards)



# class Env(object):
# 	a = np.random.randn(1)
# 	b = np.random.randn(1)

# 	thetas = [a, b]

# 	def react(arm):
# 		return 1 if np.random.random() < Env.thetas[arm] else 0

# 	def opt():
# 		return np.argmax(Env.thetas)

def get_article(filename):
	article = []
	with open(filename) as f:
		lines = f.readlines()

	for line in lines:
		article.append(line)

	return article

def ask_number(articles, num): 
	print('-' * 30)
	print('\n\n記事名：', articles[num], end='\n\n')
	interest = int(input('クリック1　スルー0 : '))
	print('-' * 30)

	return interest


class UCB(object):

	def __init__(self):
		self.counts = [0 for _ in range(n_arms)]
		# self.values = [0 for _ in range(n_arms)]
		self.values = [ np.random.randn() for _ in range(n_arms)]

	def calc_ucb(self, arm):
	  	# ucb = self.values[arm]
	  	ucb += np.sqrt(np.log(sum(self.counts)) / (2 * self.counts[arm]))
	  	return ucb

	# def get_arm(self):
	# 	if 0 in self.counts:
	# 	  arm = self.counts.index(0)
	# 	else:
	# 	  ucb = [self.calc_ucb(arm) for arm in range(n_arms)]
	# 	  arm = ucb.index(max(ucb))
	# 	return arm

	def sample(self, arm, reward):
		self.counts[arm] = self.counts[arm] + 1
		self.values[arm] = (
			(self.counts[arm] - 1 * self.values[arm] + reward) / self.counts[arm])

if __name__ == '__main__':
	obj = UCB()
	article_list = get_article('news.txt')
	ucb = obj.values

	print(ucb)

	for i in range(5):	
		num = random.randint(0, 7)
		print(num)
		interest = ask_number(article_list, num)

		# if 0 in obj.counts:
		#   # arm = obj.counts.index(0)
		#   arm = num
		# else:
		ucb += np.sqrt(np.log(sum(self.counts)) / (2 * self.counts[arm]))
		arm = ucb.index(max(ucb))

		print('armの値は', arm)
		print('UCBの値は', ucb)
