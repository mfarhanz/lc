class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # ugly solution, but good MLE and TLE; this was kind of hard
        s = [asteroids[0]]
        i = 0
        while True:
            if i == len(asteroids) - 1:
                break
            if not s:
                s.append(asteroids[i+1])
            else:
                if asteroids[i+1] < 0 and s[-1] > 0:
                    a1, a2 = abs(s[-1]), abs(asteroids[i+1])
                    if a1 < a2:
                        s.pop()
                        s.append(asteroids[i+1])
                        while True:
                            if len(s) == 1 or len(s) < 2:
                                break
                            s1 = abs(s[-2])
                            if s[-2] > 0:
                                if s1 >= a2:
                                    if s1 == a2:
                                        s.pop(-2)
                                    s.pop()
                                    break
                                else:
                                    s.pop(-2)
                            else:
                                break
                    elif a2 == a1:
                        s.pop()
                else:
                    s.append(asteroids[i+1])
            i += 1
        return s
