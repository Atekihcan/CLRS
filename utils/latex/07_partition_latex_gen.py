A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]


def partition_trace(A: list[int], p: int, r: int) -> list[str]:
    x = A[r - 1]
    i = p - 1
    states: list[str] = []

    def snapshot(A: list[int], i: int, j: int, p: int, r: int) -> str:
        out: list[str] = []
        out.append(r"\begin{tikzpicture}[")
        out.append(r"  cell/.style={draw, minimum width=\w, minimum height=\w, anchor=center},")
        out.append(r"  shadedA/.style={cell, fill=gray!40}, shadedB/.style={cell, fill=gray!60}]")

        for idx in range(len(A)):
            out.append(rf"\node[text=gray!30] at ({idx}*\w,-7mm) {{{idx + 1}}};")

        for idx, val in enumerate(A):
            pos = idx + 1
            if pos <= i:
                style = "shadedA"
            elif pos < j and val != x:
                style = "shadedB"
            else:
                style = "cell"
            out.append(rf"\node[{style}] at ({idx}*\w,0) {{{val}}};")

        out.append(rf"\draw[line width=2mm] ({(i - 0.5)}*\w,-4.5mm) -- ({(i - 0.5)}*\w,4.5mm);")
        out.append(rf"\draw[line width=2mm] ({(j - 1.5)}*\w,-4.5mm) -- ({(j - 1.5)}*\w,4.5mm);")

        if j <= r:
            # out.append(rf"\draw[line width=2mm] ({(r - 0.5)}*\w,-4.5mm) -- ({(r - 0.5)}*\w,4.5mm);")
            out.append(rf"\draw[line width=2mm] ({(r - 1.5)}*\w,-4.5mm) -- ({(r - 1.5)}*\w,4.5mm);")
        else:
            out.append(rf"\draw[line width=2mm] ({(i + 0.5)}*\w,-4.5mm) -- ({(i + 0.5)}*\w,4.5mm);")

        if i > 0:
            out.append(rf"\node at ({-1}*\w,-5mm) {{}};")
        out.append(rf"\node at ({(i - 1)}*\w,7mm) {{$i$}};")
        out.append(rf"\node at ({(j - 1)}*\w,7mm) {{$j$}};")

        out.append(r"\end{tikzpicture}")
        out.append(r"\vspace{3mm}")
        return "\n".join(out)

    for j in range(p, r):
        states.append(snapshot(A, i, j, p, r))
        # print(f"j = {j}, i = {i}")
        if A[j - 1] < x:
            i += 1
            A[i - 1], A[j - 1] = A[j - 1], A[i - 1]

    states.append(snapshot(A, i, r, p, r))
    A[i], A[r - 1] = A[r - 1], A[i]
    states.append(snapshot(A, i, r + 1, p, r))

    return states


states = partition_trace(A, 1, len(A))

header = r"""
\documentclass{article}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage[
  paperwidth=120mm,
  paperheight=315mm,
  margin=10mm
]{geometry}
\pagestyle{empty}
\begin{document}
\def\w{8mm}
\begin{center}
"""

footer = r"""
\end{center}
\end{document}
"""

doc = [header] + states + [footer]
latex_code = "\n".join(doc)

with open("E07.01-01.tex", "w") as f:
    f.write(latex_code)
