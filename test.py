from __future__ import print_function

from os import urandom

from Crypto.Cipher import AES

from bit_flipper import *
from paddings import *

key = urandom(16)
iv = urandom(16)


def step(name):
    n = (78 - len(name)) / 2
    print("\n" + n * "#" + " " + name + " " + n * "#" + "\n")


def test():
    aes = AES.new(key, AES.MODE_CBC, iv)

    step("Encryption AES-CBC-128")

    cleartext = "name=jcconvenant;photo=picture.jpg;admin=false;colour=red;"
    print("Cleartext       :", cleartext, "(len=%d)" % len(cleartext))

    cleartext = pad(cleartext, AES.block_size, Padding.Zero)
    ciphertext = aes.encrypt(cleartext)
    print("Ciphertext      :", ciphertext.encode("hex"))

    step("BitFlipping")

    dolphin = BitFlipper(ciphertext, cleartext, block_size=AES.block_size)
    dolphin.flip("false", "true;")
    flipped_ciphertext = dolphin.get_ciphertext()
    print("New ciphertext  :", flipped_ciphertext.encode("hex"))

    step("Decryption")

    decrypted = aes.decrypt(flipped_ciphertext)
    print("Decrypted       :", decrypted)

    step("Test")

    print("Test OK         :", str(decrypted.find("admin=true;") != -1))


if __name__ == '__main__':
    print()
    print("TEST - AES-CBC - Bit Flipping Attack")

    test()
