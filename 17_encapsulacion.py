class MyCounter:
    __secretCount = 0

    def __internal_count(self):
        self._secretCount += 1

    
    def count(self):
        self.__internal_count()
        print(self.__secretCount)
        
counter = MyCounter()
counter.count()
counter.count()
counter.count()

counter.__internal_count()