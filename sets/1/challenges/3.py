"""Single-byte XOR cipher"""

import cryptopals
import etaoin_shrdlu

xored_hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

results = {}
scores = {}

for c in range(0, 255):
    char = chr(c)
    results[char] = cryptopals.single_char_xor(xored_hex_string, char)
    scores[char] = etaoin_shrdlu.score(results[char])

# top_5 = sorted(scores.items(), key=lambda x:x[1], reverse=True)[:5]
#
# for k,v in top_5:
#     print k + ' (' + str(v) + '): ' + results[k]

key = max(scores.items(), key=lambda x:x[1])[0]
message = cryptopals.single_char_xor(xored_hex_string, key)

print 'Key: ' + key
print 'Message: ' + message

