def os_path(disk, *args, sep='\\', **kwargs):
    args = (disk,) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]

    path = sep.join(args)
    return path


p = os_path('D:', ' Games', ' Movavi Video Suite 22 ', ' qtaudio_windows.dll', trim=True)

if __name__ == '__main__':
    print(p)
