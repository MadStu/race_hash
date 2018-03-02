from distutils.core import setup, Extension

race_hash_module = Extension('race_hash',
                                 sources = ['racemodule.c',
                                            'race.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sponge.c',
                                            'sha3/cubehash.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'race_hash',
       version = '1.0.0',
       description = 'Binding for Race proof-of-work hashing.',
       ext_modules = [race_hash_module])
