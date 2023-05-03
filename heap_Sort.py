class Solution:

    #Heapify function to maintain heap property.

    def heapify(self,arr, n, i):

        # code here

        largest=i

        leftchild=2*i+1

        rightchild=2*i+2

        if leftchild<n and arr[leftchild]>arr[largest]:

            largest=leftchild

        if rightchild<n and arr[rightchild]>arr[largest]:

            largest=rightchild

        if largest!=i:

            arr[i],arr[largest]=arr[largest],arr[i]

            self.heapify(arr,n,largest)

    

    #Function to build a Heap from array.

    def buildHeap(self,arr,n):

        # code here

        i=n//2-1

        while i>=0:

            self.heapify(arr,n,i)

            i-=1

    

    #Function to sort an array using Heap Sort.    

    def HeapSort(self, arr, n):

        #code here

        self.buildHeap(arr,n)

        j=n-1

        while j>=0:

            arr[0],arr[j]=arr[j],arr[0]

            self.heapify(arr,j,0)

            j-=1