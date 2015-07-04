"""Single-byte XOR cipher"""

import cryptopals
import etaoin_shrdlu

xored_hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}\\/;:"\'<>,.? '

results = {}
scores = {}

for c in characters:
    results[c] = cryptopals.single_char_xor(xored_hex_string, c)
    scores[c] = etaoin_shrdlu.score(results[c])

# top_5 = sorted(scores.items(), key=lambda x:x[1], reverse=True)[:5]
#
# for k,v in top_5:
#     print k + ' (' + str(v) + '): ' + results[k]

key = max(scores.items(), key=lambda x:x[1])[0]
message = cryptopals.single_char_xor(xored_hex_string, key)

print 'Key: ' + key
print 'Message: ' + message

