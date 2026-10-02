class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        seen = set()
        for item in strs:
            new_item = "".join(sorted(item))
            if new_item not in seen:
                dict1[new_item] = [item]
                seen.add(new_item)
            else:
                dict1[new_item].append(item)
        return list(dict1.values())

        