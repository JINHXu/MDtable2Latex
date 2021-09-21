# JXu
# Convert a Markdown table to Latex.

PATH_INPUT_MD = './inpt_md.txt'
PATH_OPT_LATEX = './opt_latex.txt'

inlines = []
cline = ''

# read from inpt
with open(PATH_INPUT_MD, 'r') as inpt:
    lines = inpt.readlines()
    cline = lines[1].strip().replace('---', 'c')
    cline = cline.replace(' ', '')
    del lines[1]
    for line in lines:
        line = line.strip()
        line = line[1:]
        line = line[:-1]
        line = line.replace('|', '&')
        line = line+'\\\\'+'\n'
        inlines.append(line)

# write to opt
with open(PATH_OPT_LATEX, 'w') as opt:
    opt.write('\\begin{center}')
    opt.write('\\begin{tabular}'+'{' +cline+ '}'+'\n')
    for inline in inlines:
        opt.write('\hline'+'\n')
        opt.write(inline)
    opt.write('\hline'+'\n')
    opt.write('\\end{tabular}')
    opt.write('\\end{center}')
