'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

import unittest

# from math import pi
#
# def crash_cone(user_radius, user_height):
#     vol_of_cone = user_radius * user_radius * pi * user_height / 3
#     return (vol_of_cone)
#
#
# class BugTestCase(unittest.TestCase):
# #Test for crash_cone.py
#
#     def test_cone_volume_right(self):
#         #do you get the cone vol
#         con_vol = crash_cone(1,3)
#         self.assertEqual(con_vol, pi)
#
#     def test_for_idiots(self):
#         con_vol = crash_cone(1,3)
#         self.assertIs(con_vol, pi)


def survival_test(bug, bird):
    if len(bug) <= len(bird):
        return "Bug got eaten"
    else:
        return False


class BugTestCase(unittest.TestCase):

    def test_survival_of_bug(self):
        bug_status = survival_test("ant", "pidgeon")
        self.assertEqual(bug_status, "Bug got eaten")

    def test_bug_death(self):
        bug_status = survival_test("caterpillar", "robin")
        self.assertIs(bug_status, False)

    def test_bug_alive(self):
        bug_status = survival_test("centipede", "robin")
        self.assertTrue(bug_status, False)


if __name__ == '__main__':

    unittest.main()
