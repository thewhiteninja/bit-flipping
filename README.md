# Bit Flipping attack (AES-CBC)
<div>
  <!-- Stability -->
  <a href="https://nodejs.org/api/documentation.html#documentation_stability_index">
    <img src="https://img.shields.io/badge/stability-experimental-orange.svg?style=flat-square"
      alt="API stability" />
  </a>
  <!-- Standard -->
  <a href="https://img.shields.io/badge">
    <img src="https://img.shields.io/badge/Language-Python-brightgreen.svg"
      alt="Python" />
  </a>
</div>
<br />

Python implementation of Bit Flipping attack on AES-CBC.

## Example

```sh
TEST - AES-CBC - Bit Flipping Attack

############################ Encryption AES-CBC-128 ############################

Cleartext       : name=jcconvenant;photo=picture.jpg;admin=false;colour=red; (len=58)
Ciphertext      : c26a5697689463d662f540e55e2a1ecef9c5df20133dfe49d6d3c369679a95ff4f4c5a490f530b2a2f25db40da64f1e9302724ce61b9a435e23f4d600252a143

################################# BitFlipping #################################

New ciphertext  : c26a5697689463d662f540e55e2a1ecef9c5df20133dfe49d6c1d07071c495ff4f4c5a490f530b2a2f25db40da64f1e9302724ce61b9a435e23f4d600252a143

################################## Decryption ##################################

Decrypted       : ¶ä╚°  h8ì│►Nƒz│Ioé¤ßkü2KÀQiý4I@pg;admin=true;;colour=red;

##################################### Test #####################################

Test OK         : True
```

