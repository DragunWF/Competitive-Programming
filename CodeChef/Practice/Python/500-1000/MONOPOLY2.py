# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MONOPOLY2

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        companies = list(map(int, input().split(" ")))
        is_monopoly = False
        for i, rupees in enumerate(companies):
            total = sum([companies[j]
                        for j in range(len(companies)) if j != i])
            if rupees > total:
                is_monopoly = True
                break
        print("YES" if is_monopoly else "NO")