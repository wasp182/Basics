from prescription_data_remove_method import adverse_interactions

trial_patients= {'Charley', 'Eddie', 'Georgia', 'Frank'}

# enumerate list of drugs with adverse reactions
med_to_watch=set()
for drugs in adverse_interactions:
    print(drugs)
    # med_to_watch = med_to_watch.union(drugs)
    # use update instead
    med_to_watch.update(drugs)
    # alternate syntax
    # med_to_watch |= drugs

print(sorted(med_to_watch))

# below also does the same action as above, * upcks the list of adverse interaction
# update method will iterate over any upacking hence advantage of using method
# over operations
med_to_watch.update(*adverse_interactions)
print(*med_to_watch , sep='\n')