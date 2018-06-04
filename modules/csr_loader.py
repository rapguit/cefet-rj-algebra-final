from modules.csr_data import CSRData

def load(file_path):
    data = CSRData()
    n = 0
    m = 0

    with open(file_path) as f:
        k = 0
        row = 0
        prev_row = -1
        firstline = True
        for i, line in enumerate(f):
            if line.startswith("%"):
                continue

            ln = line.replace('\n', '').split(' ')

            if not firstline:
                value = float(ln[2]) if __is_number(ln[2]) else float(ln[3])
                row = int(ln[1])

                data.register_value(value)

                if row != prev_row:
                    if len(data.get_ia_values()) == 0:
                        data.register_ia(k)
                    else:
                        ia = data.get_ia_values()
                        alpha = 0 if len(ia) < 2 else ia[-1]
                        data.register_ia(k + alpha + 1)
                    k = 0
                else:
                    k += 1

                data.register_ja(k)
                prev_row = row
            
            if firstline:
                n = ln[0]
                m = ln[1]
                data.register_aa_size(n, m)
                firstline = False

    data.register_ia(data.get_ia_values()[-1] + data.get_ja_values()[-1] + 1)

    print("[CSR]: Matriz load")
    print(data.get_values())
    print(data.get_ia_values())
    print(data.get_ja_values())

    return data

def __is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False