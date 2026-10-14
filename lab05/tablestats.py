def read_rows(lines):
    rows = []
    first = True

    for line in lines:
        parts = line.strip().split(',')

        if first:
            first = False
            continue

        if len(parts) != 3:
            continue
        try:

            row = {
            'дата': parts[0].strip(),
            'тип': parts[1].strip(),
            'минуты': float(parts[2])
            }
            rows.append(row)
        except ValueError:
            continue

    return rows


def count_types(rows):
    res = {}

    for row in rows:
        kind = row['тип']
        res[kind] = res.get(kind,0) + 1
    return res

def total_minutes(rows,kind):
    total = 0

    for row in rows:
        if row['тип'] == kind:
            total += row['минуты']
    return round(total,1)

def to_csv(counts):
    resualt = 'тип,количество'

    for kind in sorted(counts):
        resualt += '?\n' + kind + ',' + str(counts[kind])
    return resualt
