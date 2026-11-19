import Std
namespace OptimumTwo

theorem head_square (g c x y : Int) :
  g * (g*y*y-2*c*x*y)+c*c*(x*x+y*y) =
  (g*y-c*x)^2+c*c*y*y := by
  grind

theorem mask_prefix (b e s q w d : Int) :
  1-b+e*b+b*(s+w*d)-(q+(w-1)*d) =
  (1-b+e*b+b*s-q)+d*(w*b-w+1) := by
  grind

theorem head_a_derivative (a t : Int) :
  (1+t+3*t*a*a)*(1+2*t*a*a)-4*t*a*(a+t*a+t*a*a*a) =
  1+t+t*(1-2*t)*a*a+2*t*t*a*a*a*a := by
  grind

theorem head_t_derivative (a t : Int) :
  (1+t*(1+a*a))*(1+2*a*a+4*t*a*a)-
  (1+a*a)*(1+t)*(1+2*t*a*a) =
  a*a*(1+4*t+2*(1+a*a)*t*t) := by
  grind

theorem exact_budgets :
  (1-33/500-343/500 : Rat) = 31/125 ∧
  (31/125 : Rat) > 247/1000 ∧
  (247/1000 : Rat) > 123/500 ∧
  (2*(1-123/500) : Rat) = 377/250 ∧
  (9/17-(59/96)/(4*(343/500)) : Rat) > 247/1000 ∧
  (2/5-1/32 : Rat) > 247/1000 ∧
  (247/753 : Rat) < 1/2 := by
  native_decide

end OptimumTwo
