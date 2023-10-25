"""
Hash Table Project
Shane Jose
"""

from typing import TypeVar, List, Tuple

T = TypeVar("T")
HashNode = TypeVar("HashNode")
HashTable = TypeVar("HashTable")


class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key: str, value: T, deleted: bool = False) -> None:
        self.key = key
        self.value = value
        self.deleted = deleted

    def __str__(self) -> str:
        return f"HashNode({self.key}, {self.value})"

    __repr__ = __str__

    def __eq__(self, other: HashNode) -> bool:
        return self.key == other.key and self.value == other.value

    def __iadd__(self, other: T) -> None:
        self.value += other


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
        109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
        367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
        499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
        643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
        797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
        947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,
        1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213,
        1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321,
        1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481,
        1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601,
        1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733,
        1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877,
        1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017,
        2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143,
        2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297,
        2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423,
        2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593,
        2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713,
        2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851,
        2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011,
        3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181,
        3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323,
        3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467,
        3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607,
        3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739,
        3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907,
        3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049,
        4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211,
        4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349,
        4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513,
        4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591, 4597, 4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657,
        4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733, 4751, 4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813,
        4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919, 4931, 4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973,
        4987, 4993, 4999, 5003, 5009, 5011, 5021, 5023, 5039, 5051, 5059, 5077, 5081, 5087, 5099, 5101, 5107, 5113,
        5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209, 5227, 5231, 5233, 5237, 5261, 5273, 5279, 5281, 5297,
        5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, 5393, 5399, 5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443,
        5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519, 5521, 5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591,
        5623, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669, 5683, 5689, 5693, 5701, 5711, 5717, 5737, 5741, 5743,
        5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827, 5839, 5843, 5849, 5851, 5857, 5861, 5867, 5869, 5879,
        5881, 5897, 5903, 5923, 5927, 5939, 5953, 5981, 5987, 6007, 6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073,
        6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143, 6151, 6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221,
        6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299, 6301, 6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359,
        6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449, 6451, 6469, 6473, 6481, 6491, 6521, 6529, 6547, 6551,
        6553, 6563, 6569, 6571, 6577, 6581, 6599, 6607, 6619, 6637, 6653, 6659, 6661, 6673, 6679, 6689, 6691, 6701,
        6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781, 6791, 6793, 6803, 6823, 6827, 6829, 6833, 6841, 6857,
        6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, 6947, 6949, 6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997,
        7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187,
        7193, 7207, 7211, 7213, 7219, 7229, 7237, 7243, 7247, 7253, 7283, 7297, 7307, 7309, 7321, 7331, 7333, 7349,
        7351, 7369, 7393, 7411, 7417, 7433, 7451, 7457, 7459, 7477, 7481, 7487, 7489, 7499, 7507, 7517, 7523, 7529,
        7537, 7541, 7547, 7549, 7559, 7561, 7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, 7649, 7669,
        7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, 7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829,
        7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919)

    def __init__(self, capacity: int = 8) -> None:
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other: HashTable) -> bool:
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __str__(self) -> str:
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    __repr__ = __str__

    def _hash_1(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, None if key is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param key: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    def __len__(self) -> int:
        """
        Getter for the size, which is the number of elements in the HashTable
        @return  size: int, the number of elements in the HashTable
        """
        return self.size


    def __setitem__(self, key: str, value: T) -> None:
        """
        Calls the insert function that sets the value with an associated key in the HashTable
        @param key: str, the key we are hashing
        @param value: str, the associated value we are storing
        @return None
        """
        self._insert(key, value)

    def __getitem__(self, key: str) -> T:
        """
        Calls the get function that looks up the value with an associated key in the HashTable
        @param key: str, the key we are searching
        @return value: T, the value associated to the provided key
        """

        sol = self._get(key)
        if sol is None:
            raise KeyError("Key Error")
        return sol.value

    def __delitem__(self, key: str) -> None:
        """
        Deletes the value with an associated key in the HashTable
        If the key does not exist, raise a KeyError
        @param key: str, the key we are deleting the associated value of
        @return None
        """

        sol = self._get(key)
        if sol is None:
            raise KeyError("Key Error")
        self._delete(key)

    def __contains__(self, key: str) -> bool:
        """
        Determine if a node with the key denoted by the parameter exist in the HashTable
        @param key: str, the key we are checking to be a part of the HashTable
        @return bool: Boolean, True if key is in the HashTable, False otherwise
        """

        sol = self._get(key)
        if sol is None:
            return False
        return True

    def _hash(self, key: str, inserting: bool = False) -> int:
        """
        Given a key string, return an index in the HashTable
        When inserting, insert the node into the next available bin
        When searching or deleting, continue searching until a proper node is found
        if key does not exist in the HashTable, return the index of the next available position

        @param key: str, key being used in our hash function
        @param inserting: bool, If true we are doing insertion, False otherwise
        @returns index: int, the bin that got hashed into
        """

        hash1 = self._hash_1(key)
        hash2 = self._hash_2(key)

        index = hash1
        empty_ind = None

        while True:
            value = self.table[index]
            if value is None:  # if the bin is empty, return index
                if empty_ind is None:
                    empty_ind = index
                if inserting:
                    return empty_ind
                else:
                    return index
            elif value.key == key and not value.deleted:  # if key is same as parameter and not deleted, return index
                return index
            elif empty_ind is None and value.deleted:
                if inserting:
                    return index
                empty_ind = index
            index = (index + hash2) % self.capacity  # probes the next index to check for collision
            if index == hash1:
                break
        if inserting:
            return empty_ind
        else:
            return index


    def _insert(self, key: str, value: T) -> None:
        """
        Use the key and value parameters to add a HashNode to the hash table,
        if key exists, overwrite the existing value
        if the table has a load factor >= 0.5, grow the table to double the existing capacity
        Doubling the capacity, is done in the _grow method

        @param key: str, the key associated with the value we are storing
        @param value: T, the associated value we are storing
        @returns None
        """

        load_factor = (self.size + 1) / self.capacity
        if load_factor >= 0.5:  # if load_factor >=0.5, double the capacity of the HashTable
            self._grow()

        index = self._hash(key, True)  # Get the index for the key,value to be hashed to the HashTable
        if self.table[index] is None or self.table[index] == HashNode(None, None):
            self.table[index] = HashNode(key, value)
            self.size += 1
        else:
            self.table[index].value = value


    def _get(self, key: str) -> HashNode:
        """
        Find the HashNode with the given key in the HashTable
        If the element does not exist, return None
        @param key: str, the key we are looking up
        @returns HashNode, Hashnode with the key we looked up
        """

        bucket = self._hash(key)

        if self.table[bucket] is None:
            return None
        if self.table[bucket] is HashNode(None, None):
            return None

        return self.table[bucket]

    def _delete(self, key: str) -> None:
        """
        Removes the HashNode with the given key from the HashTable
        If node found, reassign its key and value to None
        Update the size, decrement by 1
        @param key: str, the key of the Node we are looking to delete
        @returns None
        """

        bucket = self._hash(key)  # Get the index of the key to delete the key and value
        if self.table[bucket] is not None:
            self.table[bucket] = HashNode(None, None)
            self.size -= 1

    def _grow(self) -> None:
        """
        Double the capacity of the existing HashTable
        Update self.prime_index to be the index of the largest prime smaller than self.capacity
        Call _insert function to re-insert the nodes from the old HashTable
        @return None
        """
        old_table = self.table
        self.capacity *= 2

        # Update prime_index to be the largest prime smaller than self.capacity
        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

        self.table = [None] * self.capacity
        self.size = 0

        # Re-insert all the nodes from the old HashTable
        for node in old_table:
            if node and not node.deleted:
                self._insert(node.key, node.value)

        

    def update(self, pairs: List[Tuple[str, T]] = []) -> None:
        """
        Update the hash table using an iterable of key value pairs
        if the value already exists, update it, otherwise enter it into the table
        Calls _insert function to insert the updated value or key and value
        @param pairs: list of tuples, (key, value) that is being updated
        @return None
        """

        for pair in pairs:
            key = pair[0]
            value = pair[1]
            self._insert(key, value)

    def keys(self) -> List[str]:
        """
        Makes a list that contains all of the keys in the HashTable
        Exclude nonexistent and deleted HashNodes
        @returns keys_list: list, list of all the keys in the HashTable
        """

        keys_list = []
        for val in self.table:
            if val is not None:
                if val.key is not None:
                    keys_list.append(val.key)

        return keys_list

    def values(self) -> List[T]:
        """
        Makes a list that contains all of the values in the table
        Exclude nonexistent and deleted HashNodes
        @returns values_list: list, list of all the values in the HashTable
        """
        values_list = []
        for val in self.table:
            if val is not None:
                if val.key is not None:
                    values_list.append(val.value)
        return values_list

    def items(self) -> List[Tuple[str, T]]:
        """
        Makes a list that contains all of the key value pairs in the table
        Exclude nonexistent and deleted HashNodes
        @returns key_val_list: List of Tuples, list of tuples of the form (key,value)
        """

        key_val_list = []
        for val in self.table:
            if val is not None:
                if val.key is not None:
                    key_val_list.append((val.key, val.value))
        return key_val_list

    def clear(self) -> None:
        """
        Clears the table of HashNodes completely
        Does not modify the capacity
        @returns None
        """
        for i in range(self.capacity):
            if self.table[i] is not None:
                self.table[i] = None
                self.size -= 1


def display_duplicates(data: List[List[str]], filenames: List[str]) -> HashTable:
    """
    Display duplicate images represented by a HashTable
    The keys of the HashTable should be the filenames of the images
    The values lists should be empty if the image has no duplicates
    Otherwise the value lists should contain the filename of the duplicated images to the first occurrence
    of that image

    @param data: List of lists, list of lists of four hash strings corresponding to the hash results for each image rotated 0,90,180, and 270 degrees
    @param filenames: List, list of strings that corresponds the filenames of the images whose hash info lies in data
    @returns dup_filename: HashTable, that represents images that has duplicate images and ones that hasn't have duplicate images
    """

    data_filename = HashTable()  # HashTable that has data has keys, and values as filenames
    dup_filename = HashTable()  # HashTable that has keys as filenames, and values as filenames that has duplicate data values
    for i in range(len(data)):  # iterate through data list
        for j in range(len(data[i])):  # iterate through each element in data list
            if data[i][j] not in data_filename:  # if data is being visited for the first time
                data_filename[data[i][j]] = filenames[i]  # Update Hashtable, data as key, value as the filename
                dup_filename[data_filename[data[i][j]]] = []  # Update HashTablem, filename as key, value as an empty list since there is no duplicate images
            else:
                dup_filename[data_filename[data[i][j]]].append(filenames[i])  # Update the value of key by adding an additional duplicate image of the key
                break  # break the loop if a duplicate data is found

    return dup_filename


def generate_fan_chant(fan_chant: str, chant_words: List[str]) -> List[int]:
    """
    Finds all the index positions where permutations of chant_words are in the fan chant
    @param fan_chant: str, string that represents BTS fan chant
    @param chant_words: list, list of strings that represents the words to be found in fan chant
    @returns index_words, list of ints that contains the starting index of any permutation of the words within the fan_chant
    """

    # if chant_words is empty return empty list
    if len(chant_words) == 0:
        return []

    word_counts = HashTable()
    for word in chant_words:  # iterating through each word in the chant_words list
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1  # keep track of each word that appears in the chant_words list

    word_len = len(chant_words[0])
    index_words = []  # store the starting index of each occurrence of the fan chant in fan_chant
    # iterates over all possible starting indices for a substring of length word_len * len(chant_words) within fan_chant
    for i in range(len(fan_chant) - word_len * len(chant_words) + 1):
        substring_counts = HashTable()
        j = 0
        while j < len(chant_words):  # iterate over each word in the chant_words list
            start = i + j * word_len
            end = i + (j + 1) * word_len
            substring = fan_chant[start:end]
            if substring not in word_counts:  # if substring is not in word_counts, break the loop
                break
            if substring not in substring_counts:
                substring_counts[substring] = 0
            substring_counts[substring] += 1
            # If count of any substring in substring_counts > count of substring in word_counts, then break
            if substring_counts[substring] > word_counts[substring]:
                break
            j += 1
        if j == len(chant_words):  # if all words in chant_words have been found from fan_chant
            index_words.append(i)  # append the starting index of the substring
    return index_words


