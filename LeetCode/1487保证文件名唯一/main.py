def check(name, res, name_dict):
    if name not in res:
        res.append(name)
        name_dict[name] = 1
    else:
        k = 1
        new_name = name + "(" + str(k) + ")"
        while new_name in name_dict:
            k += 1
            new_name = name + "(" + str(k) + ")"
        name_dict[new_name] = 1
        res.append(new_name)


class Solution:
    def getFolderNames(self, names):
        res = []
        name_dict = {}
        for name in names:
            check(name, res, name_dict)

        return res


a = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece"]
b = ["onepiece", "onepiece(1)", "onepiece(2)", "onepiece(3)", "onepiece(4)"]
obj = Solution()
result = obj.getFolderNames(a)
assert result == b
pass
