# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/AMR15A

if __name__ == '__main__':
    N = int(input())
    soldiers = map(int, input().split(" "))
    lucky = 0
    for weapons in soldiers:
        if weapons % 2 == 0:
            lucky += 1
    print("READY FOR BATTLE" if lucky > N - lucky else "NOT READY")
