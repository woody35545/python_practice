# for ~ in ~ enmuerate(~)
# Enumerate: element의 Index와 element 값을 tuple로 반환

_list = ['a','b','c','d']

for index, element in enumerate(_list):
    print(f"[{index}]: {element}")

print("="*20)

for i in enumerate(_list):
    print(f"{i}")


