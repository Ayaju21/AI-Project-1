import random
from genetic_algorithm import run_ga, generate_target
from plotting import plot_convergence

if __name__ == "__main__":
    random.seed(42)
    target = generate_target()

    rates = [0.01, 0.02, 0.05]

    print("Target passcode:", "".join(map(str, target)))
    print("-" * 55)

    for r in rates:
        result = run_ga(
            target=target,
            mutation_rate=r,
            csv_filename=f"convergence_{r}.csv",
            verbose=False 
        )

        status = "FOUND " if result["solution_found"] else "NOT FOUND "
        gen = result["generation_found"] if result["generation_found"] else "-"
        t = f'{result["time"]:.2f}s'

        print(f"mutation={r:<4} | {status:<10} | gen={gen:<4} | time={t:<6} | csv=convergence_{r}.csv")

        plot_convergence(
            result["history"],
            title=f"GA Convergence (mutation={r})",
            save_path=f"convergence_{r}.png"
        )

    print("-" * 55)
