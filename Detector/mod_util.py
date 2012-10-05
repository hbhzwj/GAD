try:
    import matplotlib.pyplot as plt
except ImportError:
    print 'no matplotlib'
    plt = False

def find_seg(flag):
    """return (start and end point and level) of each segment"""
    n  = len(flag)
    start = [0]
    end = []
    tp = []
    for i in xrange(n-1):
        if flag[i+1] != flag[i]:
            start.append(i+1)
            # end.append(i+1) # to make lines continous
            end.append(i+2)
            tp.append(flag[i])
    end.append(n)
    tp.append(flag[n-1])
    return zip(start, end, tp)

def plot_seg(X, Y, flag, marker=None):
    """plot X and Y, but the points with flag == true to be one color, the result to be another color
    """
    segs = find_seg(flag)
    for a, b, tp in segs:
        if marker[tp] is not None:
            plt.plot(X[a:b], Y[a:b], marker[tp])

def plot_points(X, Y, threshold=None,  pic_show=False,
        pic_name=None, figure_=False, subplot_=111, title_ = None,
        xlabel_ = 'x', ylabel_ = 'y',
        ano_marker=['b-', 'r-'], threshold_marker='g--',
        *args, **kwarg):
    if not plt:
        return -1;
    if not figure_:
        figure_ = plt.figure()
    figure_.add_subplot(subplot_)

    if threshold:
        ano_flag = [ (1 if e > th  else 0) for e, th in zip(Y, threshold)]
        plot_seg(X, Y, ano_flag, ano_marker)
        if threshold_marker is not None:
            plt.plot(X, threshold, threshold_marker)
    else:
        plt.plot(X, Y, ano_marker[0])
    if title_:
        plt.title(title_)

    if pic_name: plt.savefig(pic_name)
    if pic_show: plt.show()

