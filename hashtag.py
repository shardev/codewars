def generate_hashtag(s):
    outStr = ''.join(map(str, s.strip().title().split()))
    l = len(outStr)
    if len(outStr) > 140 or len(s) == 0 or len(outStr) == 0:
        return False
    else:
        return '#' + outStr

# 1
print(generate_hashtag(" Hello there thanks for trying my Kata"))

# 2
print(generate_hashtag('Loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))