radius = float(input("Enter radius of circular part : "))
length = float(input("Enter length of rectangle : "))
breadth = float(input("Enter breadth of rectangle : "))
cost_per_meter = float(input("Enter cost of barbed wire per meter : "))
rounds = int(input("Enter number of times fencing is done: "))

pi = 3.14

if radius > 0:
    if length > 0:
        if breadth > 0:
            if cost_per_meter > 0:
                if rounds > 0:
                    # Perimeter of half circle = πr + 2r
                    half_circle_perimeter = pi * radius + 2 * radius

                    # Rectangle perimeter excluding one length (shared side)
                    rect_perimeter = length + 2 * breadth

                    # Total boundary for one round
                    total_boundary = half_circle_perimeter + rect_perimeter

                    # Total fencing for 5 rounds
                    total_length = total_boundary * rounds

                    # Total cost
                    total_cost = total_length * cost_per_meter

                    print("Total cost of fencing = Rs.", round(total_cost, 2))
                else:
                    print("Rounds must be greater than zero.")
            else:
                print("Cost per meter must be positive.")
        else:
            print("Breadth must be positive.")
    else:
        print("Length must be positive.")
else:
    print("Radius must be positive.")