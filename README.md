# MDtable2Latex

Kept experiment results documented in Markdwon? Run this [script]() to convert large MD table to Latex. \#10minutestobuildatool

## Requirements
Python 3.x

## Example 

| Number samples | minutes| accuracy | F-score (macro) | M1 F1 |  M2 F1 | F1 F1 | M1 acc\recall | M2 acc\recall | F1 acc/recall |
| --- | --- | --- | ---| ---|---|---| --- | --- | --- |
|30|2|0.95|0.948|0.914|0.931|1.0|0.965|0.918|1.0|
|50|3.5|0.971|0.97|0.952|0.96|1.0|0.984|0.936|1.0|
|75|5|0.985|0.985|0.976|0.978|1.0|0.992|0.965|1.0|
|105|7|0.986|0.986|0.979|0.979|1.0|0.983|0.975|1.0|
|128|9|0.987|0.987|0.981|0.982|1.0|0.996|0.968|1.0|

input Markdown table
```
| Number samples | minutes| accuracy | F-score (macro) | M1 F1 |  M2 F1 | F1 F1 | M1 acc\recall | M2 acc\recall | F1 acc/recall |
| --- | --- | --- | ---| ---|---|---| --- | --- | --- |
|30|2|0.95|0.948|0.914|0.931|1.0|0.965|0.918|1.0|
|50|3.5|0.971|0.97|0.952|0.96|1.0|0.984|0.936|1.0|
|75|5|0.985|0.985|0.976|0.978|1.0|0.992|0.965|1.0|
|105|7|0.986|0.986|0.979|0.979|1.0|0.983|0.975|1.0|
|128|9|0.987|0.987|0.981|0.982|1.0|0.996|0.968|1.0|
```

output Latex table
```
\begin{center}\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|}
\hline
 Number samples & minutes& accuracy & F-score (macro) & M1 F1 &  M2 F1 & F1 F1 & M1 acc\recall & M2 acc\recall & F1 acc/recall \\
\hline
30&2&0.95&0.948&0.914&0.931&1.0&0.965&0.918&1.0\\
\hline
50&3.5&0.971&0.97&0.952&0.96&1.0&0.984&0.936&1.0\\
\hline
75&5&0.985&0.985&0.976&0.978&1.0&0.992&0.965&1.0\\
\hline
105&7&0.986&0.986&0.979&0.979&1.0&0.983&0.975&1.0\\
\hline
128&9&0.987&0.987&0.981&0.982&1.0&0.996&0.968&1.0\\
\hline
\end{tabular}\end{center}
```

## Usage

Copy paste your Markdown table into `inpt_md.txt` 

Run the script:

`$ python ./mdtable2latex.py`

Copy paste `opt_latex.txt` to your `main.tex`<sup>[1](#myfootnote1)</sup>

And we are done 🎉🎉

<a name="myfootnote1">1</a>: You may need to manually take care of the escape symbols.
