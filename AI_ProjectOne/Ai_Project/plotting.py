import matplotlib.pyplot as plt

def plot_convergence(history, title, save_path):
    generations = list(range(1, len(history) + 1))

    plt.figure()
    plt.plot(generations, history)
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.grid(True)

    plt.savefig(save_path, dpi=200, bbox_inches="tight")
    plt.close()
