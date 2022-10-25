# def name(input):
#     print("제 이름은 " + input + "입니다.")
# name('은비')

# def sum(a,b):
#     return a+b
# total = sum(3,4)
# print(total)


def grade(score, name):
    if score >= 90:
        print(name + "의 등급은 A입니다.")
    elif score >= 80:
        print(name + "의 등급은 B입니다.")
    elif score >= 70:
        print(name + "의 등급은 C입니다.")
    elif score >= 60:
        print(name + "의 등급은 D입니다.")
    else:
        print(name + "의 등급은 F입니다.")

grade(65,'은비')