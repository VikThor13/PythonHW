import sys
import getopt
import yaml

key = ""
value = ""
data_file = 'storage.yml'
rem = 0


def main():
    global key
    global value
    global rem

    init_component()

    with open(data_file, 'r') as f:
        try:
            storage_map = yaml.load(f)
            # print(yaml.dump(storage_map))
        except:
            print("Ошибка чтения данных")
            sys.exit(1)
    if key != '':
        if value != '':
            if key in storage_map:
                storage_map[key].append(value)
            else:
                storage_map[key] = [value]
            write_file(storage_map)
        elif key in storage_map:
            if not rem:
                for idx, val in enumerate(storage_map[key]):
                    print(f"value {(idx + 1):d} = {val}")
            else:
                del storage_map[key]
                write_file(storage_map)
        else:
            print("Такого ключа не существует")
    else:
        print("Неверный набор параметров")
        usage()


def init_component():
    global key
    global value
    global rem

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hk:v:r", ["help", "key", "val", "rem"])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for par_key, par_value in opts:
        if par_key in ("-k", "--key"):
            key = par_value
        elif par_key in ("-v", "--val"):
            value = par_value
        elif par_key in ("-r", "--rem"):
            rem = 1
        elif par_key in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "Нераспознанный параметр"


def usage():
    print("Использование: " + sys.argv[0] + " --key key_name --val value - для записи значения")
    print(sys.argv[0] + " --key key_name [--rem] - для получения значения по ключу, --rem - для удаления значения")
    print("""Этот скрипт реализует key-value хранилище данных

ПАРАМЕТРЫ:
    -h | --help справочное сообщение.
    -k | --key 	ключ
    -v | --val 	значение соответствующее ключу
    -r | --rem  удаление значения key""")
    sys.exit()


def write_file(dict):
    with open(data_file, 'w') as f:
        f.write(yaml.dump(dict))


if __name__ == "__main__":
    main()
