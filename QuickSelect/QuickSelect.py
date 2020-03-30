
class sort():

    #nums = [61, 93, 56, 90, 11]
    nums = [4, 1, 10, 8, 7, 12, 9, 2, 15]

    def changeArr(self, newArr):

        self.nums = newArr

    def swap(self, pos1, pos2):

        temp = self.nums[pos1]
        self.nums[pos1] = self.nums[pos2]
        self.nums[pos2] = temp

        return self.nums

    def QuickSelect(self, l, r, k):

        s = self.lomuto(0, 4)
        if(s == k-1):

            return self.nums[s]
        
        elif(s > l + r - 1):
            self.QuickSelect(l, s - 1, k)

        else:
            self.QuickSelect(s + 1, r, k - 1 - s)

    def lomuto(self, l, r):

        P = self.nums[l]
        s = l

        for i in range(l + 1, r):

            if(self.nums[i] < P):

                s = s + 1
                self.nums = self.swap(s, i)

        self.nums = self.swap(l, s)
        return s


#testing

test = sort()

print(test.QuickSelect(0, 10, 5))
