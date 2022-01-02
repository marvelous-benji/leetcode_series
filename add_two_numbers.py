

class LinkedList:
    '''
    Basic implementation of a LinkedList
                Data Structure
    '''
    def __init__(self,value, node=None):
        self.value = value
        self.next = node

    def __len__(self):
        '''Returns the length of the LinkedList'''
        count = 1
        next = self.next
        while next:
            count += 1
            next = next.next
        return count

    def __repr__(self):
        '''Returns a proper visualisation of the LinkedList'''
        repr = f'{self.value}'
        next = self.next
        while next:
            repr += f'-->{next.value}'
            next = next.next
        return repr

    @staticmethod
    def generate_list(arr):
        '''Generates a LinkedList from an iterable'''
        head = __class__(None)
        instance = __class__(arr[0])
        head.next = instance
        for k in arr[1:]:
            instance.next = __class__(k)
            instance = instance.next
        return head.next

            



def add_two_linkedlist(lkd1,lkd2):
    remainder, excess = (lkd1.value + lkd2.value)%10, (lkd1.value + lkd2.value)//10
    head = LinkedList(None)
    lkd1 = lkd1.next
    lkd2 = lkd2.next
    instance = LinkedList(remainder)
    head.next = instance
    while (lkd1 or lkd2):
        if lkd1:
            value1 = lkd1.value
            lkd1 = lkd1.next
        else:
            value1 = 0
        if lkd2:
            value2 = lkd2.value
            lkd2 = lkd2.next
        else:
            value2 = 0
        remainder, excess = (value1 + value2 + excess)%10, (value1 + value2 + excess)//10
        instance.next = LinkedList(remainder)
        instance = instance.next
    if excess != 0:
        instance.next = LinkedList(excess)
    return head.next
        
