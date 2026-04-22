import random
import time
import csv

# Number of bits in the passcode
BITS = 32              

# Size of the population
POP_SIZE = 150         

# Probability of mutation
MUTATION_RATE = 0.02   

# Maximum number of generations
MAX_GENERATIONS = 2000  


# Generate a random target passcode
def generate_target():
    return [random.randint(0, 1) for _ in range(BITS)]

# Create a random individual (chromosome)
def create_individual():
    return [random.randint(0, 1) for _ in range(BITS)]

# Create the initial population
def create_population(size):
    return [create_individual() for _ in range(size)]

# Fitness function: count matching bits
def fitness(individual, target):
    return sum(1 for i in range(BITS) if individual[i] == target[i])

# Select the two best individuals as parents
def select_parents(population, target):
    sorted_pop = sorted(population, key=lambda ind: fitness(ind, target), reverse=True)
    return sorted_pop[0], sorted_pop[1]

# Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, BITS - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutate bits with a given probability
def mutate(individual, rate):
    for i in range(BITS):
        if random.random() < rate:
            individual[i] ^= 1  

# Convert bit list to string
def bits_to_string(bits):
    return "".join(str(b) for b in bits)

# Run the Genetic Algorithm
def run_ga(target, mutation_rate=MUTATION_RATE, csv_filename="convergence.csv", verbose=True):
    if verbose:
        print("Target passcode (bits):")
        print(bits_to_string(target))

    population = create_population(POP_SIZE)
    best_fitness_history = []

    start_time = time.time()
    solution_found = False
    generation_found = None

    # Evolution loop
    for gen in range(1, MAX_GENERATIONS + 1):
        fitness_values = [fitness(ind, target) for ind in population]
        best_fit = max(fitness_values)
        best_fitness_history.append(best_fit)

        # Print progress every 100 generations (only if verbose)
        if verbose and (gen % 100 == 0 or best_fit == BITS):
            print(f"Generation {gen}, best fitness = {best_fit}/{BITS}")

        # Stop if solution is found
        if best_fit == BITS:
            solution_found = True
            generation_found = gen
            break

        # Select parents
        parent1, parent2 = select_parents(population, target)

        # Elitism: keep best parents
        new_population = [parent1, parent2]

        # Create new population
        while len(new_population) < POP_SIZE:
            p1, p2 = random.choice(population), random.choice(population)
            child1, child2 = crossover(p1, p2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)

            new_population.append(child1)
            if len(new_population) < POP_SIZE:
                new_population.append(child2)

        population = new_population

    elapsed_seconds = time.time() - start_time

    # Save convergence data to CSV
    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["generation", "best_fitness"])
        for i, score in enumerate(best_fitness_history, start=1):
            writer.writerow([i, score])

    # Print final results (only if verbose)
    if verbose:
        print("\nRESULTS : ")
        if solution_found:
            print("Passcode found!")
            print(f"Generation found: {generation_found}")
        else:
            print("Passcode NOT found within max generations.")

        print(f"Time taken: {elapsed_seconds:.2f} seconds")
        print("Best fitness in last generation:", best_fitness_history[-1])
        print(f"Convergence data saved to {csv_filename}")

    return {
        "target": target,
        "solution_found": solution_found,
        "generation_found": generation_found,
        "time": elapsed_seconds,
        "history": best_fitness_history
    }
