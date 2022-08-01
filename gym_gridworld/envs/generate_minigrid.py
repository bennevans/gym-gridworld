import argparse

def make_grid(size, filename):
    top_bottom = '1 ' * size
    top_bottom = top_bottom[:-1] + '\n'
    middles = '1 '  + '0 ' * (size - 2) + '1\n'

    mid_lines = [middles] * (size - 3)
    start_end_line = '1 3 4 '  + '0 ' * (size - 4) + '1\n'

    grid_lines = [top_bottom, start_end_line] + mid_lines + [top_bottom]

    with open(filename, 'w') as f:
        f.writelines(grid_lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('size', type=int)
    parser.add_argument('output')

    args = parser.parse_args()

    make_grid(args.size, args.output)


