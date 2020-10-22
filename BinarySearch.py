class FindMissingElement:
    def __init__(self, array):
        array.sort()
        self.array = array
        self.right = len(self.array) - 1
        self.left = 0
        #self.difference = (self.array[-1] - self.array[0]) / len(self.array)
        self.missing_element = None

    def search_for_element(self):
        if len(self.array) == 0:
            print('Please enter a valid input')
            return
        else:
            difference = (self.array[-1] - self.array[0]) // len(self.array)

        while self.left <= self.right:
            mid_idx = self.right - (self.right - self.left) // 2

            if self.array[mid_idx] - self.array[mid_idx - 1] != difference and mid_idx - 1 >= 0:
                self.missing_element = self.array[mid_idx - 1] + difference
                return self.missing_element

            elif self.array[mid_idx + 1] - self.array[mid_idx] != difference and mid_idx + 1 < len(self.array):
                self.missing_element = self.array[mid_idx + 1] - difference
                return self.missing_element

            else:
                if mid_idx * difference != self.array[-1] - self.array[mid_idx]:
                    self.left = mid_idx + 1
                    return

                elif mid_idx * difference != self.array[mid_idx] - self.array[0]:
                    self.right = mid_idx - 1
                    return
