import collections
import pprint
file_input = input('File Name:')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)

print(value)
