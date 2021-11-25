import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    def find_files_helper(suffix, path, paths = []):

        items = os.listdir(path)
        for item in items:
            if os.path.isfile(path + '/' + item):
                if item.endswith(suffix):
                    paths.append(path + '/' + item)
            else:
                if os.path.isdir(path + '/' + item):
                    find_files_helper(suffix, path + '/' + item)
                    
        return paths
    return find_files_helper(suffix, path)


# four test cases
out1 = find_files(".c", "testdir")
print(out1)
out2 = find_files(".h", "testdir")
print(out2)
out3 = find_files("", "testdir")
print(out3)
out4 = find_files(".py", "testdir")
print(out4)

