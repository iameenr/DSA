//public class PharmacySystem {
//}


/*
Write an application for booking railway ticket reservation system. The application should have four functionalities.

Book
Cancel
Print booked tickets (details with summary)
Print available tickets (details with summary)

Conditions for booking:

Name
Age
Gender
Berth Preference
The tickets should not be allocated for children below age 5.But, their details should be stored. Lower berth should be allocated for persons whose age is above 60 and ladies with children if available.

Conditions for cancelling:
Whenever a ticket is cancelled, a ticket from RAC should be confirmed and a waiting-list ticket should move to RAC.

Conditions for printing booked tickets:
Print all the tickets that are filled along with the passenger details and at the end, print the total number of tickets that are filled.

Conditions for printing available tickets:
Print all the tickets that are unoccupied and at the end, print the total number of tickets that are unoccupied.
*/

import java.util.*;

//enum BERTHPREFERENCE { RAC, SECOND_CLASS, WAITING_LIST };
enum BERTHTYPE { RAC, SECOND_CLASS, WAITING_LIST };
enum GENDER { MALE, FEMALE, OTHERS };

class Passenger {
    private int id;
    private String name;
    private int age;
    private GENDER gender;
    private BERTHTYPE PassengerPreference;

    Passenger(int id, String name, int age, GENDER gender, BERTHTYPE preference) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.PassengerPreference = preference;
    }

    int getId() {
        return this.id;
    }

    String getName() {
        return this.name;
    }

    int getAge() {
        return this.age;
    }

    GENDER getGender() {
        return this.gender;
    }

    BERTHTYPE getPreference() {
        return this.PassengerPreference;
    }
}

class Ticket {
    private int id;
    private Passenger passenger;

    Ticket(int id, Passenger passenger) {
        this.id = id;
        this.passenger = passenger;
    }

    Passenger getPassenger() {
        return this.passenger;
    }

    int getId() {
        return this.id;
    }
}

class Repository {
    private List<Passenger> passengers = new ArrayList<Passenger>();
    private List<Ticket> tickets = new ArrayList<Ticket>();
    private int racTickets;
    private int secondClassTicket;
    private int waitingListTicket;

    Repository(int racTickets, int secondClassTicket, int waitingListTicket) {
        this.racTickets = racTickets;
        this.secondClassTicket = secondClassTicket;
        this.waitingListTicket = waitingListTicket;
    }

    boolean bookTicket(Ticket ticket) {
        Passenger passenger = ticket.getPassenger();
        switch(passenger.getPreference()) {
            case RAC:
                if(racTickets == 0) return false;
                racTickets--;
                break;
            case SECOND_CLASS:
                if(secondClassTicket == 0) return false;
                secondClassTicket--;
                break;
            case WAITING_LIST:
                if(waitingListTicket == 0) return false;
                waitingListTicket--;
            default:
                break;
        }
        if(passenger.getAge() <= 5) return passengers.add(passenger);
        return tickets.add(ticket) && passengers.add(passenger);
    }

    boolean bookTicket(Passenger passenger) {
        if(passenger.getAge() > 5) return false;
        return passengers.add(passenger);
    }

    boolean cancelTicket(Ticket ticket) {
        Passenger passenger = ticket.getPassenger();
        switch(passenger.getPreference()) {
            case RAC:
                racTickets++;
                break;
            case SECOND_CLASS:
                secondClassTicket++;
                break;
            case WAITING_LIST:
                waitingListTicket++;
                break;
            default:
                break;
        }

        return tickets.remove(ticket) && passengers.remove(passenger);
    }

    boolean cancelTicket(Passenger passenger) {
        return passengers.remove(passenger);
    }

    void printBookedTickets() {
        int i = 0;
        for(Ticket ticket:tickets) {
            i++;
            Passenger passenger = ticket.getPassenger();
            System.out.println(ticket.getId() + "\t" + passenger.getId() + "\t" + passenger.getName() + "\t" + passenger.getAge() + "\t" + passenger.getGender() + "\t" + passenger.getPreference());
        }

        System.out.println(i);
    }

    void printAvailableTickets() {
        System.out.println("RAC: " + racTickets + " Second Class Ticket: " + secondClassTicket + " Waiting List: " + waitingListTicket + " Total: " + (racTickets + secondClassTicket + waitingListTicket));
    }
}

public class PharmacySystem {
    public static void main(String[] args) {
        Repository repository = new Repository(63, 20, 10);

        Passenger p1 = new Passenger(1, "Albert", 20, GENDER.MALE, BERTHTYPE.RAC);
        Ticket t1 = new Ticket(1, p1);

        Passenger p2 = new Passenger(2, "John", 30, GENDER.MALE, BERTHTYPE.SECOND_CLASS);
        Ticket t2 = new Ticket(2, p1);

        Passenger p3 = new Passenger(3, "Elisa", 5, GENDER.FEMALE, BERTHTYPE.WAITING_LIST);
        Ticket t3 = new Ticket(3, p3);

        repository.bookTicket(t1);
        repository.bookTicket(t2);
        repository.bookTicket(t3);

        repository.printBookedTickets();
        repository.printAvailableTickets();
    }
}

