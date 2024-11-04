# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BUILDINGRACE

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        a, b, x, y = map(int, input().split(" "))
        chef_speed = a / x
        chefina_speed = b / y
        if chef_speed > chefina_speed:
            print("Chefina")
        elif chef_speed < chefina_speed:
            print("Chef")
        else:
            print("Both")