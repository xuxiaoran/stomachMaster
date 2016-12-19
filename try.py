#!/usr/in/python
# -*- coding: utf-8 -*-

import random
import itertools
import sys

class cai(object):
	def __init__(self, name, price, haveToOrder = False):
		self.name = name
		self.price = price
		self.haveToOrder = haveToOrder

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

class restaurant(object):
	def __init__(self, name, addr, phone, menu):
		self.name = name
		self.addr = addr
		self.phone = phone
		self.menu = menu

	def pick_helper(self, morePeople = False, item_class = cai):
		for d in self.menu:
			if isinstance(d, item_class) and d.haveToOrder and morePeople:
				yield d
			while  True:
				yield random.choice([d for d in self.menu if isinstance(d, cai)])

	def pick(self, n = 1, morePeople = False, item_class = cai):
		for i, j in itertools.izip(range(n), self.pick_helper(morePeople, item_class)):
			yield j


lailai = restaurant("来来", "4023 Carpenter Rd, Ypsilanti, MI", "734-677-0790", [
	cai("鱼香茄子煲", 12.95, haveToOrder = True),
	cai("黑椒牛柳", 15.95, None)
	])

kang = restaurant("Kang's Kitch", "1327 S University Ave, Ann Arbor, MI", "734-761-1327", [
	cai("bibimbop", 10.00, None)
	])

kungPoHouse = restaurant("宫爆小馆", "46042 Michigan Ave, Canton, MI", "734-495-1115", [
	cai("咸蛋黄豆腐", 8.99, haveToOrder = True),
	cai("孜然羊肉", 12.99, None)
	])

lizhan = restaurant("荔栈", "29505 W 9 Mile Rd, Farmington Hills, MI", "248-888-6866", [
	cai("金沙玉米", 0.00, haveToOrder = True)
	])



##################################          EDIT           #################################

Restaurants = [ lailai, kang, kungPoHouse, lizhan]

############################################################################################


if __name__ == "__main__":
	num = 1
	if len(sys.argv) == 1:
		print "default: eating alone"
	else:
		temp = sys.argv[1]
		if temp.isdigit():
			num = float(temp)
		else:
			print "Usage: %s Num_of_People" % sys.argv[0]
			sys.exit(1)

	goto = Restaurants[random.randint(0, len(Restaurants) - 1)]
	order = list(goto.pick(int(num), num > 1, cai))
	print order
	total = sum([i.price for i in order])
	print "Total: $%.02f" % total

	if num > 1:
		print "Average: $%.02f" % (total/int(num))
		