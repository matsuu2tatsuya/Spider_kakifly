import re

name_en = "Laurier's Experiment"
name_en2 = re.sub(r',', '', name_en)
print(re.sub(r"'", "\\'", name_en2))
