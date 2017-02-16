from datetime import datetime, date, time, timedelta

def alt_saturday(date_row):
	if date_row.weekday() in [5]:
		str_date_row = date_row.isoformat()
		str_week_no = datetime.strftime(datetime.strptime(str_date_row,'%Y-%m-%d'),"%U")
		week_no = int(str_week_no)
		if date_row.year in (2017,2018,2023,2024,2034,2035,2040,2041):
			week_no = week_no + 1
		if week_no % 2 == 1:
			print str_date_row + " is a Holiday" # holiday
			return
		print  str_date_row +" is a Working day"
		return
	else:
		print "This is not a saturday"
		return

if __name__ == "__main__":
	date_str = raw_input("Please enter a year, month, date (e.g. 2014, 8, 27) == ").split(",")
	date_row = date(int(date_str[0]), int(date_str[1]), int(date_str[2]))
	alt_saturday(date_row)
