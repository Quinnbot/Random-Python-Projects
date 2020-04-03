
class sort():

    # nums = [61, 93, 56, 90, 11]
    nums = [4, 1, 10, 8, 7, 12, 9, 2, 15]

    def changeArr(self, newArr):

        self.nums = newArr

    def swap(self, pos1, pos2):

        temp = self.nums[pos1]
        self.nums[pos1] = self.nums[pos2]
        self.nums[pos2] = temp

    def QuickSelect(self, l, r, k):

        s = self.lomuto(l, r)

        # print(self.nums)
        # print(l)
        # print(r)
        # print(k)
        # print(s)

        if(s == k):
            print(self.nums[s])
            return self.nums#for some reason this just returns none. so im printing it out above.
        
        elif(s > l + k):

            self.QuickSelect(l, s, k)

        else:

            self.QuickSelect(s, r, k - s)

    def lomuto(self, l, r):

        P = self.nums[l]
        s = l

        for i in range(l + 1, r):

            if(self.nums[i] < P):

                s = s + 1
                self.swap(s, i)

        self.swap(l, s)
        return s


#testing

test = sort()

print(test.QuickSelect(0, 8, 4))
