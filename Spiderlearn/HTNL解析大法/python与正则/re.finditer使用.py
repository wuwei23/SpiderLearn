#搜索整个string，以迭代器形式返回能匹配到的全部Match对象
import re
pattern = re.compile(r'\d+')
matchiter = re.finditer(pattern,'A1B2C3D4')
for match in matchiter:
    print(match.group())