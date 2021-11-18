def solution(clothes):
    answer, cart = 1, []
    for clo in clothes: cart.append(clo[1])
    n_cart, d_cart = set(cart), dict()
    for n in n_cart:    d_cart[n] = 0
    for ca in cart:     d_cart[ca] += 1
    for i in d_cart.values():   answer *= (int(i)+1)
    return answer-1