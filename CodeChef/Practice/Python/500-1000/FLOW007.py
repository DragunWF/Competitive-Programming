# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW007

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = [*input()]
        n.reverse()
        print(int("".join(n)))
