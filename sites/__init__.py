from appsettings import DbClient


class Sites:

    def __init__(self) -> None:
        dbc = DbClient()
        mrr = dbc.mrr
        self.sites = []

        records = mrr.find({})
        if records.count() > 0:
            for record in records:
                this_site = record['site']
                if this_site is not None:
                    self.sites.append(this_site)

        dbc.close()
        return
