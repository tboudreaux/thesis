% mythesis.cls
\ProvidesClass{mythesis}[2023/12/05 My custom thesis class]
\LoadClass{article}

% Load required packages
\RequirePackage{graphicx} % Required for inserting images
\RequirePackage{setspace}
\RequirePackage[left=1.5in, right=1in, top=1in, bottom=1in]{geometry}
\RequirePackage{color}
\RequirePackage{calc}

% Define the fontsize and linespacing
\renewcommand{\normalsize}{\fontsize{12}{14.4}\selectfont}

% Define custom commands for user input
\newcommand{\thesisTitle}[1]{\def\@thesisTitle{#1}}
\newcommand{\authorName}[1]{\def\@authorName{#1}}
\newcommand{\field}[1]{\def\@field{#1}}
\newcommand{\defenseDate}[1]{\def\@defenseDate{#1}}
\newcommand{\committeeChair}[1]{\def\@committeeChair{#1}}
\newcommand{\committeeMemberOne}[1]{\def\@committeeMemberOne{#1}}
\newcommand{\committeeMemberTwo}[1]{\def\@committeeMemberTwo{#1}}
\newcommand{\externalMember}[1]{\def\@externalMember{#1}}
\newcommand{\dedicationText}[1]{\def\@dedicationText{#1}}
\newcommand{\abstractText}[1]{\def\@abstractText{#1}}
\newcommand{\prefaceText}[1]{\def\@prefaceText{#1}}
\newcommand{\prelimFontSize}[1]{\def\@pelimFontSize{#1}}
\newcommand{\contentFontSize}[1]{\def\@contentFontSize{#1}}
\newcommand{\prelimLineSpace}[1]{\def\@pelimLineSpace{#1}}
\newcommand{\contentLineSpace}[1]{\def\@contentLineSpace{#1}}

\newcommand{\baseLineSkip}[1]{%
  \pgfmathparse{1.2*#1}%
  \pgfmathresult%
}


% Title page definition
\renewcommand{\maketitle}{
   \begin{titlepage}
   \selectfont
      \begin{center}
          \vspace*{1cm}
          \textbf{\@thesisTitle}
          % ... rest of the title page as above
          % Use \@authorName, \@field, etc. where needed
    
           \vspace{0.5cm}
            A Thesis\\
            Submitted to the Faculty\\
            in partial fulfillment of the requirements for the\\
            degree of\\
    
            \vspace{0.5cm}
    
            Doctor of Philosophy
    
            \vspace{0.5cm}
    
            in
    
            \@field
    
            by \@authorName
                
           \vspace{1.5cm}
    
           Guarini School of Graduate and Advances Studies \\
           Dartmouth College \\
           Hanover, New Hampshire
    
           \vspace{0.5cm}
           \@defenseDate
    
           \vspace{3cm}

\begin{flushright}
% \singlespacing


\begin{tabular}{r@{}}
\makebox[2.5in][c]{Examining Committee:} \\[1em]
\hline
\makebox[2.5in][l]{(chair) \textit{\textbf{\@committeeChair}}} \\[1em]
\hline
\makebox[2.5in][l]{\textit{\textbf{\@committeeMemberOne}}} \\[1em]
\hline
\makebox[2.5in][l]{\textit{\textbf{\@committeeMemberTwo}}} \\[1em]
\hline
\makebox[2.5in][l]{\textit{\textbf{\@externalMember}}} \\
\end{tabular}
\end{flushright}

\vfill

\begin{flushleft}
\line(1,0){200} \\
F. Jon Kull, Ph.D. \\
Dean of the Guarini School of Graduate and Advanced Studies
\end{flushleft}

\vspace{0.8cm}
      \end{center}
   \end{titlepage}
}



% Dedication page
\newcommand{\dedication}{
  \newpage
  \thispagestyle{empty}
  \vspace*{\fill}
  \begin{center}
    \textit{\@dedicationText}
  \end{center}
  \vspace*{\fill}
  \newpage
}

% Preface section
\newcommand{\preface}{
  \newpage
  \setstretch{1.5}
  \fontsize{12}{14.4}
  \selectfont
  \section*{Preface}
  \@prefaceText
  \newpage
}% Preface section
\newcommand{\GuariniAbstract}{
  \newpage
  \setstretch{1.5}
  \fontsize{12}{14.4}
  \selectfont
  {\centering\section*{Abstract}}
  \@abstractText
  \newpage
}

% Document content starts
\newcommand{\contentStart}{
  \newpage
  \pagenumbering{arabic}
}

% Copyright notice
\newcommand{\copyrightnotice}{
  \newpage
  \thispagestyle{empty}
  \vspace*{\fill}
  \begin{center}
    \textbf{Copyright Notice}
        This work is licensed under the Creative Commons\\
        Attribution-NonCommercial-ShareAlike 4.0 International License.\\
        To view a copy of this license, visit\\
        http://creativecommons.org/licenses/by-nc-sa/4.0/\\
        or send a letter to\\
        Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
  \end{center}
  \vspace*{\fill}
}

\newcommand{\makePrelim}{
    \maketitle
    \dedication
    \GuariniAbstract
    \preface
    \tableofcontents
    \listoftables
    \listoffigures
    \contentStart
}

\endinput
