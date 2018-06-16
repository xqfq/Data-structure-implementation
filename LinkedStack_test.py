from LinkedStack import *

def LinkedStack_test():
    # initialization
    s = LinkedStack()
    assert s.isEmpty() == 1,'isEmpty fails'
    assert s.first == None,'first attrbute fails'
    assert s.size() == 0,'size fails'
    # pop item when empty
    s.pop()
    assert s.size() == 0,'size fails'
    # push item
    s.push(1)
    assert s.isEmpty() == 0,'isEmpty fails'
    assert s.size() == 1,'size fails'
    # pop item
    assert s.pop() == 1,'pop fails'
    assert s.size() == 0,'size fails'
    assert s.isEmpty() == 1,'isEmpty fails'
    print('LinkedStack works')
LinkedStack_test()
