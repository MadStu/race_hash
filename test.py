import race_hash
from binascii import unhexlify, hexlify

import unittest

header_hex = ("00000020" +
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

