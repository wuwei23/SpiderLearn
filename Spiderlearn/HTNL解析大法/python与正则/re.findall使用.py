#搜索整个string，一列表形式返回能匹配到的全部字串
import re
pattern = re.compile(r'\d+')
print(re.findall(pattern,'A1B2C3D4'))