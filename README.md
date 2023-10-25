# HashTable-
The "Hash Table Project" is a Python implementation of a hash table data structure. It provides the user with a HashTable class that allows for key-value pair storage and retrieval using hashing techniques. Here's an overview of the project:

1. Hash Table Implementation: The project defines a `HashTable` class that is designed to store key-value pairs. It uses open addressing for collision resolution.

2. Hashing Functions: The project includes two hashing functions, `_hash_1` and `_hash_2`, which are used for generating hash values from keys. The `_hash_2` function incorporates prime numbers for further scattering of hash values.

3. Key-Value Storage: The `HashTable` allows users to store and retrieve key-value pairs using methods like `__setitem__` (for insertion), `__getitem__` (for retrieval), and `__delitem__` (for deletion). It also includes a `__contains__` method to check if a key exists in the hash table.

4. Load Factor and Capacity Management: The project dynamically resizes the hash table by doubling its capacity when the load factor exceeds 0.5. This is handled in the `_insert` method.

5. Additional Functionality: It provides methods for iterating through keys, values, and key-value pairs, as well as clearing the entire hash table.

6. Duplicates Detection: The `display_duplicates` function is designed to find duplicate images based on their hash values. It uses two hash tables, one to track data hash values and their corresponding filenames and the other to store filenames with duplicates.

7. Fan Chant Analysis: The `generate_fan_chant` function analyzes a given fan chant to find all the index positions where permutations of specified words are present.

The project demonstrates the power and versatility of hash tables in various scenarios, from key-value storage to duplicate detection and text analysis. Hash tables are widely used in computer science and offer efficient access and retrieval of data. Also the project provides a practical example of how hash tables can be implemented and utilized in Python.
