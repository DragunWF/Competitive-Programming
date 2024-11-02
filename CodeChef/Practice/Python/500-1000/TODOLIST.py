# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TODOLIST

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        d = map(int, input().split(" "))
        remove_count = 0
        for rating in d:
            if rating >= 1000:
                remove_count += 1
        print(remove_count)