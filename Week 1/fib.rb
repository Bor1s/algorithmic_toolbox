# Regular divide and conquer algorithm
def fib(n)
  return 0 if n < 0 || n == 0
  if n == 1
    n
  else
    fib(n - 1) + fib(n - 2)
  end
end

# External fib numbers memo
#@h = {0 => 0, 1 => 0, 2 => 1, 3 => 1}
@h = {0 => 0, 1 => 1, 2 => 1}
def fib2(n)
  if @h[n] == nil
    @h[n] = fib2(n-1) + fib2(n-2)
  else
    return @h[n]
  end
end

puts fib2(3)