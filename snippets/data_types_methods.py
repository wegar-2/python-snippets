from string import ascii_uppercase


# =====================================================================================================================
# ==================================================== DICTIONARY =====================================================
# =====================================================================================================================
# (1) .update()
dict1 = {"a": 1, "b": 3}
dict1.update({"c": 1234})
print(dict1)
# (2) .pop()
print(dict1.pop("a"))
print(dict1)
# (3) .get(, default)
print(dict1.get("z", "NA!"))
print(dict1) # note: "z" key value is still not assigned for the dictionary dict1
# (4) .setdefault
print(dict1.setdefault("z", "NA!"))
print(dict1)
# (5) dict.fromkeys()
print(dict.fromkeys(ascii_uppercase[:10], list(range(10))))
# =====================================================================================================================
