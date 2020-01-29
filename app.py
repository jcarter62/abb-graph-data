from plotter import Plot
from sites import Sites
import arrow


def timestr():
    result = arrow.now().format('YY-MM-DD HH:mm:ss')
    return result


sites = Sites().sites

print('%s - Starting' % timestr())
for site in sites:
    try:
        print('%s - %s' % (timestr(), site), end='')
        plot = Plot(site=site)
        if plot.data is not None:
            plot.save_graph_data()
    except Exception as e:
        print('%s - Exception for site: %s, %s' % (timestr(), site, str(e)))

    print(' - completed')

print('%s - Completed' % timestr())
