class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for n in nums:
            hash[n]=hash.get(n,0)+1
        hash_sort=sorted(hash.items(),key=lambda item:item[1],reverse=True)
        hash=dict(hash_sort)
        return list(islice(hash,k))
