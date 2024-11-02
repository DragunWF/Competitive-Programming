# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/THREETOPICS

if __name__ == '__main__':
    a, b, c, x = map(int, input().split(" "))
    print("YES" if x in (a, b, c) else "NO")
