nums=[5,8,9,11]
it=iter(nums)

for item in nums:
    print(it.__next__())

class TopTen:

    def __init__(self):
        self.num=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
        else:
            raise StopIteration


values=TopTen()

print(next(values))

print(values.__next__())