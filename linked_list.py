#!/usr/bin/env python
# coding: utf-8

# In[14]:


class node:

    def __init__(self,val):
        self.val=val
        self.next=None

class llist:
    def __init__(self):
        self.head=None
        
    
    def insert_beg(self,v):
        '''insert at begining'''
        temp=self.head
        self.head=node(v)
        self.head.next=temp
        
    
    def insert_at_end(self,v):
        '''insert at end'''
        temp=self.head
        if self.head==None:
            self.insert_beg(v)
            return
        while temp.next!=None:
            temp=temp.next
        temp.next=node(v)
        
    
    def insert_in_btw(self,v,pos):
        '''
            insert at any position 
            if pos=1 then insert_beg is called
            if pos>len(list) then element is inserted at last position
        '''
        if pos==1:
            self.insert_beg(v)
        else:
            temp=self.head
            i=1
            while (temp!=None) and (i!=pos-1):
                temp=temp.next
                i+=1
            if temp==None:
                self.insert_at_end(v)
                print('added at last pos')
            else:
                temp2=temp.next
                temp.next=node(v)
                temp.next.next=temp2
    
    
    def del_beg(self):
        '''delete starting element'''
        temp=self.head
        self.head=self.head.next
        temp.next=None
        
    
    def del_end(self):
        '''delete end element'''
        temp=self.head
        if temp.next:
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
        elif temp.next==None:
            del(temp)
            self.head=None
        elif temp==None:
            print('list is empty')
            
            
    # delete at any position
    # if pos=1 then del_beg is called
    # if pos>len(linked list) then last element is deleted
    def del_in_btw(self,pos):
        '''
            delete at any position
            if pos=1 then del_beg is called
            if pos>len(linked list) then last element is deleted
        '''
        if pos==1:
            self.del_beg()
            return
        
        prev=self.head
        if prev.next:
            temp=prev.next
        else:
            self.del_end()
            return
        i=1
        while (temp!=None) and (i!=pos-1):
            prev=temp
            temp=temp.next
            i+=1
        if temp==None:
            self.del_end()
            return
        prev.next=temp.next
        del(temp)
        # temp.next=None
        
        
    def printall(self):
        '''print all elements of list'''
        temp=self.head
        if temp==None:
            print('empty')
        while temp!=None:
            print(temp.val,end=' --> ')
            temp=temp.next


# In[11]:


help(llist.del_in_btw)


# In[15]:


a=llist()


# In[16]:


a.insert_at_end(1)


# In[17]:


a.printall()


# In[18]:


a.del_end()


# In[19]:


a.printall()


# In[ ]:




