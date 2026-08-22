@REM Run first pass
latexmk -pdf -outdir=build -shell-escape -gg Manuscript.tex
@REM Build dot files
dot -Tpdf -o build/swflow.pdf build/swflow.dot
@REM Rebuild final with new files
latexmk -pdf -outdir=build -shell-escape -g Manuscript.tex