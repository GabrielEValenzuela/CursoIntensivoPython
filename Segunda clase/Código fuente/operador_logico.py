var1 = True 
var2 = False

if (var1 and var2):
    print('Ambas True')
else:
    print('var1',var1)
    print('var2',var2)

if (var1 or var2):
    print('Alguna es verdad')

if (var1 and not var2):
    print('Ahora son verdad')

if (var1 ^ var2):
    print('var1 XOR var2')