% https://github.com/Ziqi-Yang/latex_assignment_template
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{assignment}[a latex class for editing your assignment]

\LoadClass[11pt,letterpaper]{article}

\RequirePackage{amsmath}
\RequirePackage[left=2cm,right=2cm,top=1.5cm,bottom=2cm]{geometry}
\RequirePackage[dvipsnames]{xcolor}
\RequirePackage{listings}
\RequirePackage{tcolorbox}

\usepackage[dvipsnames]{xcolor}
\definecolor{Mycolor1}{HTML}{059C9C}


\setlength{\textwidth}{6.5in}
\setlength{\textheight}{9.in}
\setlength{\oddsidemargin}{0in}
\setlength{\headheight}{0in}


% create a box to highlight word
\newtcbox{\hword}[1][orange]{on line, arc = 0.3mm,auto outer arc,colback = #1!12!, colframe = #1!60!,colupper = black, boxsep =0mm, left =0.3mm, right = 0.3mm, top =0.4mm, bottom = 0.4mm,boxrule =0.2mm, bottomrule =0.2mm, toprule = 0.2mm}

% default code style

\newcommand{\indicator}[1]{\mathbf{1}_{\{#1\}}}

\lstset{
    % firstnumber=1, % starts the enumeration of lines of the code at 1. THis is default
    framerule=1pt,
    frame=tb,
    emphstyle={\small\ttfamily\bfseries\color{Orange}},
    numbers=left,
    numberstyle= \tiny\color{black},
    basicstyle = \small\ttfamily,
    keywordstyle    = \bfseries\color{Mycolor1},
    identifierstyle = \bfseries\color{Red!100},
    stringstyle     = \bfseries\color{green!10!orange},
    commentstyle    = \bfseries\color{Gray!100},
    % functionstyle    = \bfseries\color{Violet},
    breaklines      =   true,
    columns         =   fixed,
    basewidth       =   .5em,
    backgroundcolor=\color{Gray!15},
    tabsize=2,
    showspaces=false,
    showstringspaces=false,
}

\newcommand{\assignmentTitle}[7]{
    \begin{flushleft}
        \textbf{Namn:} #1\\
        \textbf{Personnummer:} #2 \\
        \textbf{Kurskod:} #3 \\
        \textbf{Kursansvarig:}: #4
    \end{flushleft}


    \begin{flushright}
        \vspace{-16mm}
        \includegraphics[height=2cm]{#5}
    \end{flushright}

    \begin{center}
        \vspace{-1cm}
        \textbf{\large #6} \\
        \textbf{#7} \\
        \textbf{\today}
    \end{center}

    \noindent\rule{\linewidth}{.6pt}
}
