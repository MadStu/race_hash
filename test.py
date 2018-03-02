import race_hash
from binascii import unhexlify, hexlify

import unittest

# race block #1
# race@w1:~$ race-cli getblockhash 1
# 0000025a82ddff8f3df5368230851f73fa3ffd1ca3a1e8b7c843f3ab0f41fd9e
# race@alt-w1:~$ race-cli getblock 0000025a82ddff8f3df5368230851f73fa3ffd1ca3a1e8b7c843f3ab0f41fd9e
# {
#   "hash": "0000025a82ddff8f3df5368230851f73fa3ffd1ca3a1e8b7c843f3ab0f41fd9e",
#   "confirmations": 25782,
#   "size": 179,
#   "height": 1,
#   "version": 536870912,
#   "merkleroot": "8592f77abb36764f79df13cae0959b7141acbfae2cac0ed4473415de4e94a2c6",
#   "tx": [
#     "8592f77abb36764f79df13cae0959b7141acbfae2cac0ed4473415de4e94a2c6"
#   ],
#   "time": 1517466847,
#   "mediantime": 1517466847,
#   "nonce": 73407,
#   "bits": "1e0ffff0",
#   "difficulty": 0.000244140625,
#   "chainwork": "0000000000000000000000000000000000000000000000000000000000200020",
#   "previousblockhash": "00000addc7843f4febe1850ff1602af6f7fca2fc3c8cefaeceb2b9c0e5f404dd",
#   "nextblockhash": "0000076d574e5683ab73b37465950a445cb7b4f8ba0ab984e9ac555f808dcaec"
# }

header_hex = ("02000000" +
    "dd04f4e5c0b9b2ceaeef8c3cfca2fcf7f62a60f10f85e1eb4f3f84c7dd0a0000" +
    "c6a2944ede153447d40eac2caebfac41719b95e0ca13df794f7636bb7af79285" + 
    "dfb4725a" +
    "f0ff0f1e" +
    "bf1e0100")

best_hash = '9efd410fabf343c8b7e8a1a31cfd3ffa731f85308236f53d8fffdd825a020000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_race_hash(self):
        self.pow_hash = hexlify(race_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

