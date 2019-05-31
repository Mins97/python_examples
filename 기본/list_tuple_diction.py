list = [ 'abcd', 786, 2.23, 'john']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list * 2)
print(list+list)

print("tuple과 list의 차이점은 불변성에 있다."
      "리스트는 가변적이며 튜플은 불변적이다.")
tuple = [ 'abcd', 786, 2.23, 'john']

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 2)
print(tuple+tuple)

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name':'john', 'code':6734, 'dept':'sales'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
