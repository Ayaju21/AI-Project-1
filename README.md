# 🧬 Password Cracking Simulation (Genetic Algorithm)

An implementation of a **Genetic Algorithm (GA)** to evolve and "crack" a randomly generated 32-bit passcode. This project was developed as part of the **Artificial Intelligence (COMP338)** course.

## 📌 Project Overview
The objective is to simulate a brute-force alternative using evolutionary heuristics. The program generates a hidden 32-bit binary sequence and employs a GA to evolve a population of candidate bits until a perfect match is found. 

This implementation is built **from scratch** (zero external libraries) to demonstrate deep understanding of:
* Population dynamics
* Selection mechanisms
* Crossover and Mutation operators
* Heuristic optimization

---

## ⚙️ How It Works

### 1. Representation
* **Gene:** A single bit (0 or 1).
* **Chromosome:** A fixed-length string of 32 bits representing a potential passcode.
* **Population:** A set of chromosomes evolving over generations.

### 2. Fitness Function
The fitness is calculated based on the **Hamming Distance** (the number of bits that match the target passcode).
$$Fitness = \sum_{i=1}^{32} (Individual[i] == Target[i])$$
*Goal: Reach a fitness score of 32.*

### 3. Evolutionary Process
* **Selection:** Choosing parents based on their fitness (e.g., Roulette Wheel or Tournament Selection).
* **Crossover:** Combining two parents to produce offspring (Single-point or Multi-point).
* **Mutation:** Randomly flipping bits to maintain genetic diversity and prevent premature convergence.


1. Clone the repo:
   ```bash
   git clone [https://github.com/YourUsername/GA-Password-Cracker.git](https://github.com/YourUsername/GA-Password-Cracker.git)
