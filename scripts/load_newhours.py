# Tried to Import CSV and not well at it.

# from nwc.models import Hours
# import csv
#
# def run():
#     with open('nwchours.csv') as file:
#         reader = csv.reader(file)
#         next(reader)
#
#         Hours.objects.all().delete()
#
#         for row in reader:
#             print(row)
#
#         hour = Hours(name=row[0],
#                      date_charity=row[1],
#                      hours_work=row[2],
#                      type_work=row[3],
#                      service_work=row[4],
#                      describe=row[5])
#         hour.save()
#
