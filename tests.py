import fastlab
def test1():
 assert fastlab.sum_two_args(2,2) == 4
def test2():
 assert fastlab.sum_two_args(2.0001,2) == 4