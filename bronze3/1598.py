start, dest = map(int,input().split(' '))

def get_xy(point):
    x = (point//4)-1 if point%4==0 else point//4
    y = 4 if point%4 == 0 else point%4
    return x,y
x_s, y_s = get_xy(start)
x_d, y_d = get_xy(dest)
print(abs(x_s - x_d)+ abs(y_s - y_d))