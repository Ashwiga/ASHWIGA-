def alpha_bets(p, q):  
  new_p = q[:2] + p[2:]  
  new_q = p[:2] + q[2:]  
  
  return new_p + ' ' + new_q  
print(alpha_bets('pqr', 'xyz'))  
