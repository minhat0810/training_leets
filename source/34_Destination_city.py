# chia from, to duyệt to
class Solution(object):
    def destCity(self, paths):
        # from_maps = set()

        # for frm, to in paths:
        #     from_maps.add(frm)
        
        # for frm, to in paths:
        #     if to not in from_maps:
        #         return to
        from_maps = {frm for frm, _ in paths }
        for _, to in paths:
            if to not in from_maps:
                return to

sol = Solution()
print(sol.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))