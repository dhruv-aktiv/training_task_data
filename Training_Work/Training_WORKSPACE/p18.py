subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]


#for subjects_i in range(len(subjects)):
#    for verbs_i in range(len(verbs)):
#        for objects_i in range(len(objects)):
#            print("{} {} {}".format(subjects[subjects_i], verbs[
#                  verbs_i], objects[objects_i]))
print([ "{} {} {}".format(sub,verb,obj) for sub in subjects for verb in verbs for obj in objects])
