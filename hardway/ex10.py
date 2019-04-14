# coding:utf-8

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backalash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backalash_cat)
print(fat_cat)

"""
字符串中间的 转义字符
\\ = \
\n = 换行
\t = 水平制表符，tab
\v = 垂直制表符
\' = '
\" = "
\r = ASCII 回车符
\a = 响铃符
\b = 退格符
\oss = 值为 8 进制的 ss 的字符
\xhh = 值为 16 进制 hh 的字符
\uxxxx = 值为 16 位十六进制 xxxx 的字符
\Uxxxxxxxx = 值为 32 位十六进制 xxxx 的字符
"""
