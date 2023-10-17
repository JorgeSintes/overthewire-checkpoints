import base64
import binascii

encoded_secret = "3d3d516343746d4d6d6c315669563362"


def decode_secret(secret: str):
    bin_secret = str(binascii.unhexlify(secret))
    reversed_bin = bin_secret[::-1]
    return base64.b64decode(reversed_bin)


print(decode_secret(encoded_secret))
