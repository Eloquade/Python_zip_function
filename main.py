list1 = [1, 2, 3, 4, 5, 6]
list2 = ['one', 'two', 'three', 'four', 'five', 'six']

zipped = list(zip(list1, list2))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

for l1, l2 in zip(list1, list2):
    print(l1)
    print(l2)

items = ['apple', 'banana', 'grapes']
quantity = ['1', '2', '3']
prices = ['123', '312', '354']
sentences = []


for (items, quantity, prices) in zip(items, quantity, prices):
    items, quantity, prices = str(items), str(quantity), str(prices)
    sentence = 'i bought ' + quantity + ' ' + items + 's at ' + prices + '.'
    sentences.append(sentence)
    print(sentences)
# for i1, q1, p1 in zip(items, quantity, prices):
#     # print(i1, q1, p1)
#     # print(items, quantity, prices)
#     print(i1)
#     print(q1)
#     print(p1)


