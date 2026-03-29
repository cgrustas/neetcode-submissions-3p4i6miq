class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an hashmap
        # key : number of occurrences in list
        # value : list of integers with said occurrences
        frequencies = defaultdict(list)

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # find the number of occurrences in list with count()
        # append the integer to the hashmap 
        for num, freq in count.items():
            frequencies[freq].append(num)

        # descend the hashmap 
        sorted_frequencies = dict(sorted(frequencies.items(), reverse=True))

        # add integers to the list
        KFrequencies = []
        for sublist in sorted_frequencies.values():
            # add the integer
            for integer in sublist:
                KFrequencies.append(integer)

                # if KFrequencies has reached size K, return the list
                if len(KFrequencies) == k:
                    return KFrequencies

        return kFrequencies