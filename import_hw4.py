from hw4 import Отец
from hw4 import Сын
from hw4 import Друг
from hw4 import Мама

class Сосед(Друг,Отец,Сын,Мама):

    def __init__(self,name, age):
        super().__init__(name)
        super().__init__(age)


    @property
    def age(self):
        return self._age
