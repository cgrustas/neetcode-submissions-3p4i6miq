class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hashmap to record frequencies of integers
        # key : integer in list, value : number of appearances
        frequencies = {}
        for n in nums: 
            frequencies[n] = 1 + frequencies.get(n, 0) 
        
        # sort the dictionary by value, in descending order of frequencies
        sorted_dict = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))

        # store a list of integers from the dictionary in a separate variable
        integers = list(sorted_dict.keys())

        # then return a list of the first 'k' integers
        results = []
        for i in range(k):
            results.append(integers[i])
        return results

