## unbreakable_encryption.py 

I've added some extra demo print message to show the interim output and help illustrate the underlying logic:
```
[~/projects/classic-problems-python/chap1-small-problems/one-time-pad] # cat unbreakable_encryption.py 
from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy  # XOR
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length()+ 7) // 8, "big")
    return temp.decode()

if __name__ == "__main__":
    secret_message="One Time Pad!"
    # demo details
    print (len(secret_message))  # returns 13 
    print (secret_message.encode()) # returns b'One Time Pad!'
    print (int.from_bytes(secret_message.encode(),"big")) # covert to byte string
    print (random_key(13))      # returns a large random int as key e.g. 6154541039554383958708625107655 
    # core logic
    key1, key2 = encrypt(secret_message)
    print (key1,key2)
    result: str = decrypt(key1, key2)
    print(result)
```
and running this a few times
```
[~/projects/classic-problems-python/chap1-small-problems/one-time-pad] # python3.9  unbreakable_encryption.py 
13
b'One Time Pad!'
6293190443887862498352498304033
12237542929132684704067532518596
One Time Pad!
[~/projects/classic-problems-python/chap1-small-problems/one-time-pad] # python3.9  unbreakable_encryption.py 
13
b'One Time Pad!'
6293190443887862498352498304033
9095741776565852524947512051975
16753392744492252874690256551477 12368032317578397235055360268820
One Time Pad!
[~/projects/classic-problems-python/chap1-small-problems/one-time-pad] # python3.9  unbreakable_encryption.py 
13
b'One Time Pad!'
6293190443887862498352498304033
14066060077657624843699762854542
1080517044229590774256848507289 5292565868167098746197904192952
One Time Pad!
[~/projects/classic-problems-python/chap1-small-problems/one-time-pad] # python3.9  unbreakable_encryption.py 
13
b'One Time Pad!'
6293190443887862498352498304033
6510410509514921312771405634081
4571572119857951089442145940930 9417608239374489911085777211875
One Time Pad!
```
the main points here are
* our secret string 'One Time Pad!' has 13 character and b'One Time Pad!' is the form of this string
* we can convert our secret string to an int via the int.from_bytes(b'One Time Pad!') which returns 6293190443887862498352498304033
* we create a first key (key1) by the random_key(<input_lenght_of_message>)
* we create the second key by (key2) via an XOR operation
* the two keys are useless on their own, but together the XOR encryption operation can be reversed i.e. the decrypt() method


NB The decrypted.to_bytes() working are still a bit of a mystery to me ;)