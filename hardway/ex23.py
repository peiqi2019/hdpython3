# coding=utf-8

import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
  line = language_file.readline()
  if line:
    print_line(line, encoding, errors)
    return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
  next_lang = line.strip()
  raw_bytes = next_lang.encode(encoding, errors = errors)
  cooked_string = raw_bytes.decode(encoding, errors = errors)

  print(raw_bytes, "<====>", cooked_string)

print(sys.stdout.encoding)
print(sys.getdefaultencoding())

languages = open("hardway/languages.txt", encoding = "utf-8")

main(languages, encoding, error)

"""
命令行里面运行：
这里推荐用Cmder 运行，其他终端可能编码有错，或者显示不全
python hardway/ex23.py utf-8 strict
"""

