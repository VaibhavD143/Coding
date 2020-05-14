import math

class SegementTree():
	
	def __init__(self ,elems , ln_elems):
		self.elems = elems
		self.ln_elems = ln_elems

		
		#array to store segment tree
		#it is complete binary tree with remaining elements as 0
		self.ln_st= (2**(math.ceil(math.log2(self.ln_elems)+1))-1)
		self.st = [0]*self.ln_st
		self.lp = [0]*self.ln_st
		self.generate_st()

	def generate_st(self):
		
		#upd_n : no of elements need to be updated
		#sind : starting index from where updation will start
		upd_n = self.ln_elems
		sind = self.ln_st//2
		#all the elements will be leaf nodes
		self.st[sind:sind+self.ln_elems] = self.elems 

		upd_n = upd_n//2+1 if upd_n&1 else upd_n//2
		sind = sind//2

		#iterates through only required nodes leaving root node
		while sind:
			
			for i in range(sind,sind+upd_n):
				self.st[i] = self.st[2*i+1]+self.st[2*i+2]
			
			upd_n = upd_n//2+1 if upd_n&1 else upd_n//2
			sind = sind//2
		
		#to update root node
		self.st[0] = self.st[1]+self.st[2]

		
	# def get_sum(self,ss,se):
	# 	# n : index from where actual elements start
	# 	# ss : starting index of range
	# 	# se : ending index of range
	# 	# add : sum of range
	# 	"""
	# 	  10
	# 	/   \
	# 	6		4
	# 	/ \\  / \
	# 	2	4 1	  3
	# 	if ss is '4' or if se is '1' then include
	# 	if se is '2' or if se is '3' then don't include but include parent as both children in range
	# 	"""

	# 	n = self.ln_st//2
	# 	ss += n
	# 	se += n
	# 	add = 0
	# 	while ss <= se:

	# 		if not ss&1:
	# 			add += self.st[ss]
	# 		if se&1:
	# 			add += self.st[se]
				
	# 		ss = ss//2
	# 		se = se//2 - 1
	# 	return add

	def get_lst(self,st,ss,se):
		#if list of nodes needed
		n = len(st)//2
		ss += n
		se += n
		lst = []
		while ss <= se:
			if not ss&1:
				lst.append(ss)
			if se&1:
				lst.append(se)
			
			ss = ss//2
			se = se//2 - 1
		
		return list(set(lst))

	def get_sum(self,ss,se):
		
		if se<ss:
			se,ss = ss,se
		return self.get_sumUtil(ss,se,0,0,self.ln_st//2)
	
	
	def get_sumUtil(self,ss,se,ind,sr,er):
		"""
    ss = asked sum starting range
    se = asked sum ending range
		ind = current node index
		sr = starting range of that node
		er = ending range of that node
		"""
		#if any pending lazy updates present then first complete it
		if self.lp[ind] != 0:
			self.st[ind] += (er-sr+1)*self.lp[ind]

			if sr!=er:
				self.lp[ind*2+1] += self.lp[ind]
				self.lp[ind*2+2] += self.lp[ind]
			self.lp[ind] = 0

		#if it goes out of asked range
		if sr > er or ss>er or se<sr:
			return 0

		if ss<=sr and er<=se:
			return self.st[ind]
		
		mid = (sr+er)//2
		return self.get_sumUtil(ss,se,2*ind+1,sr,mid)+self.get_sumUtil(ss,se,2*ind+2,mid+1,er)

	"""
	us & ue : update indices starts and ends both inclusive
	val : value needs to be added to given range
	ind : current index node
	sr & se : starting and ending indices of sum current node contains
	"""

	def update_rangeUtil(self,us,ue,val,ind,sr,er):
		
		#if any pending lazy updates present then first complete it
		if self.lp[ind] != 0:
			self.st[ind] += (er-sr+1)*self.lp[ind]

			if sr!=er:
				self.lp[ind*2+1] += self.lp[ind]
				self.lp[ind*2+2] += self.lp[ind]
			self.lp[ind] = 0

		#if it goes out of asked range
		if sr > er or us>er or ue<sr:
			return None

		#if sum range of current node comletely falls into asked range
		if us<=sr and ue>=er:
			self.st[ind] += (er-sr+1)*val

			if sr != er:
				self.lp[ind*2+1] += val
				self.lp[ind*2+2] += val
			return None
		#if overlap is there then devide it and proceed
		mid = (sr+er)//2
		self.update_rangeUtil(us,ue,val,2*ind+1,sr,mid)
		self.update_rangeUtil(us,ue,val,2*ind+2,mid+1,er)

		#as overlap occured update current node with sum of updated childrens
		self.st[ind] = self.st[2*ind+1]+self.st[2*ind+2]
	
	def update_range(self,us,ue,val):
		sr = 0
		er = (self.ln_st)//2
		print(sr,er)
		if us>er or ue<sr:
			print("invalid ranges")
			return None
		
		self.update_rangeUtil(us,ue,val,0,sr,er)


elems = [1,2,3,1,6]
ln_elms = len(elems)
t = SegementTree(elems,ln_elms)
print(t.st)
t.update_range(0,4,2)
print(t.st)
print(t.lp)
t.update_range(0,4,2)
print(t.st)
print(t.lp)
print(t.get_sum(0,2))
print(t.st)
print(t.lp)
