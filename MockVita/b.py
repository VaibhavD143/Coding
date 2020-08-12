class kart:
    def __init__(self):
        # self.inv = {'SHIRT':0,'SHOE':0}
        self.inv = {}
        # self.cost = {'SHIRT':-1,"SHOE":-1}
        self.cost = {}
        # self.kart = {'SHIRT':0,'SHOE':0}
        self.kart = {}
    
    def sm_add(self,item,qty):
        if int(qty) != qty or qty<=0 or item in self.inv:
            return -1
        qty = int(qty)
        self.inv[item] =qty
        return qty
    
    def sm_remove(self,item):
        if item not in self.inv:
            return -1
        del self.inv[item]
        return 1
    
    def sm_get_qty(self,item):
        if item not in self.inv:
            return 0
        return self.inv[item]
    
    def sm_inc(self,item,qty):
        if int(qty) != qty or qty<=0 or item not in self.inv:
            return -1
        qty = int(qty)
        self.inv[item]+=qty
        return qty
    
    def sm_dec(self,item,qty):
        if int(qty) != qty or qty<=0 or item not in self.inv:
            return -1
        qty = int(qty)
        self.inv[item]-=qty
        if self.inv[item] == 0:
            del self.inv[item]
        return qty
    
    def sm_set_cost(self,item,cost):
        # if item not in self.inv:
        #     return -1

        self.cost[item] = cost
        return cost
    
    def s_add(self,item,qty):
        if int(qty) != qty or qty<=0 or item in self.kart:
            return -1
        qty = int(qty)
        self.kart[item]=qty
        return qty
    
    def s_remove(self,item):
        if item not in self.kart:
            return -1
        del self.kart[item]
        return 1
    
    def s_inc(self,item,qty):
        if int(qty) != qty or qty<=0 or item not in self.kart:
            return -1
        qty = int(qty)
        self.kart[item]+=qty
        return qty

    def s_dec(self,item,qty):
        if int(qty) != qty or qty<=0 or item not in self.kart:
            return -1
        qty = int(qty)
        self.kart[item]-=qty
        if self.kart[item] == 0:
            del self.kart[item]
        return qty
    
    def s_get_amount(self):
        # print(self.kart)
        # print(self.cost)
        sm = 0
        for i in self.kart:
            if i in self.kart and (i not in self.inv or i not in self.cost):
                return -1
            sm+=(self.kart[i]*self.cost[i])
        return round(sm,2)

for _ in range(int(input())):
    obj = kart()
    while True:
        s = input().split()
        if s[0] == "END":
            break
        if s[1] == "SM":
            if s[2] == "ADD":
                print(obj.sm_add(s[3],float(s[4])))
            elif s[2] == "REMOVE":
                print(obj.sm_remove(s[3]))
            elif s[2] == "GET_QTY":
                print(obj.sm_get_qty(s[3]))
            elif s[2] == "INCR":
                print(obj.sm_inc(s[3],float(s[4])))
            elif s[2] == "DCR":
                print(obj.sm_dec(s[3],float(s[4])))
            elif s[2] == "SET_COST":
                print(obj.sm_set_cost(s[3],float(s[4])))
            else:
                print(-1)
        elif s[1] == "S":
            if s[2] == 'ADD':
                print(obj.s_add(s[3],float(s[4])))
            elif s[2] == 'REMOVE':
                print(obj.s_remove(s[3]))
            elif s[2] == "INCR":
                print(obj.s_inc(s[3],float(s[4])))
            elif s[2] == "DCR":
                print(obj.s_dec(s[3],float(s[4])))
            elif s[2] == "GET_ORDER_AMOUNT":
                print(obj.s_get_amount())
            else:
                print(-1)
        