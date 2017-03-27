import fire
import configparser
import subprocess
import os


class DevAssistant(object):

    def runAndPrintCommand(self, command):
        action = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = action.communicate()[0]
        print output

    def runCommandAndReturnOutput(self,command):
        action = subprocess.Popen(command, stdout=subprocess.PIPE)
        return action.communicate()[0]


    def test(self,file):
        dir = ''
        fileNameWithoutExtension = ''
        if file == 'cas':
            dir = "/apps/code/bidsync/bidsync-cas"
        elif file == 'dao':
            dir = "/apps/code/bidsync/bidsync-dao"
        elif file == 'notification':
            dir = "/apps/code/bidsync/notification"
        elif file == 'business':
            dir = "/apps/code/bidsync/business"
        else:
            if file.find(".java") == -1:
                pattern = str(file) + ".java"
            else:
                pattern = file

            path = str(self.runCommandAndReturnOutput(['find', '/apps/code/bidsync', '-name', pattern])).strip()

            dashPositions = [pos for pos, char in enumerate(path) if char == "/"]

            dir = path[0:dashPositions[4] + 1]

            fileNameWithoutExtension = os.path.splitext(os.path.basename(file))[0]

        os.chdir(dir)

        if fileNameWithoutExtension != '':
            if fileNameWithoutExtension.endswith("NG"):
                prefix = path[path.find("com"):dashPositions[len(dashPositions) - 1]].replace("/", ".")
                self.runAndPrintCommand(['ant', 'test', '-Dtestclass=' + prefix + "." + fileNameWithoutExtension])
            else:
                self.runAndPrintCommand(['ant', 'test', '-Dtestclass=' + fileNameWithoutExtension])
        else:
            self.runAndPrintCommand(['ant', 'test'])

        print "Opening the test results : "

        self.runAndPrintCommand(['open', 'target/test/reports/index.html'])



if __name__ == '__main__':
    fire.Fire(DevAssistant)