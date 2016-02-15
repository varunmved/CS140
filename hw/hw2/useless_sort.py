import matplotlib as mp

#a divide and conquer  with run time T(n) = 2T(n/3) + O(n^2)
#this implies n/3 runtime in our sort, and n^2 runtime within each partion


def useless_sort(a, low, mid, high):
    #check
    al = len(a)
    if al < 3:
        return a
    
    first_third = (1/3)*al
    second_third = (2/3)*al
    
    a0 = a[0:first_third]
    a1 = a[first_third+1:second_third]
    a2 = a[second_third+1:]



    #check funny
    if (a[0:(1/3)*al)

    #split
    useless_sort(a[0:(1/3)*al])
    useless_sorta[
    
