import numpy as np
import typing
from collections import defaultdict

# define the prices to be tested 
prices_to_test = np.arange(2.49, 5.99, 1)

# define the prior values for the alpha and beta that define a gamma distribution
# Feel free to change the values of alpha and beta and experiment with them. They are not set in stone. 
alpha_0 = 30.00     
beta_0 = 1.00

def sample_true_demand(price: float) -> float:
    demand = alpha_0 + beta_0 * price
    return np.random.poisson(demand, 1)[0]


class priceParams(typing.TypedDict):
    price: float
    alpha: float
    beta: float

# Build a list of priceParams for all the prices to be tested.
p_lambdas = [] 
for price in prices_to_test:
    p_lambdas.append(
        priceParams(
            price=price, 
            alpha=alpha_0, 
            beta=beta_0
        )
    )
    
   
class OptimalPriceResult(typing.NamedTuple):
    
    price: float
    price_index: int
        
def get_optimal_price(prices, demands):
    index = np.argmax(prices * demands)
    return OptimalPriceResult(price_index = index, price = prices[index])

def sample_demands_from_model(p_lambdas):
    return list(map(lambda v: np.random.gamma(v['alpha'], 1/v['beta']), p_lambdas))


price_counts = defaultdict(lambda: 0)

for t in range(200):
    
    # Sample demands from the model
    demands = sample_demands_from_model(p_lambdas)

    # pick the price that maximizes the revenue
    optimal_price_res = get_optimal_price(prices_to_test, demands)
    
    # increase the count for the price
    price_counts[optimal_price_res.price] += 1

    # offer the selected price and observe demand
    demand_t = sample_true_demand(optimal_price_res.price)

    # update model parameters/ Update our Belief. 
    v = p_lambdas[optimal_price_res.price_index]
    v['alpha'] += demand_t
    v['beta'] += 1