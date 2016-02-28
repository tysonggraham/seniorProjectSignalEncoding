import re
p = re.sub(r'zzyy(.+)zzyy', r'\1', 'zzyyldldlzzyy')
print(p)