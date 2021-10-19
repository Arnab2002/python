# abstruct class

from abc import*
class Ab(ABC):
    @abstractmethod
    def calc(self, x):
        pass
class Sq(Ab):
    def calc(self, x):
        print("The square of the value = ", x**2)
class Sqr(Ab):
    def calc(self, x):
        print("The square root of the value = ", x**(1/2))
class Cu(Ab):
    def calc(self, x):
        print("The cube of the value = ", x**3)
s = Sq()
s.calc(16)
s = Sqr()
s.calc(16)
s = Cu()
s.calc(16)