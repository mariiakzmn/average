from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import numpy as np


def run_averages(file_input='data_sample.csv', file_output='result_average.csv'):
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')

    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    averages = planes.mean(axis=1)[np.newaxis, :]

    # write it out on my file
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')


if __name__ == "__main__":
    parser = ArgumentParser(description="Calculates the average for each column in data_sample.",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('file_input', nargs='?', default="data_sample.csv",
                        help="Input CSV file with the numbers.")
    parser.add_argument('--file_output', '-o', default="result_average.csv",
                        help="Name of the output CSV file.")
    arguments = parser.parse_args()

    run_averages(arguments.file_input, arguments.file_output)
    
