"""
The goal of this coding activity is to design a system that limits the number of active roles that any given person has. A role gives the user access to some thing, whether it be a piece of data or an internal system. The system achieves this requirement by keeping track of the last k roles that a person has used. If a new role is used, the oldest role is removed if there are already k active roles for that person. Each role has a name and a message which contains details about its use by the person. You only need to store the last message for a role invocation.

Implement the constructor, get, and set methods of RolesCache. Each instance of the RolesCache corresponds to a single person.

Finally, fill out the runtime complexity for get and set and the overall space used. Use Big O notation, i.e. O(1), O(N), etc. For a refresher on Big O notation, please review https://danielmiessler.com/study/big-o-notation/.

"""

class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, role):
        if role in self.cache:
            return self.cache[role][-1]  # Return the last message for the role
        else:
            return None

    def set(self, role, message):
        if role in self.cache:
            self.cache[role][-1] = message  # Update the message for the existing role
        else:
            if len(self.cache) >= self.capacity:
                # Remove the oldest role
                oldest_role = next(iter(self.cache))
                del self.cache[oldest_role]
            self.cache[role] = [message]  # Add the new role and message to the cache

    def _complexity(self):
        return {
            'get': 'O(1)',  # Constant time complexity for dictionary lookup
            'set': 'O(1)',  # Constant time complexity for dictionary insertion/deletion
            'space': 'O(k)'  # Space complexity is proportional to the capacity (k) of the cache
        }
