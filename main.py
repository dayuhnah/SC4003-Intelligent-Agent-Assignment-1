def print_utilities(U):
    for r in range(rows):
        row_vals = []
        for c in range(cols):
            if (r, c) in walls:
                row_vals.append('#####')
            else:
                row_vals.append(f'{U[(r, c)]:6.2f}')
        print(" ".join(row_vals))