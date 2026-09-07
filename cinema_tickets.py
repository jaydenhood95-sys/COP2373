# Cinema Ticket Pre-Sale Program
# COP 2373


def get_tickets(tickets_left):
    """Ask the user how many tickets they want to buy."""

    tickets = int(input("How many movie tickets do you need? "))

    # Check that the buyer's request is allowed.
    if tickets >= 1 and tickets <= 4 and tickets <= tickets_left:
        return tickets
    else:
        print("You can only buy 1 to 4 tickets.")
        return 0


def show_remaining(tickets_left):
    """Display the number of tickets that are still available."""

    print("Tickets remaining:", tickets_left)


def main():
    """Run the cinema ticket pre-sale program."""

    # Start with 20 tickets and no buyers.
    tickets_left = 10
    total_buyers = 0

    print("Welcome to the Cinema Ticket Pre-Sale!")
    print("There are 20 tickets available.")
    print("Each buyer can purchase up to 4 tickets.")
    print()

    # Continue selling tickets until all tickets are sold.
    while tickets_left > 0:
        tickets = get_tickets(tickets_left)

        # Only update the totals when the purchase is valid.
        if tickets > 0:
            tickets_left = tickets_left - tickets
            total_buyers = total_buyers + 1

            # Display the number of tickets left.
            show_remaining(tickets_left)
            print()

    # Display the final results.
    print("All tickets have been sold!")
    print("Total number of buyers:", total_buyers)


# Start the program.
main()

