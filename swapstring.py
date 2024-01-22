def char_mix_up(a,b):
    new_a=b[0]+a[1:]
    new_b=a[0]+b[1:]
    return new_a+new_b
print(char_mix_up('hello\t','world'))
