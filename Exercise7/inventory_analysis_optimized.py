import time
import random

# Step 1: Make 5000 fake products
products = []
for i in range(5000):
    products.append({
        "id": i,
        "name": f"Product_{i}",
        "price": round(random.uniform(10, 1000), 2)
    })

print("Starting analysis with 5000 products...")
start_time = time.time()

# THE OPTIMIZED PART - this is the 1 step change
pairs = []
n = len(products)
for i in range(n):
    for j in range(i + 1, n): 
        price_diff = abs(products[i]["price"] - products[j]["price"])
        pairs.append(price_diff)

end_time = time.time()
print(f"Done! Found {len(pairs)} pairs")
print(f"Time taken: {end_time - start_time:.4f} seconds")
