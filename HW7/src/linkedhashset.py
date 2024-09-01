import chainednode
import set
import collections.abc

"""
CSCI-603 Lab 7: LinkedHashTable

This program is used to create a homemade hash table that remembers insertion order

author: Kapil Sharma ks4643
"""
class LinkedHashSet(set.SetType, collections.abc.Iterable):
    __slots__ = (
    "initial_num_buckets", "load_limit", "hash_function", "hash_table", "head", "front", "back", "MINIMUM_BUCKETS",
    "bucket_size")
    initial_num_buckets: int
    load_limit: float
    hash_function: any
    hash_table: list
    front: chainednode.ChainedNode
    back: chainednode.ChainedNode
    MINIMUM_BUCKETS: int
    bucket_size: int

    def __init__(self, initial_num_buckets: int = 10, load_limit: float = 0.75, hash_function=hash, MINIMUM_BUCKETS=10,
                 bucket_size=0):
        super().__init__()
        self.initial_num_buckets = initial_num_buckets
        self.load_limit = load_limit
        self.hash_function = hash_function
        self.hash_table = [None] * initial_num_buckets
        self.front = None
        self.back = None
        self.MINIMUM_BUCKETS = MINIMUM_BUCKETS
        self.bucket_size = initial_num_buckets

    def remove(self, obj):
        """
        Remove an object from the hash table (and from the insertion order).
        Resize the table if its load_factor has dropped below (1-load_limit).
        :param obj: the value to remove; assumes hashing and equality work
        :return: True iff the obj has been remove from this set
        """
        if not self.contains(obj):
            return False

        load = (self.size - 1) / len(self.hash_table)
        if load < (1 - self.load_limit):
            rehashed_table = self.rehashing_logic_contract(-1)
            if rehashed_table is not None:
                self.hash_table = rehashed_table

        key = self.hash_function(obj) % len(self.hash_table)
        node = self.hash_table[key]
        temp_head = self.hash_table[key]

        if temp_head is not None:
            if temp_head.obj == self.front.obj:
                self.front = temp_head.next
            else:
                while temp_head.next is not None:
                    if temp_head.obj == obj:
                        if temp_head.prev is not None:
                            temp_head.prev.next = temp_head.next
                            if temp_head.next is not None:
                                temp_head.next.prev = temp_head.prev
                                self.size = self.size - 1
                                break
                            else:
                                temp_head.prev.next = None
                                self.size = self.size - 1
                                break
                        else:
                            temp_head.next.prev = None
                            self.front = temp_head.next
                            self.size = self.size - 1
                            break
                    temp_head = temp_head.next

            if temp_head.next is None:
                temp_head.prev.next = None
                self.back = temp_head.prev

            # prev = node
            if node.obj == obj:
                self.hash_table[key] = node.fwd
                self.size = self.size - 1
                return True

            while node.fwd is not None:  # check in chain
                cursor = node
                node = node.fwd
                if node.obj == obj:
                    cursor.fwd = node.fwd
                    self.size = self.size - 1
            return True
        return False

    def contains(self, obj):
        """
        :return: True iff obj or its equivalent has been added to this set
        """
        key = self.hash_function(obj) % self.bucket_size
        node = self.hash_table[key]
        while node is not None:
            if node.obj == obj:
                return True
            node = node.next
        return False

    def copy_table_to_new_table(self, bucket_size):
        """
        This function copies the data from the old table to new one with the changed size
        :param bucket_size:  size of the table
        :return: the new table
        """
        table = LinkedHashSet(bucket_size)
        head = self.front
        while head is not None:
            table.add(head.obj)
            head = head.next
        return table.hash_table

    def rehashing_logic_expand(self, value):
        """
        This has the logic for when the table expands
        :param value:
        :return: the expanded table object
        """
        load = (self.size + value) / len(self.hash_table)
        table = None
        if load > self.load_limit:
            table = self.copy_table_to_new_table(self.initial_num_buckets * 2)
        return table

    def rehashing_logic_contract(self, value):
        """
            This has the logic for when the table contracts
            :param value:
            :return: the expanded table object
        """
        load = (self.size + value) / len(self.hash_table)
        table = None
        if load < (1 - self.load_limit):
            self.bucket_size = len(self.hash_table) // 2
            if self.bucket_size < self.MINIMUM_BUCKETS:
                self.bucket_size = self.MINIMUM_BUCKETS
            if self.bucket_size > self.MINIMUM_BUCKETS:
                table = self.copy_table_to_new_table(self.bucket_size)
        return table

    def add(self, obj, value=1):
        """
            Insert a new object into the hash table and remember when it was added
            relative to other calls to this method. However, if the object is
            added multiple times, the hash table is left unchanged, including the
            fact that this object's location in the insertion order does not change.
            Double the size of the table if its load_factor exceeds the load_limit.
            :param obj: the object to add
            :return: True iff obj has been added to this set
        """
        node = chainednode.ChainedNode(obj)
        if self.contains(obj):
            return False

        load = (self.size + 1) / len(self.hash_table)
        if load > self.load_limit:
            rehashed_table = self.rehashing_logic_expand(1)
            if rehashed_table is not None:
                self.hash_table = rehashed_table

        key = self.hash_function(obj) % self.bucket_size

        if self.hash_table[key] is None:  # no element in the chain
            self.hash_table[key] = node
            if self.front is None:  # first element  in the set
                self.front = node
                self.back = node
            else:
                node.prev = self.back
                self.back.next = node
                self.back = node
            self.size = self.size + 1
            return True
        else:
            linear_head = self.hash_table[key]  # add for chaining
            while linear_head.fwd is not None:
                linear_head = linear_head.fwd
            linear_head.fwd = node
            node.prev = self.back
            self.back.next = node
            self.back = node
            self.size = self.size + 1

    def __str__(self):
        result = ""
        index = 0
        print("String generate----------------")
        print("Capacity:", self.bucket_size, "Size: ",self.size, "Load Factor: ", self.size/len(self.hash_table), "Load Limit: 0.75")
        print("Hash Table")
        print("------------------")
        for i in self.hash_table:
            result += str(index) + ": " + str(i) + "\n"
            index += 1
        return result

    def __iter__(self):
        head = self.front
        while head is not None:
            yield head.get_value()
            head = head.next


    def __repr__(self):
        """
        Representation of node object
        :return: string with the head
        """
        result = ""
        head = self.front
        while head is not None:
            result += str(head.obj) + "->"
            head = head.next
        return result

    def __len__(self):
        return self.size