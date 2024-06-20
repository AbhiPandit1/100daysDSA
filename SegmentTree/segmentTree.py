class MixedSegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    
    #Recrursively updating Tree
    def recursiveBuild(self, data, node, left, right):
        if left == right:
            self.tree[node] = data[left]
        else:
            mid = (left + right) // 2
            self.recursiveBuild(data, 2 * node + 1, left, mid)
            self.recursiveBuild(data, 2 * node + 2, mid + 1, right)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update_recursive(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update_recursive(idx, value, 2 * node + 1, start, mid)
            else:
                self.update_recursive(idx, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update_iterative(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query_recursive(self, L, R, node, start, end):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query_recursive(L, R, 2 * node + 1, start, mid)
        right_sum = self.query_recursive(L, R, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum

    def query_iterative(self, l, r):
        l += self.n
        r += self.n
        sum = 0
        while l < r:
            if l % 2:
                sum += self.tree[l]
                l += 1
            if r % 2:
                r -= 1
                sum += self.tree[r]
            l //= 2
            r //= 2
        return sum

    def update_value_recursive(self, idx, value):
        self.update_recursive(idx, value, 0, 0, self.n - 1)

    def update_value_iterative(self, idx, value):
        self.update_iterative(idx, value)

    def range_query_recursive(self, L, R):
        return self.query_recursive(L, R, 0, 0, self.n - 1)

    def range_query_iterative(self, L, R):
        return self.query_iterative(L, R)


data = [1, 2, 3, 4, 5, 6, 7, 8]
seg_tree = MixedSegmentTree(data)
print(seg_tree.range_query_recursive(2, 5))
seg_tree.update_value_recursive(3, 10)
print(seg_tree.range_query_recursive(2, 5))
print(seg_tree.range_query_iterative(2, 5))
seg_tree.update_value_iterative(3, 15)
print(seg_tree.range_query_iterative(2, 5))
