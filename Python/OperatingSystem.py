# import glob
# import time

# def copy_from(source):
#     time.sleep(2)
#     target = "copied_csv/{}".format(source.split("/")[-1])
#     print("copy ({})".format(source))
#     with open(source, "r") as rf:
#         with open(target, "w") as wf:
#             wf.write(rf.read())

# def normal_copy(source_path):
#     for source in glob.glob(source_path):
#         copy_from(source)

# if __name__ == "__main__":
#     source_path = "source_csv/*"
#     start = time.time()
#     normal_copy(source_path)
#     print(time.time() - start)









# import threading
# import glob
# import time

# sema = threading.Semaphore(10)

# def copy_from(source):
#     target = "copied_csv/{}".format(source.split("/")[-1])

#     sema.acquire()
#     time.sleep(2)

# # critical section

#     sema.release()

# def parallel_copy(source_path):
#     thread_list = [threading.Thread(target=copy_from, args=(source,)) for source in glob.glob(source_path)]

#     for thread in thread_list:
#         thread.start()

#     for thread in thread_list:
#         thread.join()

# if __name__ == "__main__":
#     source_path = "source_csv/*"
#     start = time.time()

#     parallel_copy(source_path)

#     print(time.time() - start)

from concurrent.futures import thread
import threading
from threading import Thread
import time



sem = threading.Semaphore(4)



def SUM(start, end, listA):
    all = 0
    for i in range(start, end):
        all += i
        print(all)
        time.sleep(0.1)
    listA.append(all)
    return


if __name__ == "__main__":
    start_time = time.perf_counter()
    START=1
    result = list()
    th1 = Thread(target=SUM, args=(START, 200, result))
    th2 = Thread(target=SUM, args=(200, 400, result))
    th3 = Thread(target=SUM, args=(400, 600, result))
    th4 = Thread(target=SUM, args=(600, 800, result))
    th5 = Thread(target=SUM, args=(800, 1001, result))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
finish_time=time.perf_counter()
print(f"여기까지 수행하는 데 {round(finish_time-start_time,2)}초 걸렸습니다.")
print(f"Result: {sum(result)}")