#!/usr/bin/env python
# coding: utf-8

# In[319]:


class node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
class tree:
    def __init__(self):
        self.root=None
        
    def insert(self,val):
        if self.root==None :
            self.root=node(val)
            print(self.root.val)
        
        else:
            prev_pointer=None
            pointer=self.root
            
            while pointer!=None:
                prev_pointer=pointer
                
                if pointer.val>=val:
                    pointer=pointer.left
                    
                else:
                    pointer=pointer.right
                    
            if prev_pointer.val<val:
                prev_pointer.right=node(val)
                print(f'inserted as right child of {prev_pointer.val}')
            else:
                prev_pointer.left=node(val)
                print(f'inserted as left child of {prev_pointer.val}')
        
    def inorder(self,pointer):

        if pointer==None:
            return
        
        self.inorder(pointer.left)
        print(pointer.val, end=',')
        self.inorder(pointer.right)
    
    
    def preorder(self,pointer):
        
        if pointer==None:
            return
        
        print(pointer.val, end=',')
        self.preorder(pointer.left)
        self.preorder(pointer.right)
        
    def postorder(self,pointer):
        
        if pointer==None:
            return
        
        self.postorder(pointer.left)
        self.postorder(pointer.right)
        print(pointer.val, end=',')
        
#     returns root node
    def return_root(self):
        return self.root
    
#     returns node with minimum value
    def find_min(self,pointer):
        
        while pointer.left!=None:
            pointer=pointer.left
        return pointer
    
#     delete a node with recurssion
    def delete_node(self,pointer,val):
        if pointer==None:
            return pointer
        
#         passing left node as pointer in delete_node
        elif val<pointer.val:
            pointer.left=self.delete_node(pointer.left,val)
            
#         passing right node as pointer in delete_node
        elif val>pointer.val:
            pointer.right=self.delete_node(pointer.right,val)
            
#         if element found
        else:
#         if leaf node then just delete
            if pointer.left==None and pointer.right==None:
                del(pointer)
                return None
            
#         if node has only right element then just connect right node
            elif pointer.left == None:
                temp=pointer
                pointer=pointer.right
                
#                 delete temp to free memory
                del(temp)
                
#         if node has only left node then just connect left node 
            elif pointer.right ==None:
                temp=pointer
                pointer=pointer.left
                del(temp)
            
#         if node has two child node ----> find node with minimum value and swap with node to be deleted ----> delete leaf node (minimum element node)
            else:
                temp=self.find_min(pointer.right)
                pointer.val=temp.val
                pointer.right=self.delete_node(pointer.right,temp.val)
                del(temp)
                
#         return final pointer
        return pointer
            
        


# In[320]:


t1=tree()


# In[321]:


t1.insert(20)
t1.insert(10)
t1.insert(30)
t1.insert(5)
t1.insert(15)
t1.insert(25)
t1.insert(35)
t1.insert(1)
t1.insert(6)
t1.insert(11)
t1.insert(16)


# In[322]:


t1.inorder(t1.return_root())


# In[323]:


t1.preorder(t1.return_root())


# In[324]:


t1.postorder(t1.return_root())


# In[325]:


t1.delete_node(t1.return_root(),35).val


# In[326]:


t1.inorder(t1.return_root())


# In[ ]:





# In[ ]:




