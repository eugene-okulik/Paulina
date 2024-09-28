from _datetime import datetime


date_string = "Jan 15, 2023 - 12:05:33"
date_format = "%b %d, %Y - %H:%M:%S"
date_format_new = "%d.%M.%Y, %H:%M"

date_object = datetime.strptime(date_string, date_format)
print(date_object.strftime('%B'))

formatted_date_string = date_object.strftime(date_format_new)
print(formatted_date_string)
