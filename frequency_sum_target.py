'''Dustin and Erica have discovered a hidden network of n communication nodes in the Starcourt Mall. Each node i (1≤i≤n) has a specific frequency ai.

To contact Suzie and save the world, the frequencies must be arranged in non-decreasing order (i.e., a1≤a2≤⋯≤an).

However, the Mind Flayer has corrupted the network. You cannot simply move the frequencies around. You can only swap the frequencies of two nodes i and j if there exists a conductive path between them.

A direct connection exists between two nodes i and j if and only if:
(ai+aj) is an odd number

If there is a sequence of direct connections (e.g., i→k→j), then a conductive path exists between i and j, and you can swap their values.

Dustin asks you: Is it possible to sort the entire network using any number of swaps?
Input

The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains an integer n (1≤n≤2⋅105) — the number of nodes.

The second line contains n integers a1,a2,…,an (1≤ai≤109) — the initial frequencies.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.
Output

For each test case, output "YES" if it is possible to sort the array, and "NO" otherwise.
Example
Input
Copy

7
3
2 4 6
3
2 3 4
4
1 5 3 7
5
1 2 100 2 101
1
10
2
10 5
2
5 3

Output
Copy

YES
YES
NO
YES
YES
YES
NO'''
a = int(input())
for i in range(0,a):
    b = int(input())
    x=0
    y=0
    c = list(map(int, input().split()))


    def qs(c):
        if (len(c)<=1):
            return c
        v = c[len(c)//2]
        left = [x for x in c if x < v]
        middle = [x for x in c if x == v]
        right = [x for x in c if x > v]
        return qs(left) + middle + qs(right)
    

    if(qs(c)==c):   
      print("YES")
    else:
        for i in c:
            if i%2==0:
                x+=1
            else:
                y+=1
        if (x>0 and y>0):
           print("YES")
        else:
            print("NO")