class Jar:
    def __init__(self, capacity=12):
        self._capacity=capacity
        if capacity<0:
             raise ValueError
        self.cookieNo=0

    def __str__(self):
        cookies="🍪"*self.cookieNo
        return cookies

    def deposit(self, n):
        if (self.cookieNo+n)>self.capacity:
            raise ValueError
        self.cookieNo+=n

    def withdraw(self, n):
        if n > self.cookieNo:
            raise ValueError
        self.cookieNo -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookieNo

jar1=Jar()
print(jar1)
