def csRaindrops(number):
    return ''.join(f'Pl{v}ng' for d, v in ((3, 'i'), (5, 'a'), (7, 'o')) if number % d == 0) or str(number)
    

print(csRaindrops(28))
print(csRaindrops(30))
print(csRaindrops(34))

