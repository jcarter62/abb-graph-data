
def save_graph_data(self):
    local_record = self.data
    key = self.site
    local_record['_id'] = key
    try:
        records = self.graph.find({"_id": key})
        this_record = None
        if records.count() > 0:
            this_record = records[0]
        if this_record is None:
            self.graph.insert_one(local_record)
        else:
            self.graph.find_one_and_replace({"_id": key}, local_record)

    except Exception as e:
        s = 'Exception occurred. ' + e.__str__()
        print(s)
