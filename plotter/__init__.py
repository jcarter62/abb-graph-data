from appsettings import DbClient
from arrow import Arrow
import math


class Plot:

    def __init__(self, site: str = '', days: float = 1.0) -> None:
        self.dbc = DbClient()
        self.dbdata = self.dbc.data
        self.graph = self.dbc.graph
        self.site = site
        self.data = []
        self.days = days
        self.set_name(site=site)
        return

    from .misc import data_obj, determine_max_min, start_timestamp
    from .save_graph_data import save_graph_data

    def set_name(self, site: str = ''):
        self.site = site.lower()

        set1 = self.dbdata.find({'site': site, 't0': {'$gt': self.start_timestamp()}})
        qtrhrs = set1.distinct('qtrhr')

        result = []
        for qh in sorted(qtrhrs):
            #
            qset = self.dbdata.find({'site': site, 'qtrhr': qh})
            detail = []
            for row in qset:
                reading = self.data_obj(row)
                detail.append(reading)

            minmax = self.determine_max_min(detail)

            qtrhour = {
                'ts': Arrow.fromtimestamp(timestamp=qh).for_json(),
                'dt': Arrow.fromtimestamp(timestamp=qh),
                'min': minmax['min'],
                'max': minmax['max'],
                'avg': minmax['avg'],
            }
            result.append(qtrhour)

        #
        # Prepare for plot
        #
        dev_x = []
        dev_y = []
        labels = []
        for r in result:
            time = r['dt'].strftime('%m/%d %H:%M')
            dev_x.append(time)
            labels.append(time)
            dev_y.append(r['avg'])

        n = labels.__len__()
        i = n-1
        div_factor = math.floor(n / 10)
        while i > 0:
            if i % div_factor != 0:
                labels[i] = ''
            i = i - 1

        result = {
            'site': self.site,
            'x': dev_x,
            'y': dev_y,
            'labels': labels
        }
        self.data = result


