# this is implemented from the chaining technique.
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Initialize buckets

    def _hash_function(self, key):
        # Simple hash: sum of character codes % table size
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        bucket = self.table[index]

        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update value
                print(f"Updated key '{key}' at index {index}")
                return

        # If key not found, append new key-value pair
        bucket.append((key, value))
        print(f"Inserted key '{key}' at index {index}")

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                print(f"Deleted key '{key}' from index {index}")
                return
        print(f"Key '{key}' not found!")

    def display(self):
        print("\nHash Table Contents:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")



if __name__ == "__main__":
    h = HashTable(10)  # Create hash table of size 10

    h.insert("apple", 100)
    h.insert("banana", 200)
    h.insert("grapes", 300)

    print("\nValue for 'apple':", h.get("apple"))

    h.display()

    h.insert("apple", 150)  # Update

    h.delete("banana")
    h.delete("orange")  # Key not present

    h.display()
 

# ચલો, આપણે હાશ ફંક્શન (_hash_function) ને ગુજરાતી ભાષામાં વિગતવાર સમજીયે, સાથે સાથે ઉદાહરણ સાથે values પણ લઈએ.

# ---

# ## 🔍 હેશ ફંક્શન શું છે?

# હેશ ફંક્શન એ કોઈ પણ “key” (જે સામાન્ય રીતે string હોય છે જેમ કે "apple") ને એક નંબર (index) માં બદલે છે. આ નંબર “હેશ ટેબલ” (Hash Table) ની લંબાઈની અંદર હોય છે. આ index બતાવે છે કે આપણે value ને Hash Table ના કયા સ્થાન (slot) માં રાખવી.

# ---

# ### 📌 આ ફંક્શન છે:

# ```python
# def _hash_function(self, key):
#     return sum(ord(char) for char in str(key)) % self.size
# ```

# ચાલો તેને ભાગે ભાગે સમજીએ:

# ---

# ### 🧮 Step-by-Step સમજૂતી:

# 1. **`ord(char)`**:
#    - દરેક character નો ASCII number આપે છે.
#    - ઉદાહરણ:
#      - `'a'` = 97
#      - `'p'` = 112
#      - `'l'` = 108
#      - `'e'` = 101

# 2. **`sum(ord(char) for char in str(key))`**:
#    - દરેક character ના ASCII values નો જમાવ (sum) કરે છે.

# 3. **`% self.size`**:
#    - હેશ ટેબલની સાઇઝના આધારે તેને Modulo કરવું (બાકીभाग લાવવો) જેથી તે કોઈ પણ માન્ય index (0 થી size-1 વચ્ચે) આપે.

# ---

# ## 🧪 ઉદાહરણ સાથે સમજાવું:

# ચાલો key તરીકે `"apple"` લઈએ અને Hash Table નું size = 10 લઈએ:

# ```python
# key = "apple"
# size = 10
# ```

# 1. `"apple"` ના characters: `'a', 'p', 'p', 'l', 'e'`
# 2. ASCII values:
#    - `a` = 97
#    - `p` = 112
#    - `p` = 112
#    - `l` = 108
#    - `e` = 101

# 3. Sum = 97 + 112 + 112 + 108 + 101 = **530**

# 4. Hash Index = 530 % 10 = **0**

# 📍 એટલે કે `"apple"` નું value Hash Table ના **index 0** પર stored થશે.

# ---

# ### બીજું ઉદાહરણ: `"banana"`

# Characters = `b, a, n, a, n, a`  
# ASCII = 98 + 97 + 110 + 97 + 110 + 97 = **609**  
# Hash Index = 609 % 10 = **9**

# 📍 `"banana"` નું value **index 9** પર જશે.

# ---

# ## ✅ ફાઇનલ રીતે કહીએ તો...

# ```python
# return sum(ord(char) for char in str(key)) % self.size
# ```

# એવું કહે છે કે:
# - દરેક letter ના number મેળવ
# - બધાનું total લ
# - Hash Table ના કદથી modulo લઈ, તે index આપી દે

# ---

# તમે મને કહો કે હવે:
# - તમને linear probing/open addressing શીખવું છે?
# - કે તમે આજ hash function ને અલગ રીતે લખવાનું શીખવા માંગો છો?
# - કે તમે તમારા project માં Hash Table વાપરવું શીખવા માંગો છો?

# તમારું goal જણાવો, મેં આગળનું આગળ લઈ જઈશ 🙂