class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [(((f"{i}","Fizz")[i%3==0],"Buzz")[i%5==0],"FizzBuzz")[i%3==0 and i%5==0] for i in range(1,n+1)]
