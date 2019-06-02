from d_src import DiscreteSource

in_file  = open("source_description.json", "r")
# out_file = open("out_file.json", "w")         для тестирования
# output   = open("out.txt", "w")
sequence_size = 0


source = DiscreteSource(in_file)
# source.print_to_file(out_file)

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
    print("Введите размер выборки: ", end = ' ')
    sequence_size = int(input())
    # source.generate(sequence_size, output)
    source.generate(sequence_size)
else:
    a = []
