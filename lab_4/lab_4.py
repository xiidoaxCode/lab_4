#Mikhailiv Ivan lab_4

import os

def count_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return len(lines)

def count_empty_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        empty_lines = 0
        for line in lines:
            if line.strip() == '':
                empty_lines += 1
        return empty_lines

def count_z_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        z_lines = 0
        for line in lines:
            if 'z' in line:
                z_lines += 1
        return z_lines

def count_z_letters(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        z_count = 0
        for line in lines:
            z_count += line.count('z')
        return z_count

def count_and_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        and_lines = 0
        for line in lines:
            if 'and' in line:
                and_lines += 1
        return and_lines

def print_statistics(filename):
    print('File:', filename)
    print(' total lines:', count_lines(filename))
    print(' empty lines:', count_empty_lines(filename))
    print(' lines with "z":', count_z_lines(filename))
    print(' "z" count":', count_z_letters(filename))
    print(' lines with "and":', count_and_lines(filename))

if __name__ == '__main__':
    while True:
        filename = input('Enter file path: ')
        print_statistics(filename)
        choice = input('Do you want to analyze another file? (y/n): ')
        if choice.lower() == 'n':
            break


