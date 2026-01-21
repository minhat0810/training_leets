class Solution(object):
    def groupAnagrams(self, strs):  
        groups = {} # tạo hashmap
        for i in strs:
            key = ''.join(sorted(i))
            if key not in groups:
                groups[key] = []  # tạo mảng rỗng
            groups[key].append(i)
        return list(groups.values())

#hướng giải quyết:
# 1. tạo hashmap
# 2. sắp sắp lại i như là key -> vd sorted(i = eat) -> ['a','e','t'] -> ''.join -> [aet]
# 3. kiểm tra nếu chưa key chứa có trong group thì tạo mảng rỗng
# 4. thêm i và mảng theo key
# 5. return về list value có trong group