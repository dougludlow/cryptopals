"""Fixed XOR."""

import cryptopals

input_string1 = '1c0111001f010100061a024b53535009181c'
input_string2 = '686974207468652062756c6c277320657965'
solution = '746865206b696420646f6e277420706c6179'
result = cryptopals.fixed_xor(input_string1, input_string2)

print solution
print result
print solution == result




