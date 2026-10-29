import matplotlib.pyplot as plt

# f = -3*x1 - 2*x2
def f(x1, x2):
    return -3 * x1 - 2 * x2

# vertices of the feasible region (found from the intersections of the lines)
vertices = [(0, 0), (4, 0), (3, 2), (1, 3), (0, 3)]

# value of f at each vertex
for x1, x2 in vertices:
    print("f", (x1, x2), "=", f(x1, x2))

values = [f(x1, x2) for x1, x2 in vertices]
print("min f =", min(values), "at", vertices[values.index(min(values))])
print("max f =", max(values), "at", vertices[values.index(max(values))])

# plot the constraint lines
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
line1 = [(7 - i) / 2 for i in x]   # x1 + 2*x2 = 7
line2 = [8 - 2 * i for i in x]     # 2*x1 + x2 = 8
line3 = [3 for i in x]             # x2 = 3
line_min = [(13 - 3 * i) / 2 for i in x]  # f = -13

plt.plot(x, line1, label="x1 + 2x2 = 7")
plt.plot(x, line2, label="2x1 + x2 = 8")
plt.plot(x, line3, label="x2 = 3")
plt.plot(x, line_min, "r--", label="f = -13")

# feasible region
xs = [v[0] for v in vertices]
ys = [v[1] for v in vertices]
plt.fill(xs, ys, color="gray", alpha=0.3, label="feasible region")

# optimal point
plt.plot(3, 2, "ko")
plt.text(3.1, 2.1, "(3, 2)")

plt.xlim(0, 8)
plt.ylim(0, 8)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Graphical method")
plt.grid(True)
plt.legend()
plt.savefig("lp_graph.png", dpi=200)
plt.show()
