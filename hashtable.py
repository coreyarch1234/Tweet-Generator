#!python

from linkedlist import LinkedList
import random

class HashTable(object):

    def __init__(self, init_size=2000):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = [] # O(1)
        for bucket in self.buckets: #O(b) for b number of iterations
            for key, value in bucket.items(): #O(l), l iterations == n/b
                all_keys.append(key) #O(1)
        return all_keys # n keys

    def values(self):
        """Return a list of all values in this hash table"""
        # # TODO: Collect all values in each of the buckets
        # pass
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # # TODO: Count number of key-value entries in each of the buckets
        # return 0
        length = 0
        for bucket in self.buckets:
            for item in bucket.items():
                if item is not None:
                    length += 1
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # # TODO: Check if the given key exists in a bucket
        # pass
        # if key in self.keys(): #self.keys return a list of all keys
        #     return True
        # return False
        index = self.bucket_index(key) # constant
        bucket = self.buckets[index] #constant
        found = bucket.find(lambda (k, v): k == key) # average case O(L) - running time == n/b (average size of linked list)
        return found is not None  #constant

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # # TODO: Check if the given key exists and return its associated value
        # pass
        index = self.bucket_index(key)
        bucket = self.buckets[index]
        # for input_key, value in bucket.items():
        #     if input_key == key:
        #         return value
        found = bucket.find(lambda (k, v): k == key) # average case O(L) - running time == n/b (average size of linked list)
        if found is not None:
            _, value = found
            return value
        raise KeyError("Key does not exist")

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # # TODO: Insert or update the given key-value entry into a bucket
        # pass
        if self.contains(key):
            for input_key, output_value in self.buckets[self.bucket_index(key)].items():
                if input_key == key:
                    self.buckets[self.bucket_index(key)].delete((key, output_value))
                    self.buckets[self.bucket_index(key)].append((key, value))
        else:
            self.buckets[self.bucket_index(key)].append((key, value)) #appended key-value pair as node in linked list at that bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # # TODO: Find the given key and delete its entry if found
        # pass
        if self.contains(key):
            for input_key, value in self.buckets[self.bucket_index(key)].items():
                if input_key == key:
                    self.buckets[self.bucket_index(key)].delete((key, value))
        else:
            raise KeyError()
    def get_random_key(self):
        random_num = random.randint(0, int(self.length() - 1))
        return self.keys()[random_num]

def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    # print(ht.keys())
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))
    print(ht.get_random_key())

    # Enable this after implementing delete:
    # print('Deleting entries:')
    # ht.delete('I')
    # print(ht)
    # ht.delete('V')
    # print(ht)
    # ht.delete('X')
    # print(ht)
    # print('contains(X): ' + str(ht.contains('X')))
    # print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
