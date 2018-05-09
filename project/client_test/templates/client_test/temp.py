import os


def sort_large_file(file_path):
    try:
        if os.path.exists(getFile):
            with open(getFile, 'r') as fp:
                #print(fp.readline())
                for lines in fp.readlines():
                    #print(lines)
                    listdata.append(int(lines))

            print(listdata)
            listdata.sort()
            listdata.reverse()
            print(listdata)
            return True


    except Exception:
        raise


if __name__ == "__main__":
    getFile = input("Enter file path : ")
    new_name = input("Enter file name to save sorted data : ")
    listdata = []
    boold = sort_large_file(getFile)
    print(boold)

    if boold:
        try:
            if new_name:
                new_file = open(new_name, 'w+')
                for item in iter(listdata):
                    print(item)
                    new_file.write("%s \n" % str(item))

                new_file.close()

        except Exception:
            raise
