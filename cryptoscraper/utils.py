def get_tag_percentage_value(tag):
    percentage_delta = round(float(tag.text.strip("%")),2)

    if "down" in tag.span.get("class")[0]:
        percentage_delta = percentage_delta * -1

    return percentage_delta

def sort_by_field(table,field, reverse=True):
    def _select_field(row):
        return row[field]

    return sorted(table, key=_select_field, reverse=reverse)