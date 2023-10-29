
# Exercitiul 1 - Write a Python class that simulates a Stack. The class should implement methods like push, pop,
# peek (the last two methods should return None if no element is present in the stack).

class Stack:
        def __init__(self):
            self.stack = []

        def push(self, element):
            self.stack.append(element)

        def pop(self):
            if len(self.stack) == 0:
                return None
            return self.stack.pop()

        def peek(self):
            if len(self.stack) == 0:
                return None
            return self.stack[-1]

        def __str__(self):
            return str(self.stack)


# Exercitiul 2 - Write a Python class that simulates a Queue. The class should implement methods like push, pop,
# peek (the last two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def __str__(self):
        return str(self.queue)


# Exercitiul 3 - Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization.
# The class should provide methods to access elements (get and set methods) and some methematical functions such as transpose, matrix multiplication
# and a method that allows iterating through all elements form a matrix an apply a transformation over them (via a lambda function).

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0] * m for _ in range(n)]

    def set(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.data[i][j] = value
        else:
            raise IndexError("Index out of range")

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.data[i][j]
        else:
            raise IndexError("Index out of range")

    def transpose(self):
        transposed_matrix = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed_matrix.set(j, i, self.get(i, j))
        return transposed_matrix

    def __mul__(self, other_matrix):
        if self.m != other_matrix.n:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")

        result_matrix = Matrix(self.n, other_matrix.m)
        for i in range(self.n):
            for j in range(other_matrix.m):
                dot_product = sum(self.get(i, k) * other_matrix.get(k, j) for k in range(self.m))
                result_matrix.set(i, j, dot_product)
        return result_matrix

    def apply_transformation(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, func(self.get(i, j)))

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])



if __name__ == '__main__':

    # Test Exercitiul 1
    print("Test Exercitiul 1")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)
    print("pop: ", stack.pop())
    print("peek: ", stack.peek())
    print(stack)

    # Test Exercitiul 2
    print("Test Exercitiul 2")
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue)
    print("pop: ", queue.pop())
    print("peek: ", queue.peek())
    print(queue)

    # Test Exercitiul 3
    print("Test Exercitiul 3")
    matrix0 = Matrix(3, 3)
    matrix0.set(0, 0, 1)
    matrix0.set(0, 1, 2)
    matrix0.set(0, 2, 3)
    matrix0.set(1, 0, 4)
    matrix0.set(1, 1, 5)
    matrix0.set(1, 2, 6)
    matrix0.set(2, 0, 7)
    matrix0.set(2, 1, 8)
    matrix0.set(2, 2, 9)
    print(matrix0)
    print("get(1,1): ", matrix0.get(1, 1))

    matrix_transpose = matrix0.transpose()
    print("transpose:")
    print(matrix_transpose)

    matrix1 = matrix0 * matrix_transpose
    print("matrix multiplication:")
    print(matrix1)

    matrix1.apply_transformation(lambda x: x + 5)
    print("apply_transformation( on matrix1 ):")
    print(matrix1)











