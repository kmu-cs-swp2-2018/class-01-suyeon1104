import time
import sys
from PyQt5.QtWidgets import  *
min_purchase = 0
purchase = 0
app = QApplication(sys.argv)
t = time.time()
while(True):
    purchase = int(input())
    if time.time() - t >= 10:
        break
    if purchase <= min_purchase:
        print("입찰하기 위한 금액이 부족합니다.")
    else:
        min_purchase = purchase
        print("입찰 최소 가격:", min_purchase)
        print("남은 경매 시간: %4.2f초" %(10 - (time.time() - t)))
    if time.time() - t >= 10:
        break
print("%d에 낙찰되었습니다!" %min_purchase)