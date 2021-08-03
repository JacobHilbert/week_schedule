# make package aviable without install
import os
import sys
double_backflip = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,double_backflip)

import doctest
import week_schedule.schedule

doctest.testmod(week_schedule.schedule,verbose=True)

print("\nTrying schedule_figure function")
week_schedule.schedule.schedule_figure("test.json").savefig("test.png")
print("ok")
