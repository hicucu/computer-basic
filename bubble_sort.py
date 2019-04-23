def bubble_sort(li):
    
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i]>li[j]:
                li[i],li[j] = li[j], li[i]            

if __name__=="__main__":
    li=[6,2,1,4]
    bubble_sort(li)
    print(li)