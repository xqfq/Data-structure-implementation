from Queue import *

def Queue_test():
    # initialization
    q = Queue(2)
    assert q.size() == 0, 'initialization fails, size'
    assert q.isEmpty() == 1, 'initialization fails isEmpty'
    assert q.capacity() == 2, 'initialization fails, capacity'
    # add an element
    q.enqueue(1)
    assert q.size() == 1, 'enqueue fails, size'
    assert q.isEmpty() == 0, 'enqueue fails isEmpty'
    assert q.capacity() == 2, 'enqueue fails, capacity'
    assert q.front() == 1, 'front fails'
    # dequeue an element
    assert q.dequeue() == 1, 'dequeue fails'
    assert q.size() == 0, 'dequeue fails, size'
    assert q.isEmpty() == 1, 'dequeue fails isEmpty'
    assert q.capacity() == 2, 'dequeue fails, capacity'
    # fill the queue
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2, 'enqueue fails, size'
    assert q.isEmpty() == 0, 'enqueue fails isEmpty'
    assert q.capacity() == 2, 'enqueue fails, capacity'
    assert q.front() == 1, 'front fails'
    # empty the queue
    q.dequeue()
    assert q.dequeue() == 2, 'dequeue fails'
    assert q.size() == 0, 'dequeue fails, size'
    assert q.isEmpty() == 1, 'dequeue fails isEmpty'
    assert q.capacity() == 2, 'dequeue fails, capacity'
    # expand the queue
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3, 'enqueue fails, size'
    assert q.isEmpty() == 0, 'enqueue fails isEmpty'
    assert q.capacity() == 4, 'enqueue fails, capacity'
    assert q.front() == 1, 'front fails'
    print('queue object works')
Queue_test()
