import sys
import functools

def cached(func):
    cache = {}
    def template(*args): #: template is wrapper; func is wrapped
        key = (func, )+args
        try:
            ret = cache[key]
        except KeyError:
            ret = func(*args)
            cache[key] = ret
        else:
            pass
        return ret

    functools.update_wrapper(template, func)
    return template

@cached
def lcs(str1, str2):
  if len(str1)==0 or len(str2)==0:
    return ''
  if str1[-1] == str2[-1]:
    return ''.join([lcs(str1[:-1], str2[:-1]), str1[-1]])
  else:
    candidate1 = lcs(str1[:-1], str2)
    candidate2 = lcs(str1, str2[:-1])
    if len(candidate1) >= len(candidate2):
      return candidate1
    else:
      return candidate2

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            print lcs(*line.split(';')).strip()
    sys.exit(0)
