class SuperStr(str):
    def is_repeatance(self, s):
        if not s or not self:
            return False
        return self == s * (len(self) // len(s)) and len(self) % len(s) == 0

    def is_palindrom(self):
        normalized = self.lower()
        return normalized == normalized[::-1]
 
s = SuperStr("abcabcabc")
print(s.is_repeatance("abc"))
print(s.is_repeatance("ab"))
print(s.is_repeatance(""))

p = SuperStr("Madam")
print(p.is_palindrom())

q = SuperStr("")
print(q.is_palindrom())    