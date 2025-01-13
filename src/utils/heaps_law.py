import math

class Calculate:
  
  def coefficients_calculator(V1 : int, N1 : int, V2 : int, N2 : int):
    # V = k * N^b 
    # log(V) = b * log(N) + log(k)
    
    # log(V1) = b * log(N1) + log(k)
    # log(V2) = b * log(N2) + log(k)
    # log(V1) - log(V2) = b * (log(N1) - log(N2))
    # b = (log(V1) - log(V2)) / (log(N1) - log(N2))
    b = (math.log(V1) - math.log(V2)) / (math.log(N1) - math.log(N2))

    # log(k) = log(V1) - b * log(N1)
    # k = e ^ (log(V1) - b * log(N1))
    k = math.exp(math.log(V1) - b * math.log(N1))

    return b, k