# Επίλυση προβλήματος μέγιστης κοινής υποακολουθίας DNA με δύο αλγορίθμους

***

### Η επίλυση του προβλήματος της μέγιστης κοινής υποακολουθίας έχει πολλές εφαρμογές. Στo συγκεκριμένo project πραγματοποιούμε την επίλυση του προβλήματος της μέγιστης κοινής υποακολουθίας DNA. Συγκεκριμένα η επίλυση γίνεται με δύο διαφορετικούς αλγορίθμους:
* Τον αλγόριθμο brute force
* Τον αλγόριθμο Longest Common Subsequence

***

### Οι ακολουθίες DNA αναπαρίστανται με συμβολοσειρές που σχηματίζονται από 4 χαρακτήρες (A,G,C,T) που αναπαριστούν τα νουκλεοτίδια αδενίνη, γουανίνη, κυτοσίνη και θυμίνη.

***

# Λύση
### Στο πρόβλημα της μέγιστης κοινής υποακολουθίας του DNA έχουμε δύο συμβολοσειρές DNA με μήκος m η μία και n η άλλη και πρέπει να βρούμε την μέγιστη κοινή υποακολουθία αυτών των δύο. H επίλυση του προβλήματος επιτυγχάνεται με τον απλοϊκό αλγόριθμο ωμής δύναμης (brute force) και τον αλγόριθμο μέγιστης κοινής υποακολουθίας. Ο πρώτος αλγόριθμος δημιουργεί όλες τις υποακολουθίες της πρώτης ακολουθίας (2m σε πλήθος υποακολουθίες) και ελέγχει ποια είναι η μεγαλύτερη κοινή ακολουθία με τη δεύτερη. Ο δεύτερος είναι αλγόριθμος δυναμικού προγραμματισμού.

### Ο αλγόριθμος LCS υλοποιείτε με τον εξής τρόπο:
* Αρχικά δεχόμαστε τις ακολουθίες και βρίσκουμε το μήκος τους (m,n)
* Έπειτα δημιουργούμε έναν πίνακα διαστάσεων n+1*m+1 όπου την πρώτη σειρά και την πρώτη στήλη γεμίζουν με μηδενικά.
* Συμπληρώνουμε κάθε κελί του πίνακα χρησιμοποιώντας την παρακάτω λογική.
* Εάν ο χαρακτήρας που αντιστοιχεί στην τρέχουσα σειρά και την τρέχουσα στήλη ταιριάζουν, τότε συμπληρώνουμε το τρέχον κελί προσθέτοντας ένα στο διαγώνιο στοιχείο.
* Διαφορετικά, πάρτε τη μέγιστη τιμή από την προηγούμενη στήλη και το στοιχείο της προηγούμενης γραμμής για τη συμπλήρωση του τρέχοντος κελιού. Τοποθετήστε ένα βέλος στο κελί με τη μέγιστη τιμή. Αν είναι ίσα, υποδείξτε κάποιο από αυτά.
* Η τιμή στην τελευταία σειρά και στην τελευταία στήλη είναι το μήκος της μεγαλύτερης κοινής υποακολουθίας.
* Για να βρούμε και το ποια είναι αυτή η κοινή υποακολουθία ξεκινάμε από το τελευταίο στοιχείο και πηγαίνουμε προς τα πίσω, μέχρι να συναντήσουμε την πρώτη θέση που παρουσιάζεται ο προηγούμενος αριθμός
### Ο αλγόριθμος αυτός τρέχει πολύ γρηγορότερα από ότι ο αλγόριθμος ωμής δύναμης.