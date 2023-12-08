% mythesis.cls
\ProvidesClass{GuariniThesis}[2023/12/05 My custom thesis class]
% \LoadClass{article}
\LoadClass{book}

% Load required packages
\RequirePackage{graphicx} % Required for inserting images
\RequirePackage{setspace}
\RequirePackage[left=1.5in, right=1in, top=1in, bottom=1in]{geometry}
\RequirePackage{xcolor}
\RequirePackage{calc}
\RequirePackage{titlesec}
\RequirePackage{natbib}
\RequirePackage{amsmath}

\RequirePackage{hyperref}
\hypersetup{colorlinks=true}
\hypersetup{linkcolor=black}



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
  \pagenumbering{roman}
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
    \copyrightnotice
    \dedication
    \GuariniAbstract
    \preface
    \tableofcontents
    \listoftables
    \listoffigures
    \contentStart
}

\endinput

% Astronomy Jounral Abreviations
\let\jnl@style=\rmfamily 
\def\ref@jnl#1{{\jnl@style#1}}% 
\newcommand\aj{\ref@jnl{AJ}}%        % Astronomical Journal 
\newcommand\psj{\ref@jnl{PSJ}}%       % Planetary Science Journal
\newcommand\araa{\ref@jnl{ARA\&A}}%  % Annual Review of Astron and Astrophys 
\renewcommand\apj{\ref@jnl{ApJ}}%    % Astrophysical Journal 
\newcommand\apjl{\ref@jnl{ApJL}}     % Astrophysical Journal, Letters 
\newcommand\apjs{\ref@jnl{ApJS}}%    % Astrophysical Journal, Supplement 
\renewcommand\ao{\ref@jnl{ApOpt}}%   % Applied Optics 
\newcommand\apss{\ref@jnl{Ap\&SS}}%  % Astrophysics and Space Science 
\newcommand\aap{\ref@jnl{A\&A}}%     % Astronomy and Astrophysics 
\newcommand\aapr{\ref@jnl{A\&A~Rv}}%  % Astronomy and Astrophysics Reviews 
\newcommand\aaps{\ref@jnl{A\&AS}}%    % Astronomy and Astrophysics, Supplement 
\newcommand\azh{\ref@jnl{AZh}}%       % Astronomicheskii Zhurnal 
\newcommand\baas{\ref@jnl{BAAS}}%     % Bulletin of the AAS 
\newcommand\icarus{\ref@jnl{Icarus}}% % Icarus
\newcommand\jaavso{\ref@jnl{JAAVSO}}  % The Journal of the American Association of Variable Star Observers
\newcommand\jrasc{\ref@jnl{JRASC}}%   % Journal of the RAS of Canada 
\newcommand\memras{\ref@jnl{MmRAS}}%  % Memoirs of the RAS 
\newcommand\mnras{\ref@jnl{MNRAS}}%   % Monthly Notices of the RAS 
\renewcommand\pra{\ref@jnl{PhRvA}}% % Physical Review A: General Physics 
\renewcommand\prb{\ref@jnl{PhRvB}}% % Physical Review B: Solid State 
\renewcommand\prc{\ref@jnl{PhRvC}}% % Physical Review C 
\renewcommand\prd{\ref@jnl{PhRvD}}% % Physical Review D 
\renewcommand\pre{\ref@jnl{PhRvE}}% % Physical Review E 
\renewcommand\prl{\ref@jnl{PhRvL}}% % Physical Review Letters 
\newcommand\pasp{\ref@jnl{PASP}}%     % Publications of the ASP 
\newcommand\pasj{\ref@jnl{PASJ}}%     % Publications of the ASJ 
\newcommand\qjras{\ref@jnl{QJRAS}}%   % Quarterly Journal of the RAS 
\newcommand\skytel{\ref@jnl{S\&T}}%   % Sky and Telescope 
\newcommand\solphys{\ref@jnl{SoPh}}% % Solar Physics 
\newcommand\sovast{\ref@jnl{Soviet~Ast.}}% % Soviet Astronomy 
\newcommand\ssr{\ref@jnl{SSRv}}% % Space Science Reviews 
\newcommand\zap{\ref@jnl{ZA}}%       % Zeitschrift fuer Astrophysik 
\renewcommand\nat{\ref@jnl{Nature}}%  % Nature 
\newcommand\iaucirc{\ref@jnl{IAUC}}% % IAU Cirulars 
\newcommand\aplett{\ref@jnl{Astrophys.~Lett.}}%  % Astrophysics Letters 
\newcommand\apspr{\ref@jnl{Astrophys.~Space~Phys.~Res.}}% % Astrophysics Space Physics Research 
\newcommand\bain{\ref@jnl{BAN}}% % Bulletin Astronomical Institute of the Netherlands 
\newcommand\fcp{\ref@jnl{FCPh}}%   % Fundamental Cosmic Physics 
\newcommand\gca{\ref@jnl{GeoCoA}}% % Geochimica Cosmochimica Acta 
\newcommand\grl{\ref@jnl{Geophys.~Res.~Lett.}}%  % Geophysics Research Letters 
\renewcommand\jcp{\ref@jnl{JChPh}}%     % Journal of Chemical Physics 
\newcommand\jgr{\ref@jnl{J.~Geophys.~Res.}}%     % Journal of Geophysics Research 
\newcommand\jqsrt{\ref@jnl{JQSRT}}%   % Journal of Quantitiative Spectroscopy and Radiative Trasfer 
\newcommand\memsai{\ref@jnl{MmSAI}}% % Mem. Societa Astronomica Italiana 
\newcommand\nphysa{\ref@jnl{NuPhA}}%     % Nuclear Physics A 
\newcommand\physrep{\ref@jnl{PhR}}%       % Physics Reports 
\newcommand\physscr{\ref@jnl{PhyS}}%        % Physica Scripta 
\newcommand\planss{\ref@jnl{Planet.~Space~Sci.}}%  % Planetary Space Science 
\newcommand\procspie{\ref@jnl{Proc.~SPIE}}%      % Proceedings of the SPIE 

\newcommand\actaa{\ref@jnl{AcA}}%  % Acta Astronomica
\newcommand\caa{\ref@jnl{ChA\&A}}%  % Chinese Astronomy and Astrophysics
\newcommand\cjaa{\ref@jnl{ChJA\&A}}%  % Chinese Journal of Astronomy and Astrophysics
\newcommand\jcap{\ref@jnl{JCAP}}%  % Journal of Cosmology and Astroparticle Physics
\newcommand\na{\ref@jnl{NewA}}%  % New Astronomy
\newcommand\nar{\ref@jnl{NewAR}}%  % New Astronomy Review
\newcommand\pasa{\ref@jnl{PASA}}%  % Publications of the Astron. Soc. of Australia
\newcommand\rmxaa{\ref@jnl{RMxAA}}%  % Revista Mexicana de Astronomia y Astrofisica

%% added feb 9, 2016
\newcommand\maps{\ref@jnl{M\&PS}}% Meteoritics and Planetary Science
\newcommand\aas{\ref@jnl{AAS Meeting Abstracts}}% American Astronomical Society Meeting Abstracts
\newcommand\dps{\ref@jnl{AAS/DPS Meeting Abstracts}}% American Astronomical Society/Division for Planetary Sciences Meeting Abstracts



\let\astap=\aap 
\let\apjlett=\apjl 
\let\apjsupp=\apjs 
\let\applopt=\ao
