from krone import Krone
from bst import BST


class Test:
    """delete before submission"""
    _count = 0

    def test(self, a, b):
        if a == b:
            self.print("Passed")
        else:
            self.print(f"Failed. \nResult: {a}\nExpected: {b}")
            if a:
                for i in range(len(a)):
                    if a[i] != b[i]:
                        print(f"Problem: {a[i]} != {b[i]} ")

    def print(self, msg):
        self._count += 1
        print(f"Test {self._count}: {msg}.")


def main():
    pass


def test():
    value_array = [57.12, 23.44, 87.43, 68.99, 111.22, 44.55, 77.77, 18.36, 543.21, 20.21, 345.67, 36.18, 48.48, 101.00,
                   11.00, 21.00, 51.00, 1.00, 251.00, 151.00]
    krone_array = list(Krone(a) for a in value_array)
    tree = BST()
    for a in krone_array:
        tree.insert(a)

    tester = Test()
    bft_result = [57.12, 23.44, 87.43, 18.36, 44.55, 68.99, 111.22, 11.00, 20.21, 36.18, 48.48, 77.77, 101.00, 543.21,
                  1.00, 21.00, 51.00, 345.67, 251.00, 151.00]
    tester.test(tree.breadth_first_traversal(tree.get_head()), bft_result)
    in_result = sorted(value_array)
    tester.test(tree.inorder_traversal(tree.get_head()), in_result)
    pre_result = [57.12, 23.44, 18.36, 11.00, 1.00, 20.21, 21.00, 44.55, 36.18, 48.48, 51.00, 87.43, 68.99, 77.77,
                  111.22, 101.00, 543.21, 345.67, 251.00, 151.00]
    tester.test(tree.preorder_traversal(tree.get_head()), pre_result)
    post_result = [1.00, 11.00, 21.00, 20.21, 18.36, 36.18, 51.00, 48.48, 44.55, 23.44, 77.77, 68.99, 101.00, 151.00,
                   251.00, 345.67, 543.21, 111.22, 87.43, 57.12]
    tester.test(tree.postorder_traversal(tree.get_head()), post_result)


if __name__ == "__main__":
    # main()
    test()