import random as r  # βιβλιοθήκη για την τυχαιότητα
import timeit  # βιβλιοθήκη για την μέτρηση του χρόνου
import matplotlib.pyplot as plt

# Συνάρτηση που δημιουργεί την λίστα των προθεματικών αθροισμάτων
def prefix(a_list):
    prefix_sums = list()  # Αρχικοποίηση λίστας των προθεματικών αθροισμάτων

    for i in range(0, len(a_list)):  # Προσπέλαση λίστας των προθεματικών αθροισμάτων

        if i == 0:  # Αν το i είναι 0
            # Προσθέτουμε το στοιχείο που βρίσκεται σε αυτή την θέση στον πίνακα
            prefix_sums.append(a_list[i])
        else:  # Αλλιώς
            # Προσθέτουμε το προηγούμενο στοιχείο της λίστας των προθεματικών αθροισμάτων μέ το στοιχείο που βρίσκεται στην θέση i του αρχικού μας πίνακα
            prefix_sums.append(a_list[i] + prefix_sums[i - 1])

    return prefix_sums  # Επιστρέφει τη λίστα των προθεματικών αθροισμάτων


# Υλοποίηση του πρώτου αλγορίθμου
def MaxSubSlow(a_list):
    # Αρχικοποίηση της μεταβλητής που θα αποθηκέυει το μεγαλύτερο άθροισμα
    largest_sum = a_list[0]
    start = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκεύει την θέση που ξεκινάει το μέγιστο άθροισμα
    end = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκεύει την θέση που τελειώνει το μέγιστο άθροισμα

    for i in range(0, len(a_list)):

        for j in range(i, len(a_list)):
            # Αρχικοποίηση της μεταβλητής που θα αποθηκέυει το εκάστοτε άθροισμα
            sum = 0

            for x in range(i, j + 1):
                sum += a_list[x]  # Υπολογίζει το εκάστοτε άθροισμα
            # Αν το άθροισμα που υπολόγισε είναι μεγαλύτερο του μέγιστου
            if largest_sum < sum:
                largest_sum = sum  # Το μεγαλύτερο άθροισμα είναι ίσο με το άθροισμα που υπολογίσαμε πριν
                start = i  # Η θέση που ξεκινάει το μέγιστο άθροισμα
                end = j  # Η θέση που τελειώνει το μέγιστο άθροισμα
    # Επιστρέφει μία λίστα με το μέγιστο άθροισμα, την θέση που ξεκινάει και την θέση που τελειώνει
    return largest_sum, start, end


# Υλοποίηση του δεύτερου αλγορίθμου
def MaxSubFaster(a_list):
    # Αρχικοποίηση της μεταβλητής που θα αποθηκέυει το μεγαλύτερο άθροισμα
    largest_sum = a_list[0]
    sum = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκέυει το εκάστοτε άθροισμα
    start = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκεύει την θέση που ξεκινάει το μέγιστο άθροισμα
    end = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκεύει την θέση που τελειώνει το μέγιστο άθροισμα

    for i in range(0, len(a_list)):

        for j in range(i, len(a_list)):

            if i == 0:  # Αν το i είναι ίσο με 0
                # Το άθροισμα ισούται με το στοιχείο του πίνακα στην θέση 0
                sum = a_list[j]
            else:  # Αλλιώς
                # Το άθροισμα ισούται με το το στοιχείο που βρίσκεται στην θέση j μείον το στοιχείο που βρίσκεται στην θέση i-1
                sum = a_list[j] - a_list[i - 1]
            # Αν το άθροισμα είναι μεγαλύτερο από το μέγιστο άθροισμα
            if largest_sum < sum:
                largest_sum = sum  # Το μεγαλύτερο άθροισμα είναι ίσο με το άθροισμα που υπολογίσαμε πριν
                start = i  # Η θέση που ξεκινάει το μέγιστο άθροισμα
                end = j  # Η θέση που τελειώνει το μέγιστο άθροισμα

    # Επιστρέφει μία λίστα με το μέγιστο άθροισμα, την θέση που ξεκινάει και την θέση που τελειώνει
    return largest_sum, start, end


# Υλοποίηση του τρίτου αλγορίθμου
def MaxSubFastest(a_list):
    # Αρχικοποίηση της μεταβλητής που θα αποθηκέυει το μεγαλύτερο άθροισμα
    largest_sum = a_list[0]
    sum = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκέυει το εκάστοτε άθροισμα
    start = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκεύει την θέση που ξεκινάει το μέγιστο άθροισμα
    end = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκεύει την θέση που τελειώνει το μέγιστο άθροισμα
    pointer = 0  # Αρχικοποίηση της μεταβλητής που θα αποθηκεύει την θέση που μηδενίστηκε τελευταία φορά ο πίνακας

    for i in range(0, len(a_list)):
        sum += a_list[i]  # Υπολογίζει το εκάστοτε άθροισμα

        if largest_sum < sum:  # Αν το άθροισμα είναι μεγαλύτερο από το μέγιστο άθροισμα
            largest_sum = sum  # Το μεγαλύτερο άθροισμα είναι ίσο με το άθροισμα που υπολογίσαμε πριν
            start = pointer  # Η θέση που ξεκινάει το μέγιστο άθροισμα
            end = i  # Η θέση που τελειώνει το μέγιστο άθροισμα

        if sum < 0:  # Αν το τωρινό άθροισμα είναι μικρότερο του μηδενός
            sum = 0  # Μηδενίζουμε το sum
            # θέτουμε την επόμενη θέση από αυτή που βρισκόμαστε ώς αρχική για το επομενο άθροισμα
            pointer = i + 1
            # Επιστρέφει μία λίστα με το μέγιστο άθροισμα, την θέση που ξεκινάει και την θέση που τελειώνει
    return largest_sum, start, end


# Υλοποίηση της συνάρτησης δημιουργίας ενός τυχαίου πίνακα
def ArrayGen(num, ran):
    return [r.randint(-ran, ran) for x in range(num)]


def main():
    # Αρχικοποίηση του πίνακα των συναρτήσεων
    functions = [MaxSubSlow, MaxSubFaster, MaxSubFastest]
    # Αρχικοποίηση του πίνακα των τιμών που καθορίζουν το μέγεθος του τυχαίου πίνακα
    num = [10, 100, 1000]  # 5000
    ran = 100  # Εύρος του πίνακα
    timed = dict()

    for f in functions:
        print(f"\nThe fuction that we use is the {f.__name__}\n")

        if f.__name__ == "MaxSubSlow":
            print("The complexity of this function is O(n^3)\n")
        elif f.__name__ == "MaxSubFaster":
            print("The complexity of this function is O(n^2)\n")
        else:
            print("The complexity of this function is O(n)\n")

        for n in num:
            sequence = ArrayGen(n, ran)  # Δημιουργία του τυχαίου πίνακα
            # Δημιουργία του πίνακα των προθεματικών αθροισμάτων
            prefix_sums = prefix(sequence)
            # Καταγραφή της ώρας που ξεκινάει να υλοποιείται ο κώδικας
            start_time = timeit.default_timer()

            if f.__name__ == "MaxSubFaster":
                results = f(prefix_sums)  # Αποτελέσματα του δεύτερου αλγόριθμου
                # Καταγραφή της ώρας που παίρνει ο κώδικας να υλοποιηθεί
                duration = timeit.default_timer() - start_time
            else:
                results = f(sequence)  # Αποτελέσματα του δεύτερου αλγόριθμου
                # Καταγραφή της ώρας που παίρνει ο κώδικας να υλοποιηθεί
                duration = timeit.default_timer() - start_time
            print(
                f"\nThe  results is for number {n} in the range -{ran}, {ran}: {duration} seconds\n"
            )
            print(f"Maximum sum Subarray is: {results[0]}")
            print(f"\nStart Index of window is: {results[1]}")
            print(f"\nEnd Index of window is: {results[2]}")

            timed[(f.__name__, n)] = duration
    time_first_algorithm = list()
    time_second_algorithm = list()
    time_third_algorithm = list()
    for function_name, n_size in timed:
        if function_name == "MaxSubSlow":
            time_first_algorithm.append(timed[function_name, n_size])
        elif function_name == "MaxSubFaster":
            time_second_algorithm.append(timed[function_name, n_size])
        elif function_name == "MaxSubFastest":
            time_third_algorithm.append(timed[function_name, n_size])
    plt.plot(num, time_first_algorithm, label="time_first_algorithm")
    plt.plot(num, time_second_algorithm, label="time_second_algorithm")
    plt.plot(num, time_third_algorithm, label="time_third_algorithm")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
