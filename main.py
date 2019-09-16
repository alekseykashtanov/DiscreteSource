from d_src import DiscreteSource

in_file = open("source_description.json", "r")
output = open("out.txt", "w")
sequence_size = 0


def print_seq(seq):
    for i in seq:
        print(i, end='')


source = DiscreteSource(in_file)

print("Выберите режим:")
print("1 - реализация источника длины N, если N <= 0, то для остановки нажмите клавишу \'q\'/\'й\'")
print("2 - вероятность появления последователности")

usr_input = input()
while usr_input != '1' and usr_input != '2':
    print("Неизвестный режим. Попробуйте еще раз")
    usr_input = input()

if usr_input == '1':
    # print("Введите путь к входному файлу: ")
    # in_file = input()
    # print("Введите путь к выходному файлу: ")
    # out_file = input()
    print("Введите размер выборки: ", end=' ')
    sequence_size = int(input())
    # source.generate(sequence_size, output)
    print_seq(source.generate(sequence_size))
    # output.write(source.generate(sequence_size))
else:
    print("Введите размер выборки: ", end=' ')
    sequence_size = int(input())
    print("Введите последователность для анализа (последний элемент - любой не \'0\' или \'1\')")
    a = input().split(sep=' ')
    print(a)
    sequence = source.generate(sequence_size)
    p = sequence.count('1') / sequence_size
    print("Вероятность: ", p ** a.count('1') * (1 - p) ** a.count('0'))
    print("Сгенерированная последовательность: ")
    print_seq(sequence)
