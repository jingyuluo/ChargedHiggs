import os,shutil


Masses = [200, 220, 250, 300, 350, 400, 500, 600, 700,  800, 1000, 1250, 1500, 1750, 2000, 2500, 3000]

for mass in Masses:
    str_mass = str(mass)
    jdfName = "cond_M{0}".format(str_mass)
    jdf = open(jdfName, "w")
    jdf.write("universe = vanilla\n")
    jdf.write("Executable = comb.sh\n")
    jdf.write("Should_Transfer_Files = YES\n")
    jdf.write("WhenToTransferOutput = ON_EXIT\n")
    jdf.write("request_memory = 3072\n")
    jdf.write("Output = combine_M{0}.out\n".format(str_mass))
    jdf.write("Error = combine_M{0}.err\n".format(str_mass))
    jdf.write("Log = combine_M{0}.log\n".format(str_mass))
    jdf.write("Notification = Error\n")
    jdf.write("Arguments = {0}\n".format(str_mass))
    jdf.write("Queue\n")
    jdf.close()
    os.system("condor_submit cond_M{0}".format(str_mass))
