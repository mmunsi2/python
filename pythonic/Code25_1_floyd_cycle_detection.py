'''
Created on Jun 13, 2018

@author: rajat.arora07
'''

#Has_cycle function will use 2 pointers to detect a cycle.
#In each iteration:
#The slow pointer will increment by 1.
#While the faster one will increment by 2.
#If they meet somewhere then it confirms a cycle in the list ,according to Floyd's Cycle finding algorithm.
def has_cycle(head):
    temp=head
    if temp==None:
        return False
    temp1=head.next
    if temp1==None:
        return False
    while(temp and temp1):
        temp=temp.next
        temp1=temp1.next
        temp1=temp1.next
        if temp==temp1:
            return True
    return False