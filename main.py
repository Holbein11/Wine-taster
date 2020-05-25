clarity = input('clear - hazy\n')

intensity = input('pale - medium - deep\n')

colour = input('lemon-green - lemon - gold - amber - brown - pink - salmon - orange - onion skin - purple - ruby - garnet - tawny - brown\n')

print ('Appearance is %s, %s, %s'% (clarity,intensity,colour))

condition = input('clean, unclean\n')
intensity = input('light, medium -, medium +, pronounced\n')
aromas = input('delicate, intense, simple, complex, generic, well defined, fresh, cooked, under-ripe, ripe, overripe\n')
print('On the nose condition is %s, with %s intensity and %s aroma characteristics'%(condition,intensity,aromas))

sweetness = input('dry, off-dry, medium, dry, medium-sweet, sweet, luscious\n')
acidity = input('low, medium-, medium+, high\n')
tannin = input('no, low, medium-, medium, medium+, high, well-integrated, soft, ripe, stalky, green, course, fine-grained\n')
alcohol = input('low, medium-, medium, medium+, high\n')
body = input('light, medium-, medium, medium+, full\n')
flavintensity = input('light, medium-, medium, medium+, pronounced\n')
flavprimary = input('lemon, orange, lime, grapefruit, apple, pear, gooseberry, rose, violet, acacia, blossom, peach, apricot, passion fruit, pineapple, mango, melon, lychee, redcurrent, raspberry, strawberry, red cherry, red plum, blackcurrent, blackberry, fig, raisin, sultana, jamminess, preserved fruits, green bell pepper, grass, tomato leaf, asparagus, blackcurrent leaf, eucalyptus, mint, garrigue, black white pepper, liquorice, ginger, flint, wet stones, wet wool, wax, rubber, green olive, black olive tapenade\n')
yeast = input('biscuit, bread, toast, yoghurt\n')
MLF = input('butter, cream, yoghurt\n')
oak = input('vanilla, nutmeg, coconut, toast, cedar, charred wood, smoke, chocolate, coffee')
oxidative = input('almond, coconut, hazelnut, chocolate, coffee, toffee, caramel')
fruit = input('dried apricot, fig, prune, tar, truffle\n')
age = input('petrol, cinammon, ginger, nutmeg, toast, nutty, cereal, mushroom, honey, leather, forest floor, earth, mushroom, cedar, tobacco, meaty, savoury, farmyard\n')
finish = input('short, medium-, medium, medium+, long\n')

print('On the palate the wine %s, with %s acidity, %s tannin, %s alcohol, %s body and %s intensity. There are flavours of %s\n '%(sweetness, acidity, tannin, alcohol, body, flavintensity, flavprimary, yeast, MLF, oak, oxidative, fruit, age))