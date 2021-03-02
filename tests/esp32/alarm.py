import machine
from machine import Timer
import time

def cb(word):
    print(word)

# Create 16 alarms randomly with timing: 1sec - 16sec
# They have to expire starting the one with 1sec expiration up to the one with 16 sec
alarm1 = Timer.Alarm(handler=cb, s=1,  arg="alarm1",  periodic=False)
alarm3 = Timer.Alarm(handler=cb, s=3,  arg="alarm3",  periodic=False)
alarm4 = Timer.Alarm(handler=cb, s=4,  arg="alarm4",  periodic=False)
alarm12 = Timer.Alarm(handler=cb, s=12,arg="alarm12", periodic=False)
alarm5 = Timer.Alarm(handler=cb, s=5,  arg="alarm5",  periodic=False)
alarm6 = Timer.Alarm(handler=cb, s=6,  arg="alarm6",  periodic=False)
alarm7 = Timer.Alarm(handler=cb, s=7,  arg="alarm7",  periodic=False)
alarm8 = Timer.Alarm(handler=cb, s=8,  arg="alarm8",  periodic=False)
alarm16 = Timer.Alarm(handler=cb, s=16,arg="alarm16", periodic=False)
alarm9 = Timer.Alarm(handler=cb, s=9,  arg="alarm9",  periodic=False)
alarm2 = Timer.Alarm(handler=cb, s=2,  arg="alarm2",  periodic=False)
alarm10 = Timer.Alarm(handler=cb, s=10,arg="alarm10", periodic=False)
alarm11 = Timer.Alarm(handler=cb, s=11,arg="alarm11", periodic=False)
alarm13 = Timer.Alarm(handler=cb, s=13,arg="alarm13", periodic=False)
alarm14 = Timer.Alarm(handler=cb, s=14,arg="alarm14", periodic=False)
alarm15 = Timer.Alarm(handler=cb, s=15,arg="alarm15", periodic=False)

# Wait for expiration
time.sleep(16)

# Create 16 alarms again randomly with timing: 1sec - 16sec 
alarm3 = Timer.Alarm(handler=cb, s=3,  arg="alarm3",  periodic=False)
alarm12 = Timer.Alarm(handler=cb, s=12,arg="alarm12", periodic=False)
alarm6 = Timer.Alarm(handler=cb, s=6,  arg="alarm6",  periodic=False)
alarm1 = Timer.Alarm(handler=cb, s=1,  arg="alarm1",  periodic=False)
alarm7 = Timer.Alarm(handler=cb, s=7,  arg="alarm7",  periodic=False)
alarm8 = Timer.Alarm(handler=cb, s=8,  arg="alarm8",  periodic=False)
alarm13 = Timer.Alarm(handler=cb, s=13,arg="alarm13", periodic=False)
alarm5 = Timer.Alarm(handler=cb, s=5,  arg="alarm5",  periodic=False)
alarm16 = Timer.Alarm(handler=cb, s=16,arg="alarm16", periodic=False)
alarm4 = Timer.Alarm(handler=cb, s=4,  arg="alarm4",  periodic=False)
alarm15 = Timer.Alarm(handler=cb, s=15,arg="alarm15", periodic=False)
alarm2 = Timer.Alarm(handler=cb, s=2,  arg="alarm2",  periodic=False)
alarm10 = Timer.Alarm(handler=cb, s=10,arg="alarm10", periodic=False)
alarm9 = Timer.Alarm(handler=cb, s=9,  arg="alarm9",  periodic=False)
alarm11 = Timer.Alarm(handler=cb, s=11,arg="alarm11", periodic=False)
alarm14 = Timer.Alarm(handler=cb, s=14,arg="alarm14", periodic=False)

# Cancel every second alarm, they must not expire
alarm2.cancel()
alarm4.cancel()
alarm6.cancel()
alarm8.cancel()
alarm10.cancel()
alarm12.cancel()
alarm14.cancel()
alarm16.cancel()

# Wait for expiration
time.sleep(16)

# Set and cancel the same alarm 5 times, no expiration must happen
for num in range(0,5):
    alarm1.callback(cb,arg="alarm1")
    alarm1.cancel()
# Expiration must happen because of this set
alarm1.callback(cb,arg="alarm1")

# Wait for expiration
time.sleep(2)

# Activate the previous 16 alarms
alarm1.callback(cb,arg="alarm1")
alarm3.callback(cb,arg="alarm3")
alarm4.callback(cb,arg="alarm4")
alarm12.callback(cb,arg="alarm12")
alarm5.callback(cb,arg="alarm5")
alarm6.callback(cb,arg="alarm6")
alarm7.callback(cb,arg="alarm7")
alarm8.callback(cb,arg="alarm8")
alarm16.callback(cb,arg="alarm16")
alarm9.callback(cb,arg="alarm9")
alarm2.callback(cb,arg="alarm2")
alarm10.callback(cb,arg="alarm10")
alarm11.callback(cb,arg="alarm11")
alarm13.callback(cb,arg="alarm13")
alarm14.callback(cb,arg="alarm14")
alarm15.callback(cb,arg="alarm15")

# Wait 5 sec, which means alarm1-5 should expire, but alarm6-16 not
time.sleep(5)
# Acticate alarm2 which means it has to expire between alarm7 and alarm8
alarm2.callback(cb,arg="alarm2")
# Cancel alarm14
alarm14.cancel()

# Wait for the alarms to expire except alarm14
time.sleep(12)

# Activate the previous 16 alarms
alarm1.callback(cb,arg="alarm1")
alarm3.callback(cb,arg="alarm3")
alarm4.callback(cb,arg="alarm4")
alarm12.callback(cb,arg="alarm12")
alarm5.callback(cb,arg="alarm5")
alarm6.callback(cb,arg="alarm6")
alarm7.callback(cb,arg="alarm7")
alarm8.callback(cb,arg="alarm8")
alarm16.callback(cb,arg="alarm16")
alarm9.callback(cb,arg="alarm9")
alarm2.callback(cb,arg="alarm2")
alarm10.callback(cb,arg="alarm10")
alarm11.callback(cb,arg="alarm11")
alarm13.callback(cb,arg="alarm13")
alarm14.callback(cb,arg="alarm14")
alarm15.callback(cb,arg="alarm15")

# Wait 4 sec, which means alarm1-4 should expire, but alarm5-16 not
time.sleep(4)

# Cancel alarm6
alarm6.cancel()

# Wait 2 sec, which means alarm5 and alarm7 should expire, but alarm6 not
time.sleep(2)

#Add alarm6 back which means alarm6 should expire between alarm12 and alarm13
alarm6.callback(cb,arg="alarm6")

# Wait 12 sec for all alarm to expire
time.sleep(12)

# Check alarm expirations with milisec values
alarm1 = Timer.Alarm(handler=cb, ms=136, arg="alarm1",  periodic=False)
alarm3 = Timer.Alarm(handler=cb, ms=600, arg="alarm3",  periodic=False)
alarm4 = Timer.Alarm(handler=cb, ms=241, arg="alarm4",  periodic=False)
alarm12 = Timer.Alarm(handler=cb, ms=77, arg="alarm12", periodic=False)

#Wait for expiration
time.sleep(1)

# Check alarm expirations with microsec values
alarm1 = Timer.Alarm(handler=cb, us=136, arg="alarm1",  periodic=False)
alarm3 = Timer.Alarm(handler=cb, us=600, arg="alarm3",  periodic=False)
alarm4 = Timer.Alarm(handler=cb, us=241, arg="alarm4",  periodic=False)
alarm12 = Timer.Alarm(handler=cb, us=77, arg="alarm12", periodic=False)

# Wait for expiration
time.sleep(1)

# Put back non-periodic alarm as the first element
alarm1 = Timer.Alarm(handler=cb, ms=455, arg="alarm1",  periodic=False)
alarm3 = Timer.Alarm(handler=cb, s=2, arg="alarm3",  periodic=False)

# Wait 500 ms which means alarm1 has expired but alarm3 not
time.sleep(0.5)

# Add alarm1 again, it should expire before alarm3
alarm1.callback(handler=cb, arg="alarm1")

# Wait for expiration
time.sleep(2)
