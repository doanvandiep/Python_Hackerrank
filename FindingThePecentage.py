N = input();

map = {};
for i in range(0,int(N)):
    S = input().split();
    lst = (float(S[1]) + float(S[2]) + float(S[3]))/3;
    map[S[0]] = lst;


print("%0.2f" % map[input()])  # In ra điểm trung bình của sinh viên có tên được nhập
