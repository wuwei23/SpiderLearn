#按照能够匹配的字串将string分割后返回列表，马修split用于指定最大分割次数
#不指定则将全部分割
import re
pattern = re.compile(r'\d+')
print(re.split(pattern,'A1B2C3D4'))
#分割字串