from datetime import datetime
import datetime
new_date_of_birth = '1998-02-02'
print(datetime.datetime)
print(type(new_date_of_birth))
dob_datetime = datetime.datetime.strptime(str(new_date_of_birth), "%Y-%m-%d").strftime("%Y-%m-%d")
                   
print(dob_datetime)
print(type(dob_datetime))
