# -*- coding: UTF-8 -*-
pageIndex = 1
pageSize = 10
rowsCount = 100

if rowsCount % pageSize == 0:
    pageCount = rowsCount / pageSize
else:
    pageCount = rowsCount / pageSize + 1

print pageCount

startIndex = pageIndex * pageSize
print startIndex

endIndex = startIndex + pageSize - 1
print endIndex

for i in range(0,101):
    print  i

import urllib

print "userName:" + urllib.unquote('%E5%A4%9A%E5%A4%A7%E7%82%B9%E4%BA%8B')