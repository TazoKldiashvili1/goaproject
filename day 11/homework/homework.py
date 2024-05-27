#მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე
#დაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს 
#  რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)


dedis_wlovaneba= int(input("enter mothers age")) 
mamis_wlovaneba= int(input("enter fathers age"))

if dedis_wlovaneba>mamis_wlovaneba:
    print("deda uprosia mamaze") 

elif mamis_wlovaneba>dedis_wlovaneba:
    print("mama uprosia dedaze")

else: 
   print("mama da deda tolebi arian")