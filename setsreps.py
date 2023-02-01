# vajab lisatööd
def mitu(lihased, eesmärk):
    per_grupp = ""
    if eesmärk == "jõud":
        per_grupp = "4-5 sets, 2-6 reps"
    elif eesmärk == "lihasmass":
        per_grupp = "3-4 sets, 6-10 reps"
    elif eesmärk == "vastupidavus":
        per_grupp = "2-3 sets, 10-20 reps"
    return per_grupp
