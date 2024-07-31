def main():
  x = int(input("k: ")
  series,a,b=[0,1],0,1
  while b<x:
    a,b=b,a+b
    if b<x:
      series.append(b)
  for number in series:
    print(number)
    sum_even_indexed = sum(series[i] for i in range(0,len(series),2))
    print(f"sum:{sum_even_indexed}")
    main()
    
