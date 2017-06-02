
# -*- coding:utf-8 -*-



aStr = raw_input('请输入一串字符:')
 
str_num = 0
spac_num = 0
figue_num = 0
 
for strs in aStr:
    if strs.isalpha():
        str_num +=1
    elif strs.isdigit():
        figue_num +=1
    elif strs == ' ':
        spac_num +=1
    else:
        pass

print '英文字母有：%d' %str_num
print '数字有：%d'%figue_num
print '空格有：%d'%spac_num