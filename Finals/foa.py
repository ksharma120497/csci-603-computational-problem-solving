def a(arr):
  r=len(arr)-1
  l=0
  target=arr[-1]/2
  m = (l + r) // 2
  if () > target/2:
    print("YES")
    return
  while(l<=r and len(arr[l:r+1])>3):
    m = (l + r) // 2
    if arr[m]>target:
      r=m
    else:
      l=m
  x=arr[l:]
  x=x[:3]
  x[2]-=x[1]
  x[1]-=x[0]
  if l>0:
      x[0]-=arr[l-1]

  if sum(x)>=target:
    print("YES")
  else:
    print("NO")



if __name__ == "__main__":
    # input()
    # arr=list(map(int,input().split()))
    # a(arr)
    a([1,1,1,5,5,6,9])