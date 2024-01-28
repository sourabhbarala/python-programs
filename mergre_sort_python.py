#!/usr/bin/env python
# coding: utf-8

# In[65]:


def merge(arr,first,mid,last):
    
    print('----------------------------------------------------------------------')
    
#     making sub left and right lists
    left_list=arr[first:(mid+1)]
    right_list=arr[(mid+1):(last+1)]

    print(f'main list to be sorted:{arr[first:(last+1)]}\nright list:{right_list}\nleft list:{left_list}')
    
#     starting index of left and right list
    i,j=0,0
    
#     main list (list to be sorted) will be killed from 'k' index
    k=first
    
#     getting length of right and left list
    len_right_list,len_left_list=len(right_list),len(left_list)
    
#     if both list have elements then compare and fill smaller element in main list
    while i<len_right_list and j<len_left_list:
        
        print('both sub lists have elements')
        
#         compare elements
        if right_list[i]<=left_list[j]:
        
#         put smaller elemnet in sorted list
            arr[k]=right_list[i]
            i+=1
            k+=1
            
        else:
            arr[k]=left_list[j]
            j+=1
            k+=1
            
        print(f'main array after fill: {arr[first:(last+1)]}\n')
    
#     once elements of one list are complete, put all the elements of other list in main list
    while j<len_left_list:
        print('filling left elemets of left list')
        arr[k]=left_list[j]
        j+=1
        k+=1
        
    while i<len_right_list:
        print('filling left elemets of right list')
        arr[k]=right_list[i]
        i+=1
        k+=1
        
#         main list (partly sorted)
    print(f'both sub lists are empty\nfinal main list: {arr}')
    print('----------------------------------------------------------------------\n\n')
    

def merge_sort(arr,first,last):
    if not (first<last):
        print('(only one element, hence return)\n')
        
#         check is more than one element is present
    if first<last:
        
#         calculate mid element by floor division (5//2 = 2)
        mid=(first+last)//2
    
        print(f'mid value = ({first} + {last})//2 = {mid}')
        print(f'< calling merge_sort( first = {first}, last = mid = {mid}) >\n')
#         call the same function for right sub list
        merge_sort(arr,first,mid)
    
        print(f'mid value = {mid}')
        print(f'< calling merge_sort( first = (mid+1) = {mid+1}, last = {last}) >\n')    
#         call the same function for left sub list
        merge_sort(arr,mid+1,last)
    
        print(f'< calling merge(first = {first}, mid = {mid}, last = {last}) >\n')
#         function to compare element of both sub list and make a sorted list
        merge(arr,first,mid,last)
        


# In[69]:


arr=[9,8,7,6,5,3,3,2,1,11,0]
merge_sort(arr,0,(len(arr)-1))


# In[68]:


arr


# In[ ]:




