from linked_list import Node
from linked_list import LinkedList as LList

import unittest

class TestLinkedList(unittest.TestCase):
    def test_init(self):
        ll = LList([2, 5, 7])
        self.assertEqual(list(ll), [2, 5, 7])
        self.assertEqual(len(ll), 3)

        ll = LList()
        self.assertEqual(list(ll), [])
        self.assertEqual(len(ll), 0)

        ll = LList([])
        self.assertEqual(list(ll), [])
        self.assertEqual(len(ll), 0)

    def test_convert(self):
        self.assertEqual(list(LList([6])), [6])
        self.assertEqual(list(LList([[2, 4], [8, 2]])), [[2, 4], [8, 2]])
        self.assertEqual(list(LList(["five", 6, 7.3, 103])), ["five", 6, 7.3, 103])
        self.assertEqual(tuple(LList([3, 7, 64, 1])), (3, 7, 64, 1))
        self.assertEqual(set(LList([64, 754, 673])), {64, 754, 673})

    def test_display(self):
        self.assertEqual(LList([6]).display(), "[Head: 6]")
        self.assertEqual(LList(["one", "two"]).display(), "[Head: one] -> [Tail: two]")
        self.assertEqual(LList([4.3, 5.8, 10.2, 1.2]).display(), "[Head: 4.3] -> [5.8] -> [10.2] -> [Tail: 1.2]")

    def test_str(self):
        self.assertEqual(str(LList([4, 8, 1, 4])), "[4, 8, 1, 4]")
        self.assertEqual(str(LList([2.5])), "[2.5]")
        self.assertEqual(str(LList([4.3, 5.8, 10.2, 1.2])), "[4.3, 5.8, 10.2, 1.2]")

    def test_defulats(self):
        ll = LList([0, -6, 2, 7, -3, 5])
        self.assertEqual(min(ll), -6)
        self.assertEqual(max(ll), 7)
        self.assertEqual(sum(ll), 5)

        self.assertEqual(len(ll), 6)

    def test_equal(self):
        self.assertTrue(LList([4,2,8])==LList([4,2,8]))
        self.assertTrue(LList([1, 8, 3, 6])==LList([1, 8, 3, 6]))
        self.assertTrue(LList([])==LList([]))

        self.assertFalse(LList([1, 6, 2])==LList([1, 6, 2, 4]))
        self.assertFalse(LList([5, 2, 8])==LList([1, 7, 7]))
        self.assertFalse(LList(["abcd", "efg"])==LList(["abcd", "efX"]))

        self.assertFalse(LList([1]) == 0)

    def test_not_equal(self):
        self.assertTrue(LList([1, 6, 2])!=LList([1, 6, 2, 4]))
        self.assertTrue(LList([5, 2, 8])!=LList([1, 7, 7]))
        self.assertTrue(LList(["abcd", "efg"])!=LList(["abcd", "efX"]))

        self.assertFalse(LList([4,2,8])!=LList([4,2,8]))
        self.assertFalse(LList([1, 8, 3, 6])!=LList([1, 8, 3, 6]))
        self.assertFalse(LList([])!=LList([]))

        self.assertTrue(LList([1]) != 0)
    
    def test_iter(self):
        pl = [6, 2, 5, 1, 12, 6, 456]
        ll = LList(pl)
        for item1, item2 in zip(pl, ll):
            self.assertEqual(item1, item2)

    def test_contains(self):
        ll = LList([6, 2, 5, 1, 12, 6, 456])
        self.assertTrue(6 in ll)
        self.assertTrue(1 in ll)
        self.assertTrue(456 in ll)

        self.assertFalse(-5 in ll)
        self.assertFalse(13 in ll)
    
    def test_bool(self):
        self.assertTrue(bool(LList([4])))
        self.assertTrue(bool(LList([7, 2, 3])))

        self.assertFalse(bool(LList()))
        self.assertFalse(bool(LList([])))

        self.assertTrue(LList().is_empty())
        self.assertFalse(LList([1]).is_empty())

    def test_append(self):
        ll = LList()
        self.assertEqual(list(ll), [])
        self.assertEqual(len(ll), 0)
        ll.append(4)
        self.assertEqual(ll, LList([4]))
        self.assertEqual(list(ll), [4])
        self.assertEqual(len(ll), 1)
        ll.append(7)
        self.assertEqual(ll, LList([4, 7]))
        self.assertEqual(list(ll), [4, 7])
        self.assertEqual(len(ll), 2)
        ll.append(2)
        self.assertEqual(ll, LList([4, 7, 2]))
        self.assertEqual(list(ll), [4, 7, 2])
        self.assertEqual(len(ll), 3)
    
    def test_prepend(self):
        ll = LList([5, 3])
        self.assertEqual(list(ll), [5, 3])
        self.assertEqual(len(ll), 2)
        ll.prepend(-6)
        self.assertEqual(ll, LList([-6, 5, 3]))
        self.assertEqual(list(ll), [-6, 5, 3])
        self.assertEqual(len(ll), 3)
        ll.prepend(-23)
        self.assertEqual(ll, LList([-23, -6, 5, 3]))
        self.assertEqual(list(ll), [-23, -6, 5, 3])
        self.assertEqual(len(ll), 4)
        ll.prepend(13)
        self.assertEqual(ll, LList([13, -23, -6, 5, 3]))
        self.assertEqual(list(ll), [13, -23, -6, 5, 3])
        self.assertEqual(len(ll), 5)

        ll = LList()
        ll.prepend(0)
        self.assertEqual(ll, LList([0]))
        self.assertEqual(list(ll), [0])
        self.assertEqual(len(ll), 1)
    
    def test_exstend(self):
        ll = LList([1, 2, 3])
        ll.extend([4, 5])
        self.assertEqual(ll, LList([1, 2, 3, 4, 5]))
        self.assertEqual(list(ll), [1, 2, 3, 4, 5])
        self.assertEqual(len(ll), 5)
        ll.extend([6, 7])
        self.assertEqual(ll, LList([1, 2, 3, 4, 5, 6, 7]))
        self.assertEqual(list(ll), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(len(ll), 7)

        ll = LList()
        ll.extend([4, 5])
        self.assertEqual(ll, LList([4, 5]))
        self.assertEqual(list(ll), [4, 5])
        self.assertEqual(len(ll), 2)

    def test_len(self):
        ll = LList()
        self.assertEqual(len(ll), 0)

        ll = LList([2, 3])
        self.assertEqual(len(ll), 2)
        ll.append(4)
        self.assertEqual(len(ll), 3)
        ll.prepend(1)
        self.assertEqual(len(ll), 4)
        ll.pop()
        self.assertEqual(len(ll), 3)
        ll.append(5)
        self.assertEqual(len(ll), 4)
        ll.append(6)
        self.assertEqual(len(ll), 5)
        del ll[2]
        self.assertEqual(len(ll), 4)
        # ll.remove(3)
        # self.assertEqual(len(ll), 3)
        ll.clear()
        self.assertEqual(len(ll), 0)
    
    def test_clear(self):
        ll = LList([4, 6, 2])
        ll.clear()
        self.assertEqual(ll, LList())
        self.assertEqual(len(ll), 0)
    
    def test_copy(self):
        ll1 = LList([1, 3])
        ll2 = ll1.copy()
        self.assertFalse(ll1 is ll2)
        self.assertEqual(ll1, ll2)
        ll2.append(3)
        self.assertNotEqual(ll1, ll2)

        ll1 = LList()
        ll2 = ll1.copy()
        self.assertFalse(ll1 is ll2)
        self.assertEqual(ll1, ll2)
        ll1.append(3)
        self.assertNotEqual(ll1, ll2)
    
    def test_pop(self):
        ll = LList([1, 2, 3, 5, 6, 7, 8])
        self.assertEqual(ll.pop(), 8)
        self.assertEqual(ll, LList([1, 2, 3, 5, 6, 7]))
        self.assertEqual(len(ll), 6)

        self.assertEqual(ll.pop(0), 1)
        self.assertEqual(ll, LList([2, 3, 5, 6, 7]))
        self.assertEqual(len(ll), 5)

        self.assertEqual(ll.pop(2), 5)
        self.assertEqual(ll, LList([2, 3, 6, 7]))
        self.assertEqual(len(ll), 4)

        self.assertEqual(ll.pop(-2), 6)
        self.assertEqual(ll, LList([2, 3, 7]))
        self.assertEqual(len(ll), 3)
        
        self.assertEqual(ll.pop(), 7)
        self.assertEqual(ll, LList([2, 3]))
        self.assertEqual(len(ll), 2)

        self.assertEqual(ll.pop(), 3)
        self.assertEqual(ll, LList([2]))
        self.assertEqual(len(ll), 1)

        self.assertEqual(ll.pop(), 2)
        self.assertEqual(ll, LList([]))
        self.assertEqual(len(ll), 0)
        
        ll = LList([1])

        with self.assertRaises(IndexError) as exc:
            ll.pop(2)
        self.assertEqual(str(exc.exception), "pop index out of range")

        self.assertEqual(ll.pop(), 1)

        with self.assertRaises(IndexError) as exc:
            ll.pop()
        self.assertEqual(str(exc.exception), "pop from empty list")

    def test_insert(self):
        ll = LList([2, 4, 5])
        ll.insert(3, 6)
        self.assertEqual(ll, LList([2, 4, 5, 6]))
        ll.insert(0, 1)
        self.assertEqual(ll, LList([1, 2, 4, 5, 6]))
        ll.insert(2, 3)
        self.assertEqual(ll, LList([1, 2, 3, 4, 5, 6]))

        self.assertEqual(len(ll), 6)

    def test_index(self):
        ll = LList([1, 3, 5])
        self.assertEqual(ll.index(3), 1)
        self.assertEqual(ll.index(5), 2)

        with self.assertRaises(ValueError) as exc:
            ll.index(100)
        self.assertEqual(str(exc.exception), "100 is not in LinkedList")
    
    def test_count(self):
        ll = LList([1, 3, 5, 5, 6, 7, 8, 8, 8, 9])
        self.assertEqual(ll.count(1), 1)
        self.assertEqual(ll.count(5), 2)
        self.assertEqual(ll.count(8), 3)
        self.assertEqual(ll.count(10), 0)
    
    def test_remove(self):
        ll = LList([1, 2, 3, 4])
        ll.remove(4)
        self.assertEqual(ll, LList([1, 2, 3]))
        ll.remove(2)
        self.assertEqual(ll, LList([1, 3]))
        ll.remove(1)
        self.assertEqual(ll, LList([3]))
        ll.remove(3)
        self.assertEqual(ll, LList([]))
    
    def test_getitem(self):
        ll = LList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(ll[0], 0)
        self.assertEqual(ll[8], 8)
        self.assertEqual(ll[4], 4)
        self.assertEqual(ll[9], 9)
        self.assertEqual(ll[-1], 9)
        self.assertEqual(ll[-4], 6)
    
    def test_getitem_slice(self):
        ll = LList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(ll[:], LList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(ll[4:], LList([4, 5, 6, 7, 8, 9]))
        self.assertEqual(ll[:4], LList([0, 1, 2, 3]))
        self.assertEqual(ll[2:-2], LList([2, 3, 4, 5, 6, 7]))
        self.assertEqual(ll[-5:-1:], LList([5, 6, 7, 8]))
        self.assertEqual(ll[::2], LList([0, 2, 4, 6, 8]))
        self.assertEqual(ll[1::2], LList([1, 3, 5, 7, 9]))
        self.assertEqual(ll[3::3], LList([3, 6, 9]))
        self.assertEqual(ll[2::4], LList([2, 6]))
    
    def test_setitem(self):
        ll = LList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        ll[9] = 0
        self.assertEqual(ll, LList([0, 1, 2, 3, 4, 5, 6, 7, 8, 0]))
        ll[4] = 0
        self.assertEqual(ll, LList([0, 1, 2, 3, 0, 5, 6, 7, 8, 0]))
        ll[-1] = 1
        self.assertEqual(ll, LList([0, 1, 2, 3, 0, 5, 6, 7, 8, 1]))
        ll[-6] = 0
        self.assertEqual(ll, LList([0, 1, 2, 3, 0, 5, 6, 7, 8, 1]))

        with self.assertRaises(IndexError) as exc:
            ll[100] = 0
        self.assertEqual(str(exc.exception), "LinkedList index out of range")
        with self.assertRaises(IndexError) as exc:
            ll[-100] = 0
        self.assertEqual(str(exc.exception), "LinkedList index out of range")

    def test_delitem(self):
            ll = LList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            del ll[9]
            self.assertEqual(ll, LList([0, 1, 2, 3, 4, 5, 6, 7, 8]))
            del ll[0]
            self.assertEqual(ll, LList([1, 2, 3, 4, 5, 6, 7, 8]))
            del ll[4]
            self.assertEqual(ll, LList([1, 2, 3, 4, 6, 7, 8]))
            del ll[2]
            self.assertEqual(ll, LList([1, 2, 4, 6, 7, 8]))
            del ll[-1]
            self.assertEqual(ll, LList([1, 2, 4, 6, 7]))
            del ll[-3]
            self.assertEqual(ll, LList([1, 2, 6, 7]))

            self.assertEqual(len(ll), 4)

            with self.assertRaises(IndexError) as exc:
                del ll[100]
            self.assertEqual(str(exc.exception), "LinkedList index out of range")
            with self.assertRaises(IndexError) as exc:
                del ll[-100]
            self.assertEqual(str(exc.exception), "LinkedList index out of range")

    def test_add(self):
        self.assertEqual(LList([])+LList([]), LList([]))
        self.assertEqual(LList([1])+LList([5]), LList([1, 5]))
        self.assertEqual(LList([1, 2, 3])+LList([4, 5, 6]), LList([1, 2, 3, 4, 5, 6]))
        
        ll = LList([1, 2, 3])
        ll += LList([4, 5, 6])
        self.assertEqual(ll, LList([1, 2, 3, 4, 5, 6]))

    def test_mul(self):
        ll = LList([1, 2, 3])
        self.assertEqual(ll*2, LList([1, 2, 3, 1, 2, 3]))
        ll *= 10
        self.assertEqual(ll, LList([1, 2, 3]*10))

    def test_reverse(self):
        ll = LList([1, 2, 3, 4])
        self.assertEqual(reversed(ll), LList([4, 3, 2, 1]))

        ll.reverse()
        self.assertEqual(ll, LList([4, 3, 2, 1]))

if __name__ == "__main__":
    unittest.main()
