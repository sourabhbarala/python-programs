#!/usr/bin/env python
# coding: utf-8

# In[73]:


def partition(arr,pivot,q):
#     p is one more than pivot
    print('----------------------------------------------------------------------------------')
    p=pivot+1
    print(f'pivot index: {pivot}\np index: {p}\nq index: {q}\n')
#     run till p is smaller than q
    while True: 
#         find the bigger element than pivot
        while p<len(arr) and arr[pivot]>arr[p] :
            p+=1
#         find smaller element than pivot
        while q>-1 and arr[q]>arr[pivot]:
            q-=1
            
#         if element found, and p and q do not cross each other ----> swap p and q
        if p<q :
            print(f'found\nbigger element at index: {p}\nsmaller element at index: {q}')
            print(f'array before swapping p and q\n{arr}')
            temp=arr[p]
            arr[p]=arr[q]
            arr[q]=temp
            print(f'array after swapping p and q\n{arr}\n')
            
#         if p and q cross each other, than swap pivot and q
        else:
            print(f'p and q crossed each other\npivot index: {pivot}\np index: {p}\nq index: {q}')
            print(f'array before swapping pivot and q\n{arr}')
            
            temp=arr[pivot]
            arr[pivot]=arr[q]
            arr[q]=temp
            
            print(f'after swaping pivot and q\n{arr}\n')
#             since p>q break loop
            break
#     return the position of sorted element
    print(f'returning index of sorted element:{q}')
    print('----------------------------------------------------------------------------------\n\n')
    return q

def quicksort(arr,pivot,q):
    
    print(f'< quick sort(pivot index: {pivot}, q index: {q}) >')
    if not (pivot<q):print('(no need to sort, hence return)')
#     pivot==q means only one element   ---->   no need to sort
    if pivot<q:
#     call partition to sort the array and get sortted index
        print(f'< calling partition(pivot = {pivot}, q = {q})')
        sorted_pos=partition(arr,pivot,q)
#     call quicksort to sort the left part of sorted index
        print(f'< calling quicksort(pivot index = {pivot}, q index =  {sorted_pos-1}) >')
        quicksort(arr,pivot,sorted_pos-1)
#     call quicksort to sort the right part of the sorted index
        print(f'< calling quicksort(pivot index = {sorted_pos+1}, q index = {q}) >')
        quicksort(arr,sorted_pos+1,q)


    
            


# In[74]:


ar=[12,11,13,9,20,7,6,5,4,3,2,1]
quicksort(ar,0,len(ar)-1)


# In[72]:


ar


# In[ ]:




