import sys

if __name__ == "__main__":
    layer = sys.argv[1]

    if layer == "silver":
        from silver.run_silver import run
        run()

    elif layer == "gold":
        from gold.run_gold import run
        run()

    else:
        raise ValueError("Invalid layer")
