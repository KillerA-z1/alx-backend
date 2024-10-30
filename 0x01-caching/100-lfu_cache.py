#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines an LFU caching system with LRU tie-breaker
    """

    def __init__(self):
        """ Initialize the class
        """
        super().__init__()
        self.frequency = {}      # Key usage frequencies
        self.usage_order = {}    # Key usage timestamps
        self.timestamp = 0       # Incremental timestamp for LRU

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        self.timestamp += 1

        if key in self.cache_data:
            # Update existing key
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order[key] = self.timestamp
        else:
            # Add new key
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Need to discard an item
                min_freq = min(self.frequency.values())
                # Get keys with the lowest frequency
                keys_with_min_freq = [k for k in self.frequency
                                      if self.frequency[k] == min_freq]
                if len(keys_with_min_freq) == 1:
                    key_to_discard = keys_with_min_freq[0]
                else:
                    # Use LRU among keys with the same min frequency
                    oldest_usage = min(self.usage_order[k]
                                       for k in keys_with_min_freq)
                    lru_keys = [k for k in keys_with_min_freq
                                if self.usage_order[k] == oldest_usage]
                    key_to_discard = lru_keys[0]
                # Discard the key
                del self.cache_data[key_to_discard]
                del self.frequency[key_to_discard]
                del self.usage_order[key_to_discard]
                print("DISCARD:", key_to_discard)
            # Add the new key
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = self.timestamp

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.timestamp += 1
        # Update frequency and usage timestamp
        self.frequency[key] += 1
        self.usage_order[key] = self.timestamp
        return self.cache_data[key]
