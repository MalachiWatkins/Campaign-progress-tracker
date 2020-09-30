

class log_gen:
    def firsthalf(self):
        log_file = open("log.txt", "w")
        with open("act_logs/act1.txt", "r") as f:
            log_file.write(f.read())
        log_file.close()
        return

    def secondhalf(self):
        return

    def act(self, act):  # acn be run multiple times to simulate progress
        act_txt = "act_logs/act" + act + ".txt"
        print(act_txt)
        log_file = open("log.txt", "a")
        with open(act_txt, "r") as f:
            log_file.write(f.read())
        log_file.close()
        return


def write():
    write_file = log_gen()
    write_ask = str(input("Enter witch act to gen or act1-5: "))
    if write_ask == "act1-5":
        write_file.firsthalf()
    if write_ask == "act":
        act_input = str(input("Enter an act: "))
        write_file.act(act=act_input)


write()
