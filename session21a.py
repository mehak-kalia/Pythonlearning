import threading
import time

class Movieticket:
    def __init__(self, moviename, seatno, row ):
        self.moviename = moviename
        self.seatno = seatno
        self.row = row
        self.isbooked = False

    def showmovieticket(self):
        print("movieticket details are {} | {} | {}".format(self.moviename, self.seatno, self.row))

class Booktickettask(threading.Thread):

    def selectticket(self, ticket, email):
        self.ticket = ticket
        self.email = email

    def run(self):
        if self.ticket.isbooked == False:
            print("Ticket Booking Started for {}".format(self.email))
            print("Movie Ticket Booked for {}".format(self.email))

            print("Movie Ticket Payment Transaction Started...")
            for i in range(0, 10):
                time.sleep(0.5)  # a time delay added for processing payments
                print("Processing Payments.. {} {}".format(self.email, i))

            self.ticket.isbooked = True
            print("Email Sent to {}".format(self.email))
            self.ticket.showmovieticket()
            print("Ticket Booking Finished for {}".format(self.email))
        else:
            print("Sorry {} ticket isnt available".format(self.email))

def main():

    print("Ticket Booking App Started")

    m1 = Movieticket("Avengers", 1, "A")
    m2 = Movieticket("Avengers", 2, "A")
    m3 = Movieticket("Avengers", 3, "A")
    m4 = Movieticket("Avengers", 4, "A")
    m5 = Movieticket("Avengers", 5, "A")

    rowA = [m1, m2, m3, m4, m5]

    task1 = Booktickettask()
    task2 = Booktickettask()

    # Both the users will like to book the same movie ticket :(
    task1.selectticket(rowA[2], "john@example.com")
    task2.selectticket(rowA[2], "fionna@example.com")

    task1.start()
    task2.start()


    print("Ticket Booking App Finished")

if __name__ == '__main__':
    main()
