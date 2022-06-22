# ------------------------------------------------------------------
# ----------------------Threding in python -------------------------
# ------------------------------------------------------------------

#  ===> What is Thread
#   * thread is a separate flow of execution.    
#   * ever thread has a task.    
#   * if one thread is not depended on another thread then it's called thread other wise not.



# ----------- Main thread  ------------------
# NOTE: Main thread created by PVB (python virtual machine)
import threading
t = threading.current_thread().getName() # get thread name    
print(t)



# -------- Create Thread ------------------------
# you can create thread using diffrent way
    # 1 - without using class
     






    # 2 - using child class of thread class
    # 3 - without using child class of thread class
