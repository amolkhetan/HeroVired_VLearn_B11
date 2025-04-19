import psutil as psutil

Thresold=80

def CPUHealth_Check ():
    cpu_usage = psutil.cpu_percent(interval=5)
    try:
       if cpu_usage > Thresold and cpu_usage <=Thresold+5:
          print ("Alert! CPU usage exceeds threshold: 80% ", cpu_usage , " Press ctrl+c to stop monitoring")
       elif cpu_usage > Thresold+5 and cpu_usage <=Thresold+10:
          print ("Alert! CPU usage exceeds threshold: 85%", cpu_usage , " Press ctrl+c to stop monitoring")
       elif cpu_usage > Thresold+10 and cpu_usage <=Thresold+15:
          print ("Alert! CPU usage exceeds threshold: 90% ",cpu_usage , " Press ctrl+c to stop monitoring")
       elif cpu_usage > Thresold+15 and cpu_usage <=Thresold+20:
          print ("Alert! CPU usage exceeds threshold: 100% ", cpu_usage , " Press ctrl+c to stop monitoring")
       else:
          print ("CPU Usage within Thresold Limits ", cpu_usage , " Press ctrl+c to stop monitoring")
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}    

if __name__== "__main__":
    print("Monitoring CPU usage...")

    while True:
      CPUHealth_Check()
      


         