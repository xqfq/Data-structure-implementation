from Stack import *
def stack_test():
    s=Stack(3)
    assert s.isEmpty() == 1,'isEmpty method fails when the stack is empty'
    assert s.stackList == [0,0,0],'Initialization failed'
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.size() == 3,'Size method fails'
    assert s.stackList == [1,2,3],'Push method without expansion failed'
    s.push(4)
    assert s.size() == 4,'Size method fails after expanding'
    assert s.stackList == [1,2,3,4,0,0],'Push method with expansion failed'
    assert s.pop() == 4,'Pop method fails to return the right item'
    assert s.stackList == [1,2,3,0,0,0],'Pop method fails to delete the right item'
    assert s.size() == 3,'Size method fails after popping'
    assert s.isEmpty() == 0,'isEmpty method fails when the stack is not empty'
    print('Stack class works.')
stack_test()
