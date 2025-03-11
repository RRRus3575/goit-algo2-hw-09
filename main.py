import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    x = [random.uniform(*b) for b in bounds]
    current_value = func(x)

    for _ in range(iterations):      
        neighbors = [
            [min(max(x[0] + epsilon, bounds[0][0]), bounds[0][1]), x[1]],  # x1 + epsilon
            [min(max(x[0] - epsilon, bounds[0][0]), bounds[0][1]), x[1]],  # x1 - epsilon
            [x[0], min(max(x[1] + epsilon, bounds[1][0]), bounds[1][1])],  # x2 + epsilon
            [x[0], min(max(x[1] - epsilon, bounds[1][0]), bounds[1][1])]   # x2 - epsilon
        ]

        best_neighbor = min(neighbors, key=func)
        new_value = func(best_neighbor)

        if abs(new_value - current_value) < epsilon: 
            break

        if func(best_neighbor) < current_value:
            x = best_neighbor 
            current_value = new_value
    
    return x, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    x = [random.uniform(*b) for b in bounds]
    current_value = func(x)

    for _ in range(iterations):
        step_size = random.uniform(0, epsilon)
        neighbors = [
            [min(max(x[0] + random.uniform(-step_size, step_size), bounds[0][0]), bounds[0][1]), x[1]],  # x1 + step
            [min(max(x[0] - random.uniform(-step_size, step_size), bounds[0][0]), bounds[0][1]), x[1]],  # x1 - step
            [x[0], min(max(x[1] + random.uniform(-step_size, step_size), bounds[1][0]), bounds[1][1])],  # x2 + step
            [x[0], min(max(x[1] - random.uniform(-step_size, step_size), bounds[1][0]), bounds[1][1])]   # x2 - step
        ]

        best_neighbor = min(neighbors, key=func)
        new_value = func(best_neighbor)

        if abs(new_value - current_value) < epsilon: 
            break

        if func(best_neighbor) < current_value:
            x = best_neighbor 
            current_value = new_value
    
    return x, current_value




# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    x = [random.uniform(*b) for b in bounds]
    current_value = func(x)

    for _ in range(iterations):
        step_size = random.uniform(0, epsilon)

        neighbors = [
            [min(max(x[0] + random.uniform(-step_size, step_size), bounds[0][0]), bounds[0][1]), x[1]],  # x1 + step
            [min(max(x[0] - random.uniform(-step_size, step_size), bounds[0][0]), bounds[0][1]), x[1]],  # x1 - step
            [x[0], min(max(x[1] + random.uniform(-step_size, step_size), bounds[1][0]), bounds[1][1])],  # x2 + step
            [x[0], min(max(x[1] - random.uniform(-step_size, step_size), bounds[1][0]), bounds[1][1])]   # x2 - step
        ]

        new_x = random.choice(neighbors) 
        result = func(new_x)
        delta = result - current_value

        if delta < 0 or random.random() < math.exp(-delta / temp):
            x = new_x
            current_value = result

        temp *= cooling_rate

        if temp < epsilon:  
            break


    return x, current_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]
    
    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
