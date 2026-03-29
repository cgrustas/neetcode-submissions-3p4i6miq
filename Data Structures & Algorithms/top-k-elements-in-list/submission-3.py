class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an hashmap
        # key : integer in list
        # value : number of occurrences
        count = {}

        # a list of len(nums) + 1 empty sublists
        frequencies = [[] for i in range(len(nums) + 1)]

        # find the number of occurrences for each integer in list
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # append the integer to the sublist
        # use the number of occurrences to determine the index of the sublist
        for num, freq in count.items():
            frequencies[freq].append(num)

        
        # add integers to the list
        result = []
        for i in range(len(nums), 0, -1):
            for integer in frequencies[i]:
                # add the integer
                result.append(integer)

                # if result has reached size K, return the list
                if len(result) == k:
                    return result

