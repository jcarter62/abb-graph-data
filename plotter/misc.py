from arrow import Arrow

def data_obj(self, row) -> object:
    return {
        'state': row['state'],
        'local': row['local'],
        't0': row['t0'],
        'tflow': row['tflow']
    }


def determine_max_min(self, rows) -> object:
    dmax = -999
    dmin = 999
    davg = 0
    total_flow = 0
    n = 0
    for r in rows:
        rflow = r['tflow']
        if rflow > dmax:
            dmax = rflow
        if rflow < dmin:
            dmin = rflow
        n = n + 1
        total_flow = total_flow + rflow
    if n > 0:
        davg = total_flow / n
    return {
        'max': round(dmax, 2),
        'min': round(dmin, 2),
        'avg': round(davg, 2),
        'n': n
    }


def start_timestamp(self):
    days = self.days
    hours = -1 * (24 * days)
    return Arrow.utcnow().shift(hours=hours).timestamp
