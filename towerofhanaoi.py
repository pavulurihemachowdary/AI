def TowerOfHanoi(n,from_rod,to,aux):
    if n==1:
        print("move disk 1 from",from_rod,"to",to)
        return
    TowerOfHanoi(n-1,from_rod,aux,to)
    print("move disk",n,"from",from_rod,"to",to)
    TowerOfHanoi(n-1,aux,to,from_rod)
n=3
TowerOfHanoi(n,'A','C','B')