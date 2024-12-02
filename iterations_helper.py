class IterationsHelper:
    @staticmethod
    def for_loop(start, end):
        result = []
        for i in range(start, end + 1):
            result.append(i)
        return result

    @staticmethod
    def while_loop(start, end):
        result = []
        i = start
        while i <= end:
            result.append(i)
            i += 1
        return result

    @staticmethod
    def do_while_loop(start, end):
        result = []
        i = start
        while True:
            result.append(i)
            i += 1
            if i > end:
                break
        return result

    @staticmethod
    def for_each_loop(iterable):
        result = []
        for item in iterable:
            result.append(item)
        return result

    @staticmethod
    def fibonacci(n):
        result = []
        a, b = 0, 1
        while len(result) < n:
            result.append(a)
            a, b = b, a + b
        return result