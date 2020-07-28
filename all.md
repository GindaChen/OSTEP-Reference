# Chapter 00: Preface

## [CK+08] The xv6 Operating system

Russ Cox, Frans Kaashoek, Robert Morris, Nickolai Zeldovich 
From: http://pdos.csail.mit.edu/6.828/2008/index.html. xv6 was developed as a port of the original U NIX version 6 and represents a beautiful, clean, and simple way to understand a modern operating system.

## [F96] Six Easy Pieces: Essentials Of Physics Explained By Its Most Brilliant Teacher
Richard P. Feynman. Basic Books, 1996.
This book reprints the six easiest chapters of Feynman’s Lectures on Physics, from 1963. If you like Physics, it is a fantastic read.

## [HP90] Computer Architecture a Quantitative Approach” (1st ed.)
 David A. Patterson and John L. Hennessy . Morgan-Kaufman, 1990.
A book that encouraged each of us at our undergraduate institutions to pursue graduate studies; we later both had the pleasure of working with Patterson, who greatly shaped the foundations of our research careers.

## [KR88] The C Programming Language” 
Brian Kernighan and Dennis Ritchie. PrenticeHall, April 1988 
The C programming reference that everyone should have, by the people who invented the language.

## [K62] The Structure of Scientiﬁc Revolutions 
Thomas S. Kuhn. University of Chicago Press, 1962.
A great and famous read about the fundamentals of the scientiﬁc process. Mop-up work, anomaly, crisis, and revolution. We are mostly destined to do mop-up work, alas.

# Chapter 02: Introduction

## [SS+10]  Membrane: Operating System Support for Restartable File Systems 
 S. Sundararaman, S. Subramanian, A. Rajimwale, A. Arpaci-Dusseau, R. Arpaci-Dusseau, M. Swift. FAST ’10, San Jose, CA, February 2010. 
The great thing about writing your own class notes: you can advertise your own research. But this paper is actually pretty neat — when a ﬁle system hits a bug and crashes, Membrane auto-magically restarts it, all without applications or the rest of the system being affected.

## [BH00]  The Evolution of Operating Systems 
 P. Brinch Hansen. In ’Classic Operating Systems: From Batch Processing to Distributed Systems.’ Springer-Verlag, New York, 2000. 
This essay provides an intro to a wonderful collection of papers about historically signiﬁcant systems.

## [BS+09]  Tolerating File-System Mistakes with EnvyFS 
 L. Bairavasundaram, S. Sundararaman, A. Arpaci-Dusseau, R. Arpaci-Dusseau. USENIX ’09, San Diego, CA, June 2009. 
A fun paper about using multiple ﬁle systems at once to tolerate a mistake in any one of them.

## [B+72]  TENEX, A Paged Time Sharing System for the PDP-10 
 D. Bobrow, J. Burchﬁel, D. Murphy, R. Tomlinson. CACM, Volume 15, Number 3, March 1972. 
TENEX has much of the machinery found in modern operating systems; read more about it to see how much innovation was already in place in the early 1970’s.

## [S68]  SDS 940 Time-Sharing System 
 Scientiﬁc Data Systems. TECHNICAL MANUAL, SDS 90 11168, August 1968. 
Yes, a technical manual was the best we could ﬁnd. But it is fascinating to read these old system documents, and see how much was already in place in the late 1960’s. One of the minds behind the Berkeley Time-Sharing System (which eventually became the SDS system) was Butler Lampson, who later won a Turing award for his contributions in systems.

## [BOH10]  Computer Systems: A Programmer’s Perspective 
 R. Bryant and D. O’Hallaron. Addison-Wesley, 2010. 
Another great intro to how computer systems work. Has a little bit of overlap with this book — so if you’d like, you can skip the last few chapters of that book, or simply read them to get a different perspective on some of the same material. After all, one good way to build up your own knowledge is to hear as many other perspectives as possible, and then develop your own opinion and thoughts on the matter. You know, by thinking!

## [G85]  The GNU Manifesto 
 R. Stallman. 1985. www.gnu.org/gnu/manifesto.html. 
A huge part of Linux’s success was no doubt the presence of an excellent compiler, gcc, and other relevant pieces of open software, thanks to the GNU effort headed by Stallman. Stallman is a visionary when it comes to open source, and this manifesto lays out his thoughts as to why.

## [K+61]  One-Level Storage System 
 T. Kilburn, D.B.G. Edwards, M.J. Lanigan, F.H. Sumner. 
IRE Transactions on Electronic Computers, April 1962. The Atlas pioneered much of what you see in modern systems. However, this paper is not the best read. If you were to only read one, you might try the historical perspective below [L78].

## [L78]  The Manchester Mark I and Atlas: A Historical Perspective 
 S. H. Lavington. Communications of the ACM, Volume 21:1, January 1978. 
A nice piece of history on the early development of computer systems and the pioneering efforts of the Atlas. Of course, one could go back and read the Atlas papers themselves, but this paper provides a great overview and adds some historical perspective.

## [O72]  The Multics System: An Examination of its Structure 
 Elliott Organick. MIT Press, 1972. 
A great overview of Multics. So many good ideas, and yet it was an over-designed system, shooting for too much, and thus never really worked. A classic example of what Fred Brooks would call the second-system effect [B75].

## [PP03]  Introduction to Computing Systems: From Bits and Gates to C and Beyond 
 Yale N. Patt, Sanjay J. Patel. McGraw-Hill, 2003. 
One of our favorite intro to computing systems books. Starts at transistors and gets you all the way up to C; the early material is particularly great.

## [RT74]  The U NIX Time-Sharing System 
 Dennis M. Ritchie, Ken Thompson. CACM, Volume 17: 7, July 1974. 
A great summary of U NIX written as it was taking over the world of computing, by the people who wrote it.

## [B75]  The Mythical Man-Month 
 F. Brooks. Addison-Wesley, 1975. 
A classic text on software engineering; well worth the read.

# Chapter 04: Processes

## [BH70]  The Nucleus of a Multiprogramming System 
 Per Brinch Hansen. Communications of the ACM, Volume 13:4, April 1970. 
This paper introduces one of the ﬁrst microkernels in operating systems history, called Nucleus. The idea of smaller, more minimal systems is a theme that rears its head repeatedly in OS history; it all began with Brinch Hansen’s work described herein.

## [CK+08]  The xv6 Operating System 
 Russ Cox, Frans Kaashoek, Robert Morris, Nickolai Zeldovich. From: https://github.com/mit-pdos/xv6-public. 
The coolest real and little OS in the world. Download and play with it to learn more about the details of how operating systems actually work. We have been using an older version (2012-01-30-1-g1c41342) and hence some examples in the book may not match the latest in the source.

## [DV66]  Programming Semantics for Multiprogrammed Computations 
 Jack B. Dennis, Earl C. Van Horn. 
Communications of the ACM, Volume 9, Number 3, March 1966 . This paper deﬁned many of the early terms and concepts around building multiprogrammed systems.

## [L+75]  Policy/mechanism separation in Hydra 
 R. Levin, E. Cohen, W. Corwin, F. Pollack, W. Wulf. SOSP ’75, Austin, Texas, November 1975. 
An early paper about how to structure operating systems in a research OS known as Hydra. While Hydra never became a mainstream OS, some of its ideas inﬂuenced OS designers.

## [V+65]  Structure of the Multics Supervisor 
 V.A. Vyssotsky, F. J. Corbato, R. M. Graham. Fall Joint Computer Conference, 1965. 
An early paper on Multics, which described many of the basic ideas and terms that we ﬁnd in modern systems. Some of the vision behind computing as a utility are ﬁnally being realized in modern cloud systems.

# Chapter 05: Process API

## [B+19]  A fork() in the road 
Andrew Baumann, Jonathan Appavoo, Orran Krieger, Timothy Roscoe. HotOS ’19, Bertinoro, Italy. 
A fun paper full of fork()ing rage. Read it to get an opposing viewpoint on the U NIX process API. Presented at the always lively HotOS workshop, where systems researchers go to present extreme opinions in the hopes of pushing the community in new directions.

## [C63]  A Multiprocessor System Design 
Melvin E. Conway. AFIPS ’63 Fall Joint Computer Conference, New York, USA 1963. 
An early paper on how to design multiprocessing systems; may be the ﬁrst place the term fork() was used in the discussion of spawning new processes.

## [DV66]  Programming Semantics for Multiprogrammed Computations 
Jack B. Dennis and Earl C. Van Horn. Communications of the ACM, Volume 9, Number 3, March 1966. 
A classic paper that outlines the basics of multiprogrammed computer systems. Undoubtedly had great inﬂuence on Project MAC, Multics, and eventually U NIX.

## [J16]  They could be twins! 
Phoebe Jackson-Edwards. The Daily Mail. March 1, 2016.. 
This hard-hitting piece of journalism shows a bunch of weirdly similar child/parent photos and is frankly kind of mesmerizing. Go ahead, waste two minutes of your life and check it out. But don’t forget to come back here! This, in a microcosm, is the danger of surﬁng the web.

## [L83]  Hints for Computer Systems Design 
Butler Lampson. ACM Operating Systems Review, Volume 15:5, October 1983. 
Lampson’s famous hints on how to design computer systems. You should read it at some point in your life, and probably at many points in your life.

## [QI15]  With Great Power Comes Great Responsibility 
The Quote Investigator. Available: https://quoteinvestigator.com/2015/07/23/great-power. 
The quote investigator concludes that the earliest mention of this concept is 1793, in a collection of decrees made at the French National Convention. The speciﬁc quote: Ils doivent envisager qu’une grande responsabilit est la suite insparable d’un grand pouvoir”, which roughly translates to They must consider that great responsibility follows inseparably from great power.” Only in 1962 did the following words appear in Spider-Man: ...with great power there must also come–great responsibility!” So it looks like the French Revolution gets credit for this one, not Stan Lee. Sorry, Stan.

## [SR05]  Advanced Programming in the U NIX Environment 
W. Richard Stevens, Stephen A. Rago. Addison-Wesley, 2005. 
All nuances and subtleties of using U NIX APIs are found herein. Buy this book! Read it! And most importantly, live it.

# Chapter 06: Direct Execution

## [I11]  Intel 64 and IA-32 Architectures Software Developer’s Manual 
Volume 3A and 3B: System Programming Guide. Intel Corporation, January 2011. 
This is just a boring manual, but sometimes those are useful.

## [K+61]  One-Level Storage System 
T. Kilburn, D.B.G. Edwards, M.J. Lanigan, F.H. Sumner. IRE Transactions on Electronic Computers, April 1962. 
The Atlas pioneered much of what you see in modern systems. However, this paper is not the best one to read. If you were to only read one, you might try the historical perspective below [L78].

## [L78]  The Manchester Mark I and Atlas: A Historical Perspective 
S. H. Lavington. Communications of the ACM, 21:1, January 1978. 
A history of the early development of computers and the pioneering efforts of Atlas.

## [M+63]  A Time-Sharing Debugging System for a Small Computer 
J. McCarthy, S. Boilen, E. Fredkin, J. C. R. Licklider. AFIPS ’63 (Spring), May, 1963, New York, USA. An early paper about time-sharing that refers to using a timer interrupt; the quote that discusses it: 
The basic task of the channel 17 clock routine is to decide whether to remove the current user from core and if so to decide which user program to swap in as he goes out.”

## [S07]  The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86) 
Hovav Shacham. CCS ’07, October 2007. 
One of those awesome, mind-blowing ideas that you’ll see in research from time to time. The author shows that if you can jump into code arbitrarily, you can essentially stitch together any code sequence you like (given a large code base); read the paper for the details. The technique makes it even harder to defend against malicious attacks, alas.

## [O90]  Why Aren’t Operating Systems Getting Faster as Fast as Hardware? 
J. Ousterhout. USENIX Summer Conference, June 1990. 
A classic paper on the nature of operating system performance.

## [P10]  The Single UNIX Speciﬁcation, Version 3 
The Open Group, May 2010. Available: http://www.unix.org/version3/. 
This is hard and painful to read, so probably avoid it if you can. Like, unless someone is paying you to read it. Or, you’re just so curious you can’t help it!

## [C+04]  Microreboot — A Technique for Cheap Recovery 
G. Candea, S. Kawamoto, Y. Fujiki, G. Friedman, A. Fox. OSDI ’04, San Francisco, CA, December 2004. 
An excellent paper pointing out how far one can go with reboot in building more robust systems.

## [M11]  Mac OS 9 
Apple Computer, Inc.. January 2011. http://en.wikipedia.org/wiki/ Mac OS 9 . 
You can probably even ﬁnd an OS 9 emulator out there if you want to; check it out, it’s a fun little Mac!

## [A79]  Alto User’s Handbook 
Xerox. Xerox Palo Alto Research Center, September 1979. Available: http://history-computer.com/Library/AltoUsersHandbook.pdf. 
An amazing system, way ahead of its time. Became famous because Steve Jobs visited, took notes, and built Lisa and eventually Mac.

## [MS96]  lmbench: Portable tools for performance analysis 
Larry McVoy and Carl Staelin. USENIX Annual Technical Conference, January 1996. 
A fun paper about how to measure a number of different things about your OS and its performance. Download lmbench and give it a try.

# Chapter 07: CPU Scheduling

## [O45]  Animal Farm 
George Orwell. Secker and Warburg (London), 1945. 
A great but depressing allegorical book about power and its corruptions. Some say it is a critique of Stalin and the pre-WWII Stalin era in the U.S.S.R; we say it’s a critique of pigs.

## [C54]  Priority Assignment in Waiting Line Problems 
A. Cobham. Journal of Operations Research, 2:70, pages 70–76, 1954. 
The pioneering paper on using an SJF approach in scheduling the repair of machines.

## [K64]  Analysis of a Time-Shared Processor 
Leonard Kleinrock. Naval Research Logistics Quarterly, 11:1, pages 59–73, March 1964. 
May be the ﬁrst reference to the round-robin scheduling algorithm; certainly one of the ﬁrst analyses of said approach to scheduling a time-shared system.

## [CK68]  Computer Scheduling Methods and their Countermeasures 
Edward G. Coffman and Leonard Kleinrock. AFIPS ’68 (Spring), April 1968. 
An excellent early introduction to and analysis of a number of basic scheduling disciplines.

## [J91]  The Art of Computer Systems Performance Analysis: Techniques for Experimental Design, Measurement, Simulation, and Modeling 
R. Jain. Interscience, New York, April 1991. 
The standard text on computer systems measurement. A great reference for your library, for sure.

## [PV56]  Machine Repair as a Priority Waiting-Line Problem 
Thomas E. Phipps Jr., W. R. Van Voorhis. Operations Research, 4:1, pages 76–86, February 1956. 
Follow-on work that generalizes the SJF approach to machine repair from Cobham’s original work; also postulates the utility of an STCF approach in such an environment. Speciﬁcally, There are certain types of repair work, ... involving much dismantling and covering the ﬂoor with nuts and bolts, which certainly should not be interrupted once undertaken; in other cases it would be inadvisable to continue work on a long job if one or more short ones became available (p.81).”

## [MB91]  The effect of context switches on cache performance 
Jeffrey C. Mogul, Anita Borg. ASPLOS, 1991. 
A nice study on how cache performance can be affected by context switching; less of an issue in today’s systems where processors issue billions of instructions per second but context-switches still happen in the millisecond time range.

## [W15]  You can’t have your cake and eat it 
Authors: Unknown.. Wikipedia (as of December 2015). http://en.wikipedia.org/wiki/You can’t have your cake and eat it. 
The best part of this page is reading all the similar idioms from other languages. In Tamil, you can’t have both the moustache and drink the soup.”

## [B+79]  The Convoy Phenomenon 
M. Blasgen, J. Gray, M. Mitoma, T. Price. ACM Operating Systems Review, 13:2, April 1979. 
Perhaps the ﬁrst reference to convoys, which occurs in databases as well as the OS.

# Chapter 08: Multi-level Feedback

## [O11]  John Ousterhout’s Home Page 
John Ousterhout. www.stanford.edu/˜ouster/. 
The home page of the famous Professor Ousterhout. The two co-authors of this book had the pleasure of taking graduate operating systems from Ousterhout while in graduate school; indeed, this is where the two co-authors got to know each other, eventually leading to marriage, kids, and even this book. Thus, you really can blame Ousterhout for this entire mess you’re in.

## [AD00]  Multilevel Feedback Queue Scheduling in Solaris 
Andrea Arpaci-Dusseau. Available: http://www.ostep.org/Citations/notes-solaris.pdf. 
A great short set of notes by one of the authors on the details of the Solaris scheduler. OK, we are probably biased in this description, but the notes are pretty darn good.

## [C+62]  An Experimental Time-Sharing System 
F. J. Corbato, M. M. Daggett, R. C. Daley. IFIPS 1962. 
A bit hard to read, but the source of many of the ﬁrst ideas in multi-level feedback scheduling. Much of this later went into Multics, which one could argue was the most inﬂuential operating system of all time.

## [CS97]  Inside Windows NT 
Helen Custer and David A. Solomon. Microsoft Press, 1997. 
The NT book, if you want to learn about something other than U NIX. Of course, why would you? OK, we’re kidding; you might actually work for Microsoft some day you know.

## [B86]  The Design of the U NIX Operating System 
M.J. Bach. Prentice-Hall, 1986. 
One of the classic old books on how a real U NIX operating system is built; a deﬁnite must-read for kernel hackers.

## [E95]  An Analysis of Decay-Usage Scheduling in Multiprocessors 
D.H.J. Epema. SIGMETRICS ’95. 
A nice paper on the state of the art of scheduling back in the mid 1990s, including a good overview of the basic approach behind decay-usage schedulers.

## [LM+89]  The Design and Implementation of the 4.3BSD U NIX Operating System 
S.J. Lefﬂer, M.K. McKusick, M.J. Karels, J.S. Quarterman. Addison-Wesley, 1989. 
Another OS classic, written by four of the main people behind BSD. The later versions of this book, while more up to date, don’t quite match the beauty of this one.

## [Y+18]  Principled Schedulability Analysis for Distributed Storage Systems using Thread Architecture Models 
Suli Yang, Jing Liu, Andrea C. Arpaci-Dusseau, Remzi H. ArpaciDusseau. OSDI ’18, San Diego, California. 
A recent work of our group that demonstrates the difﬁculty of scheduling I/O requests within modern distributed storage systems such as Hive/HDFS, Cassandra, MongoDB, and Riak. Without care, a single user might be able to monopolize system resources.

## [P+95]  Informed Prefetching and Caching 
R.H. Patterson, G.A. Gibson, E. Ginting, D. Stodolsky, J. Zelenka. SOSP ’95, Copper Mountain, Colorado, October 1995. 
A fun paper about some very cool ideas in ﬁle systems, including how applications can give the OS advice about what ﬁles it is accessing and how it plans to access them.

## [M06]  Solaris Internals: Solaris 10 and OpenSolaris Kernel Architecture 
Richard McDougall. Prentice-Hall, 2006. 
A good book about Solaris and how it works.

# Chapter 09: Lottery Scheduling

## [W02]  Memory Resource Management in VMware ESX Server 
Carl A. Waldspurger. OSDI ’02, Boston, Massachusetts. 
he paper to read about memory management in VMMs (a.k.a., hypervisors). In addition to being relatively easy to read, the paper contains numerous cool ideas about this new type of VMM-level memory management.

## [W95]  Lottery and Stride Scheduling: Flexible Proportional-Share Resource Management 
Carl A. Waldspurger. Ph.D. Thesis, MIT, 1995. 
The award-winning thesis of Waldspurger’s that outlines lottery and stride scheduling. If you’re thinking of writing a Ph.D. dissertation at some point, you should always have a good example around, to give you something to strive for: this is such a good one.

## [B+18]  The Battle of the Schedulers: FreeBSD ULE vs. Linux CFS 
J. Bouron, S. Chevalley, B. Lepers, W. Zwaenepoel, R. Gouicem, J. Lawall, G. Muller, J. Sopena. USENIX ATC ’18, July 2018, Boston, Massachusetts. 
A recent, detailed work comparing Linux CFS and the FreeBSD schedulers. An excellent overview of each scheduler is also provided. The result of the comparison: inconclusive (in some cases CFS was better, and in others, ULE (the BSD scheduler), was. Sometimes in life there are no easy answers.

## [B72]  Symmetric binary B-Trees: Data Structure And Maintenance Algorithms 
Rudolf Bayer. Acta Informatica, Volume 1, Number 4, December 1972. 
A cool balanced tree introduced before you were born (most likely). One of many balanced trees out there; study your algorithms book for more alternatives!

## [AC97]  Extending Proportional-Share Scheduling to a Network of Workstations 
Andrea C. Arpaci-Dusseau and David E. Culler. PDPTA’97, June 1997. 
A paper by one of the authors on how to extend proportional-share scheduling to work better in a clustered environment.

## [KL88]  A Fair Share Scheduler 
J. Kay and P. Lauder. CACM, Volume 31 Issue 1, January 1988. 
An early reference to a fair-share scheduler.

## [J09]  Inside The Linux 2.6 Completely Fair Scheduler 
M. Tim Jones. December 15, 2009. http://ostep.org/Citations/inside-cfs.pdf. 
A simple overview of CFS from its earlier days. CFS was created by Ingo Molnar in a short burst of creativity which led to a 100K kernel patch developed in 62 hours.

## [K+15]  Proﬁling A Warehouse-scale Computer 
S. Kanev, P. Ranganathan, J. P. Darago, K. Hazelwood, T. Moseley, G. Wei, D. Brooks. ISCA ’15, June, 2015, Portland, Oregon. 
A fascinating study of where the cycles go in modern data centers, which are increasingly where most of computing happens. Almost 20% of CPU time is spent in the operating system, 5% in the scheduler alone!

## [D82]  Why Numbering Should Start At Zero 
Edsger Dijkstra, August 1982. Available: http://www.cs.utexas.edu/users/EWD/ewd08xx/EWD831.PDF. 
A short note from E. Dijkstra, one of the pioneers of computer science. We’ll be hearing much more on this guy in the section on Concurrency. In the meanwhile, enjoy this note, which includes this motivating quote:  One of my colleagues — not a computing scientist — accused a number of younger computing scientists of ’pedantry’ because they started numbering at zero.” The note explains why doing so is logical.

## [WW94]  Lottery Scheduling: Flexible Proportional-Share Resource Management 
Carl A. Waldspurger and William E. Weihl. OSDI ’94, November 1994. 
The landmark paper on lottery scheduling that got the systems community re-energized about scheduling, fair sharing, and the power of simple randomized algorithms.

# Chapter 10: Multi-CPU Scheduling

## [G83]  Using Cache Memory To Reduce Processor-Memory Trafﬁc 
James R. Goodman. ISCA ’83, Stockholm, Sweden, June 1983. 
The pioneering paper on how to use bus snooping, i.e., paying attention to requests you see on the bus, to build a cache coherence protocol. Goodman’s research over many years at Wisconsin is full of cleverness, this being but one example.

## [FLR98]  The Implementation of the Cilk-5 Multithreaded Language 
Matteo Frigo, Charles E. Leiserson, Keith Randall. PLDI ’98, Montreal, Canada, June 1998. 
Cilk is a lightweight language and runtime for writing parallel programs, and an excellent example of the work-stealing paradigm.

## [SA96]  Earliest Eligible Virtual Deadline First: A Flexible and Accurate Mechanism for Proportional Share Resource Allocation 
Ion Stoica and Hussein Abdel-Wahab. Technical Report TR-95-22, Old Dominion University, 1996. 
A tech report on this cool scheduling idea, from Ion Stoica, now a professor at U.C. Berkeley and world expert in networking, distributed systems, and many other things.

## [SHW11]  A Primer on Memory Consistency and Cache Coherence 
Daniel J. Sorin, Mark D. Hill, and David A. Wood. Synthesis Lectures in Computer Architecture. Morgan and Claypool Publishers, May 2011. 
A deﬁnitive overview of memory consistency and multiprocessor caching. Required reading for anyone who likes to know way too much about a given topic.

## [M11]  Towards Transparent CPU Scheduling 
Joseph T. Meehean. Doctoral Dissertation at University of Wisconsin—Madison, 2011. 
A dissertation that covers a lot of the details of how modern Linux multiprocessor scheduling works. Pretty awesome! But, as co-advisors of Joe’s, we may be a bit biased here.

## [CSG99]  Parallel Computer Architecture: A Hardware/Software Approach 
David E. Culler, Jaswinder Pal Singh, and Anoop Gupta. Morgan Kaufmann, 1999. 
A treasure ﬁlled with details about parallel machines and algorithms. As Mark Hill humorously observes on the jacket, the book contains more information than most research papers.

## [B+10]  An Analysis of Linux Scalability to Many Cores Abstract 
Silas Boyd-Wickizer, Austin T. Clements, Yandong Mao, Aleksey Pesterev, M. Frans Kaashoek, Robert Morris, Nickolai Zeldovich. OSDI ’10, Vancouver, Canada, October 2010. 
A terriﬁc modern paper on the difﬁculties of scaling Linux to many cores.

## [A90]  The Performance of Spin Lock Alternatives for Shared-Memory Multiprocessors 
Thomas E. Anderson. IEEE TPDS Volume 1:1, January 1990. 
A classic paper on how different locking alternatives do and don’t scale. By Tom Anderson, very well known researcher in both systems and networking. And author of a very ﬁne OS textbook, we must say.

## [TTG95]  Evaluating the Performance of Cache-Afﬁnity Scheduling in Shared-Memory Multiprocessors 
Josep Torrellas, Andrew Tucker, Anoop Gupta. Journal of Parallel and Distributed Computing, Volume 24:2, February 1995. 
This is not the ﬁrst paper on the topic, but it has citations to earlier work, and is a more readable and practical paper than some of the earlier queuingbased analysis papers.

# Chapter 13: Address Spaces

## [R+89]  Mach: A System Software kernel 
R. Rashid, D. Julin, D. Orr, R. Sanzi, R. Baron, A. Forin, D. Golub, M. Jones. COMPCON ’89, February 1989. 
Although not the ﬁrst project on microkernels per se, the Mach project at CMU was well-known and inﬂuential; it still lives today deep in the bowels of Mac OS X.

## [NS07]  Valgrind: A Framework for Heavyweight Dynamic Binary Instrumentation 
N. Nethercote, J. Seward. PLDI 2007, San Diego, California, June 2007. 
Valgrind is a lifesaver of a program for those who use unsafe languages like C. Read this paper to learn about its very cool binary instrumentation techniques – it’s really quite impressive.

## [M83]  Reminiscences on the History of Time Sharing 
John McCarthy. 1983. Available: http://www-formal.stanford.edu/jmc/history/timesharing/timesharing.html. 
A terriﬁc historical note on where the idea of time-sharing might have come fzshortm, including some doubts towards those who cite Strachey’s work [S59] as the by pioneering work in this area..

## [M+63]  A Time-Sharing Debugging System for a Small Computer 
J. McCarthy, S. Boilen, E. Fredkin, J. C. R. Licklider. AFIPS ’63 (Spring), New York, NY, May 1963. 
A great early example of a system that swapped program memory to the drum” when the program wasn’t running, and then back into core” memory when it was about to be run.

## [M62]  Time-Sharing Computer Systems 
J. McCarthy. Management and the Computer of the Future, MIT Press, Cambridge, MA, 1962. 
Probably McCarthy’s earliest recorded paper on time sharing. In another paper [M83], he claims to have been thinking of the idea since 1957. McCarthy left the systems area and went on to become a giant in Artiﬁcial Intelligence at Stanford, including the creation of the LISP programming language. See McCarthy’s home page for more info: http://www-formal.stanford.edu/jmc/

## [L60]  Man-Computer Symbiosis 
J. C. R. Licklider. IRE Transactions on Human Factors in Electronics, HFE-1:1, March 1960. 
A funky paper about how computers and people are going to enter into a symbiotic age; clearly well ahead of its time but a fascinating read nonetheless.

## [S59]  Time Sharing in Large Fast Computers 
C. Strachey. Proceedings of the International Conference on Information Processing, UNESCO, June 1959. 
One of the earliest references on time sharing.

## [CV65]  Introduction and Overview of the Multics System 
F. J. Corbato, V. A. Vyssotsky. Fall Joint Computer Conference, 1965. 
A great early Multics paper. Here is the great quote about time sharing: The impetus for time-sharing ﬁrst arose from professional programmers because of their constant frustration in debugging programs at batch processing installations. Thus, the original goal was to time-share computers to allow simultaneous access by several persons while giving to each of them the illusion of having the whole machine at his disposal.”

## [BH70]  The Nucleus of a Multiprogramming System 
Per Brinch Hansen. Communications of the ACM, 13:4, April 1970. 
The ﬁrst paper to suggest that the OS, or kernel, should be a minimal and ﬂexible substrate for building customized operating systems; this theme is revisited throughout OS research history.

## [S+03]  Improving the Reliability of Commodity Operating Systems 
M. M. Swift, B. N. Bershad, H. M. Levy. SOSP ’03. 
The ﬁrst paper to show how microkernel-like thinking can improve operating system reliability.

## [DV66]  Programming Semantics for Multiprogrammed Computations 
Jack B. Dennis, Earl C. Van Horn. Communications of the ACM, Volume 9, Number 3, March 1966. 
An early paper (but not the ﬁrst) on multiprogramming.

# Chapter 14: Memory API

## [SN05] Using Valgrind to Detect Undeﬁned Value Errors with Bit-precision
J. Seward, N. Nethercote. USENIX ’05. 
How to use valgrind to ﬁnd certain types of errors.

## [SR05] Advanced Programming in the U NIX Environment
W. Richard Stevens, Stephen A. Rago. Addison-Wesley, 2005. 
We’ve said it before, we’ll say it again: read this book many times and use it as a reference whenever you are in doubt. The authors are always surprised at how each time they read something in this book, they learn something new, even after many years of C programming.

## [W06] Survey on Buffer Overﬂow Attacks and Countermeasures
T. Werthman. Available: www.nds.rub.de/lehre/seminar/SS06/Werthmann BufferOverﬂow.pdf. 
A nice survey of buffer overﬂows and some of the security problems they cause. Refers to many of the famous exploits.

## [N+07] Exterminator: Automatically Correcting Memory Errors with High Probability
G. Novark, E. D. Berger, B. G. Zorn. PLDI 2007, San Diego, California. 
A cool paper on ﬁnding and correcting memory errors automatically, and a great overview of many common errors in C and C++ programs. An extended version of this paper is available CACM (Volume 51, Issue 12, December 2008).

## [KR88] The C Programming Language
Brian Kernighan, Dennis Ritchie. Prentice-Hall 1988. 
The C book, by the developers of C. Read it once, do some programming, then read it again, and then keep it near your desk or wherever you program.

## [HJ92] Purify: Fast Detection of Memory Leaks and Access Errors
R. Hastings, B. Joyce. USENIX Winter ’92. 
The paper behind the cool Purify tool, now a commercial product.

# Chapter 15: Address Translation

## [M65] On Dynamic Program Relocation
W.C. McGee. IBM Systems Journal, Volume 4:3, 1965, pages 184–199. 
This paper is a nice summary of early work on dynamic relocation, as well as some basics on static relocation.

## [P90] Relocating loader for MS-DOS .EXE executable ﬁles
Kenneth D. A. Pillay. Microprocessors & Microsystems archive, Volume 14:7 (September 1990). 
An example of a relocating loader for MS-DOS. Not the ﬁrst one, but just a relatively modern example of how such a system works.

## [SS74] The Protection of Information in Computer Systems
J. Saltzer and M. Schroeder. CACM, July 1974. 
From this paper: The concepts of base-and-bound register and hardware-interpreted descriptors appeared, apparently independently, between 1957 and 1959 on three projects with diverse goals. At M.I.T., McCarthy suggested the base-and-bound idea as part of the memory protection system necessary to make time-sharing feasible. IBM independently developed the base-and-bound register as a mechanism to permit reliable multiprogramming of the Stretch (7030) computer system. At Burroughs, R. Barton suggested that hardware-interpreted descriptors would provide direct support for the naming scope rules of higher level languages in the B5000 computer system.” We found this quote on Mark Smotherman’s cool history pages [S04]; see them for more information.

## [S04] System Call Support
Mark Smotherman. May 2004. people.cs.clemson.edu/ ˜mark/syscall.html. 
A neat history of system call support. Smotherman has also collected some early history on items like interrupts and other fun aspects of computing history. See his web pages for more details.

## [WL+93] Efﬁcient Software-based Fault Isolation
Robert Wahbe, Steven Lucco, Thomas E. Anderson, Susan L. Graham. SOSP ’93. 
A terriﬁc paper about how you can use compiler support to bound memory references from a program, without hardware support. The paper sparked renewed interest in software techniques for isolation of memory references.

## [W17] Answer to footnote: Is there anything other than havoc that can be wreaked?
Waciuma Wanjohi. October 2017. 
Amazingly, this enterprising reader found the answer via google’s Ngram viewing tool (available at the following URL: http://books.google.com/ngrams). The answer, thanks to Mr. Wanjohi It’s only since about 1970 that ’wreak havoc’ has been more popular than ’wreak vengeance’. In the 1800s, the word wreak was almost always followed by ’his/their vengeance’.” Apparently, when you wreak, you are up to no good, but at least wreakers have some options now.

# Chapter 16: Segmentation

## [R69] A note on storage fragmentation and program segmentation
Brian Randell. Communications of the ACM, Volume 12:7, July 1969. 
One of the earliest papers to discuss fragmentation.

## [W+95] Dynamic Storage Allocation: A Survey and Critical Review
Paul R. Wilson, Mark S. Johnstone, Michael Neely, David Boles. 
International Workshop on Memory Management, Scotland, UK, September 1995. A great survey paper on memory allocators.

## [CV65] Introduction and Overview of the Multics System
F. J. Corbato, V. A. Vyssotsky. 
Fall Joint Computer Conference, 1965. One of ﬁve papers presented on Multics at the Fall Joint Computer Conference; oh to be a ﬂy on the wall in that room that day!

## [DD68] Virtual Memory, Processes, and Sharing in Multics
Robert C. Daley and Jack B. Dennis. Communications of the ACM, Volume 11:5, May 1968. 
An early paper on how to perform dynamic linking in Multics, which was way ahead of its time. Dynamic linking ﬁnally found its way back into systems about 20 years later, as the large X-windows libraries demanded it. Some say that these large X11 libraries were MIT’s revenge for removing support for dynamic linking in early versions of U NIX!

## [G62] Fact Segmentation
M. N. Greenﬁeld. Proceedings of the SJCC, Volume 21, May 1962. 
Another early paper on segmentation; so early that it has no references to other work.

## [I09] Intel 64 and IA-32 Architectures Software Developer’s Manuals
Intel. 2009. Available: http://www.intel.com/products/processor/manuals. 
Try reading about segmentation in here (Chapter 3 in Volume 3a); it’ll hurt your head, at least a little bit.

## [H61] Program Organization and Record Keeping for Dynamic Storage
A. W. Holt. Communications of the ACM, Volume 4:10, October 1961. 
An incredibly early and difﬁcult to read paper about segmentation and some of its uses.

## [LL82] Virtual Memory Management in the VAX/VMS Operating System
Henry M. Levy, Peter H. Lipman. IEEE Computer, Volume 15:3, March 1982. 
A classic memory management system, with lots of common sense in its design. We’ll study it in more detail in a later chapter.

## [RK68] Dynamic Storage Allocation Systems
B. Randell and C.J. Kuehner. Communications of the ACM, Volume 11:5, May 1968. 
A nice overview of the differences between paging and segmentation, with some historical discussion of various machines.

## [L83] Hints for Computer Systems Design
Butler Lampson. ACM Operating Systems Review, 15:5, October 1983. 
A treasure-trove of sage advice on how to build systems. Hard to read in one sitting; take it in a little at a time, like a ﬁne wine, or a reference manual.

## [K68] The Art of Computer Programming: Volume I
Donald Knuth. Addison-Wesley, 1968. 
Knuth is famous not only for his early books on the Art of Computer Programming but for his typesetting system TeX which is still a powerhouse typesetting tool used by professionals today, and indeed to typeset this very book. His tomes on algorithms are a great early reference to many of the algorithms that underly computing systems today.

# Chapter 17: Free Space Management

## [B94] The Slab Allocator: An Object-Caching Kernel Memory Allocator
Jeff Bonwick. USENIX ’94. 
A cool paper about how to build an allocator for an operating system kernel, and a great example of how to specialize for particular common object sizes.

## [B+00] Hoard: A Scalable Memory Allocator for Multithreaded Applications
Emery D. Berger, Kathryn S. McKinley, Robert D. Blumofe, Paul R. Wilson. ASPLOS-IX, November 2000. 
Berger and company’s excellent allocator for multiprocessor systems. Beyond just being a fun paper, also used in practice!

## [K65] A Fast Storage Allocator
Kenneth C. Knowlton. Communications of the ACM, Volume 8:10, October 1965. 
The common reference for buddy allocation. Random strange fact: Knuth gives credit for the idea not to Knowlton but to Harry Markowitz, a Nobel-prize winning economist. Another strange fact: Knuth communicates all of his emails via a secretary; he doesn’t send email himself, rather he tells his secretary what email to send and then the secretary does the work of emailing. Last Knuth fact: he created TeX, the tool used to typeset this book. It is an amazing piece of software 4.

## [S15] Understanding glibc malloc
Sploitfun. February, 2015. sploitfun.wordpress.com/ 2015/02/10/understanding-glibc-malloc/. 
A deep dive into how glibc malloc works. Amazingly detailed and a very cool read.

## [E06] A Scalable Concurrent malloc(3) Implementation for FreeBSD
Jason Evans. April, 2006. http://people.freebsd.org/˜jasone/jemalloc/bsdcan2006/jemalloc.pdf. 
A detailed look at how to build a real modern allocator for use in multiprocessors. The "jemalloc" allocator is in widespread use today, within FreeBSD, NetBSD, Mozilla Firefox, and within Facebook.

## [W+95] Dynamic Storage Allocation: A Survey and Critical Review
Paul R. Wilson, Mark S. Johnstone, Michael Neely, David Boles. International Workshop on Memory Management, Scotland, UK, September 1995. 
An excellent and far-reaching survey of many facets of memory allocation. Far too much detail to go into in this tiny chapter!

# Chapter 18: Introduction to Paging

## [L78] The Manchester Mark I and Atlas: A Historical Perspective
S. H. Lavington. Communications of the ACM, Volume 21:1, January 1978. 
This paper is a great retrospective of some of the history of the development of some important computer systems. As we sometimes forget in the US, many of these new ideas came from overseas.

## [I09] Intel 64 and IA-32 Architectures Software Developer’s Manuals” Intel, 2009. Available: http://www.intel.com/products/processor/manuals. 
In particular, pay attention to Volume 3A: System Programming Guide Part 1” and Volume 3B: System Programming Guide Part 2”.


## [KE+62] One-level Storage System
T. Kilburn, D.B.G. Edwards, M.J. Lanigan, F.H. Sumner. IRE Trans. EC-11, 2, 1962. Reprinted in Bell and Newell, Computer Structures: Readings and Examples”. McGraw-Hill, New York, 1971. 
The Atlas pioneered the idea of dividing memory into ﬁxed-sized pages and in many senses was an early form of the memory-management ideas we see in modern computer systems.

# Chapter 19: Translation Lookaside Buffers

## [BC91] Performance from Architecture: Comparing a RISC and a CISC with Similar Hardware Organization
D. Bhandarkar and Douglas W. Clark. Communications of the ACM, September 1991. 
A great and fair comparison between RISC and CISC. The bottom line: on similar hardware, RISC was about a factor of three better in performance.

## [WG00] The SPARC Architecture Manual: Version 9
David L. Weaver and Tom Germond. SPARC International, San Jose, California, September 2000. Available: www.sparc.org/ standards/SPARCV9.pdf. 
Another manual. I bet you were hoping for a more fun citation to end this chapter.

## [W03] A Survey on the Interaction Between Caching, Translation and Protection
Adam Wiggins. University of New South Wales TR UNSW-CSE-TR-0321, August, 2003. 
An excellent survey of how TLBs interact with other parts of the CPU pipeline, namely hardware caches.

## [PS81] RISC-I: A Reduced Instruction Set VLSI Computer
D.A. Patterson and C.H. Sequin. ISCA ’81, Minneapolis, May 1981. 
The paper that introduced the term RISC, and started the avalanche of research into simplifying computer chips for performance.

## [I09] Intel 64 and IA-32 Architectures Software Developer’s Manuals
Intel, 2009. Available: http://www.intel.com/products/processor/manuals. 
In particular, pay attention to Volume 3A: System Programming Guide” Part 1 and Volume 3B: System Programming Guide Part 2”.

## [HP06] Computer Architecture: A Quantitative Approach
John Hennessy and David Patterson. Morgan-Kaufmann, 2006. 
A great book about computer architecture. We have a particular attachment to the classic ﬁrst edition.

## [CP78] The architecture of the IBM System/370
R.P. Case, A. Padegs. Communications of the ACM. 21:1, 73-96, January 1978. 
Perhaps the ﬁrst paper to use the term translation lookaside buffer. The name arises from the historical name for a cache, which was a lookaside buffer as called by those developing the Atlas system at the University of Manchester; a cache of address translations thus became a translation lookaside buffer. Even though the term lookaside buffer fell out of favor, TLB seems to have stuck, for whatever reason.

## [CG68] Shared-access Data Processing System
John F. Couleur, Edward L. Glaser. Patent 3412382, November 1968. 
The patent that contains the idea for an associative memory to store address translations. The idea, according to Couleur, came in 1964.

## [C95] The Core of the Black Canyon Computer Corporation
John Couleur. IEEE Annals of History of Computing, 17:4, 1995. 
In this fascinating historical note, Couleur talks about how he invented the TLB in 1964 while working for GE, and the fortuitous collaboration that thus ensued with the Project MAC folks at MIT.

## [SB92] CPU Performance Evaluation and Execution Time Prediction Using Narrow Spectrum Benchmarking
Rafael H. Saavedra-Barrera. EECS Department, University of California, Berkeley. Technical Report No. UCB/CSD-92-684, February 1992.. 
A great dissertation about how to predict execution time of applications by breaking them down into constituent pieces and knowing the cost of each piece. Probably the most interesting part that comes out of this work is the tool to measure details of the cache hierarchy (described in Chapter 5). Make sure to check out the wonderful diagrams therein.

## [H93] MIPS R4000 Microprocessor User’s Manual
Joe Heinrich. Prentice-Hall, June 1993. Available: http://cag.csail.mit.edu/raw/ . documents/R4400 Uman book Ed2.pdf 
A manual, one that is surprisingly readable. Or is it?

## [CM00] The evolution of RISC technology at IBM
John Cocke, V. Markstein. IBM Journal of Research and Development, 44:1/2. 
A summary of the ideas and work behind the IBM 801, which many consider the ﬁrst true RISC microprocessor.

# Chapter 20: Advanced Page Tables

## [BOH10] Computer Systems: A Programmer’s Perspective
Randal E. Bryant and David R. O’Hallaron. Addison-Wesley, 2010. 
We have yet to ﬁnd a good ﬁrst reference to the multi-level page table. However, this great textbook by Bryant and O’Hallaron dives into the details of x86, which at least is an early system that used such structures. It’s also just a great book to have.

## [JM98] Virtual Memory: Issues of Implementation
Bruce Jacob, Trevor Mudge. IEEE Computer, June 1998. 
An excellent survey of a number of different systems and their approach to virtualizing memory. Plenty of details on x86, PowerPC, MIPS, and other architectures.

## [LL82] Virtual Memory Management in the VAX/VMS Operating System
Hank Levy, P. Lipman. IEEE Computer, Vol. 15, No. 3, March 1982. 
A terriﬁc paper about a real virtual memory manager in a classic operating system, VMS. So terriﬁc, in fact, that we’ll use it to review everything we’ve learned about virtual memory thus far a few chapters from now.

## [M28] Reese’s Peanut Butter Cups
Mars Candy Corporation. Published at stores near you. 
Apparently these ﬁne confections were invented in 1928 by Harry Burnett Reese, a former dairy farmer and shipping foreman for one Milton S. Hershey. At least, that is what it says on Wikipedia. If true, Hershey and Reese probably hate each other’s guts, as any two chocolate barons should.

## [N+02] Practical, Transparent Operating System Support for Superpages
Juan Navarro, Sitaram Iyer, Peter Druschel, Alan Cox. OSDI ’02, Boston, Massachusetts, October 2002. 
A nice paper showing all the details you have to get right to incorporate large pages, or superpages, into a modern OS. Not as easy as you might think, alas.

## [M07] Multics: History
Available: http://www.multicians.org/history.html. 
This amazing web site provides a huge amount of history on the Multics system, certainly one of the most inﬂuential systems in OS history. The quote from therein: Jack Dennis of MIT contributed inﬂuential architectural ideas to the beginning of Multics, especially the idea of combining paging and segmentation.” (from Section 1.2.1)

# Chapter 21: Swapping - Mechanisms

## [LL82] Virtual Memory Management in the VAX/VMS Operating System
Hank Levy, P. Lipman. IEEE Computer, Vol. 15, No. 3, March 1982. 
Not the ﬁrst place where page clustering was used, but a clear and simple explanation of how such a mechanism works. We sure cite this paper a lot!

## [D97] Before Memory Was Virtual
Peter Denning. In the Beginning: Recollections of Software Pioneers, Wiley, November 1997. 
An excellent historical piece by one of the pioneers of virtual memory and working sets.

## [CS94] Take Our Word For it 
F. Corbato, R. Steinberg. www.takeourword.com/TOW146 (Page 4). 
Richard Steinberg writes: Someone has asked me the origin of the word daemon as it applies to computing. Best I can tell based on my research, the word was ﬁrst used by people on your team at Project MAC using the IBM 7094 in 1963.” Professor Corbato replies: Our use of the word daemon was inspired by the Maxwell’s daemon of physics and thermodynamics (my background is in physics). Maxwell’s daemon was an imaginary agent which helped sort molecules of different speeds and worked tirelessly in the background. We fancifully began to use the word daemon to describe background processes which worked tirelessly to perform system chores.”

## [G+95] Idleness is not sloth
Richard Golding, Peter Bosch, Carl Staelin, Tim Sullivan, John Wilkes. USENIX ATC ’95, New Orleans, Louisiana. 
A fun and easy-to-read discussion of how idle time can be better used in systems, with lots of good examples.

# Chapter 22: Swapping - Policies

## [MM03] ARC: A Self-Tuning, Low Overhead Replacement Cache
Nimrod Megiddo and Dharmendra S. Modha. FAST 2003, February 2003, San Jose, California. 
An excellent modern paper about replacement algorithms, which includes a new policy, ARC, that is now used in some systems. Recognized in 2014 as a "Test of Time" award winner by the storage systems community at the FAST ’14 conference.

## [KE+62] One-level Storage System
T. Kilburn, D.B.G. Edwards, M.J. Lanigan, F.H. Sumner. IRE Trans. EC-11:2, 1962. 
Although Atlas had a use bit, it only had a very small number of pages, and thus the scanning of the use bits in large memories was not a problem the authors solved.

## [CD85] An Evaluation of Buffer Management Strategies for Relational Database Systems
Hong-Tai Chou, David J. DeWitt. VLDB ’85, Stockholm, Sweden, August 1985. 
A famous database paper on the different buffering strategies you should use under a number of common database access patterns. The more general lesson: if you know something about a workload, you can tailor policies to do better than the general-purpose ones usually found in the OS.

## [HP06] Computer Architecture: A Quantitative Approach
John Hennessy and David Patterson. Morgan-Kaufmann, 2006. A marvelous book about computer architecture. Read it!


## [FP89] Electrochemically Induced Nuclear Fusion of Deuterium
Martin Fleischmann, Stanley Pons. Journal of Electroanalytical Chemistry, Volume 26, Number 2, Part 1, April, 1989. 
The famous paper that would have revolutionized the world in providing an easy way to generate nearly-inﬁnite power from jars of water with a little metal in them. Unfortunately, the results published (and widely publicized) by Pons and Fleischmann were impossible to reproduce, and thus these two well-meaning scientists were discredited (and certainly, mocked). The only guy really happy about this result was Marvin Hawkins, whose name was left off this paper even though he participated in the work, thus avoiding association with one of the biggest scientiﬁc goofs of the 20th century.

## [D70] Virtual Memory
Peter J. Denning. Computing Surveys, Vol. 2, No. 3, September 1970. 
Denning’s early and famous survey on virtual memory systems.

## [C69] A Paging Experiment with the Multics System
F.J. Corbato. Included in a Festschrift published in honor of Prof. P.M. Morse. MIT Press, Cambridge, MA, 1969. 
The original (and hard to ﬁnd!) reference to the clock algorithm, though not the ﬁrst usage of a use bit. Thanks to H. Balakrishnan of MIT for digging up this paper for us.

## [H87] Aspects of Cache Memory and Instruction Buffer Performance
Mark D. Hill. Ph.D. Dissertation, U.C. Berkeley, 1987. 
Mark Hill, in his dissertation work, introduced the Three C’s, which later gained wide popularity with its inclusion in H&P [HP06]. The quote from therein: I have found it useful to partition misses ... into three components intuitively based on the cause of the misses (page 49).”

## [EF78] Cold-start vs. Warm-start Miss Ratios
Malcolm C. Easton, Ronald Fagin. Communications of the ACM, 21:10, October 1978. 
A good discussion of cold- vs. warm-start misses.

## [M+70] Evaluation Techniques for Storage Hierarchies
R. L. Mattson, J. Gecsei, D. R. Slutz, I. L. Traiger. IBM Systems Journal, Volume 9:2, 1970. 
A paper that is mostly about how to simulate cache hierarchies efﬁciently; certainly a classic in that regard, as well for its excellent discussion of some of the properties of various replacement algorithms. Can you ﬁgure out why the stack property might be useful for simulating a lot of different-sized caches at once?

## [BNS69] An Anomaly in Space-time Characteristics of Certain Programs Running in a Paging Machine
L. A. Belady, R. A. Nelson, G. S. Shedler. Communications of the ACM, 12:6, June 1969. 
Introduction of the little sequence of memory references known as Belady’s Anomaly. How do Nelson and Shedler feel about this name, we wonder?

## [AD03] Run-Time Adaptation in River
Remzi H. Arpaci-Dusseau. ACM TOCS, 21:1, February 2003. 
A summary of one of the authors’ dissertation work on a system named River, where he learned that comparison against the ideal is an important technique for system designers.

## [B66] A Study of Replacement Algorithms for Virtual-Storage Computer
Laszlo A. Belady. IBM Systems Journal 5(2): 78-101, 1966. 
The paper that introduces the simple way to compute the optimal behavior of a policy (the MIN algorithm).

# Chapter 23: Complete VM Systems

## [B+13] Efﬁcient Virtual Memory for Big Memory Servers
A. Basu, J. Gandhi, J. Chang, M. D. Hill, M. M. Swift. ISCA ’13, June 2013, Tel-Aviv, Israel. 
A recent work showing that TLBs matter, consuming 10% of cycles for large-memory workloads. The solution: one massive segment to hold large data sets. We go backward, so that we can go forward!

## [S+04] On the Effectiveness of Address-space Randomization
H. Shacham, M. Page, B. Pfaff, E. J. Goh, N. Modadugu, D. Boneh. CCS ’04, October 2004. 
A description of the return-tolibc attack and its limits. Start reading, but be wary: the rabbit hole of systems security is deep...

## [O16] Virtual Memory and Linux
A. Ott. Embedded Linux Conference, April 2016. https://events.static.linuxfound.org/sites/events/ﬁles/slides/elc 2016 mem.pdf . 
A useful set of slides which gives an overview of the Linux VM.

## [M04] Cloud Atlas
D. Mitchell. Random House, 2004. 
It’s hard to pick a favorite book. There are too many! Each is great in its own unique way. But it’d be hard for these authors not to pick Cloud Atlas”, a fantastic, sprawling epic about the human condition, from where the the last quote of this chapter is lifted. If you are smart – and we think you are – you should stop reading obscure commentary in the references and instead read Cloud Atlas”; you’ll thank us later.

## [LL82] Virtual Memory Management in the VAX/VMS Operating System
H. Levy, P. Lipman. IEEE Computer, Volume 15:3, March 1982. 
Read the original source of most of this material. Particularly important if you wish to go to graduate school, where all you do is read papers, work, read some more papers, work more, eventually write a paper, and then work some more.

## [JS94] 2Q: A Low Overhead High Performance Buffer Management Replacement Algorithm
T. Johnson, D. Shasha. VLDB ’94, Santiago, Chile. 
A simple but effective approach to building page replacement.

## [G+17] KASLR is Dead: Long Live KASLR
D. Gruss, M. Lipp, M. Schwarz, R. Fellner, C. Maurice, S. Mangard. Engineering Secure Software and Systems, 2017. Available: https://gruss.cc/files/kaiser.pdf 
Excellent info on KASLR, KPTI, and beyond.

## [G04] Understanding the Linux Virtual Memory Manager
M. Gorman. Prentice Hall, 2004. 
An in-depth look at Linux VM, but alas a little out of date.

## [C93] Inside Windows NT
H. Custer, D. Solomon. Microsoft Press, 1993. 
The book about Windows NT that explains the system top to bottom, in more detail than you might like. But seriously, a pretty good book.

## [C03] The Innovator’s Dilemma
Clayton M. Christenson. Harper Paperbacks, January 2003. 
A fantastic book about the disk-drive industry and how new innovations disrupt existing ones. A good read for business majors and computer scientists alike. Provides insight on how large and successful companies completely fail.

## [BC05] Understanding the Linux Kernel
D. P. Bovet, M. Cesati. O’Reilly Media, November 2005. 
One of the many books you can ﬁnd on Linux, which are out of date, but still worthwhile.

## [BJ81] Converting a Swap-Based System to do Paging in an Architecture Lacking Page-Reference Bits
O. Babaoglu, W. N. Joy. SOSP ’81, Paciﬁc Grove, California, December 1981. 
How to exploit existing protection machinery to emulate reference bits, from a group at Berkeley working on their own version of UNIX: the Berkeley Systems Distribution (BSD). The group was inﬂuential in the development of virtual memory, ﬁle systems, and networking.

## [BB+72] TENEX, A Paged Time Sharing System for the PDP-10
D. G. Bobrow, J. D. Burchﬁel, D. L. Murphy, R. S. Tomlinson. CACM, Volume 15, March 1972. 
An early time-sharing OS where a number of good ideas came from. Copy-on-write was just one of those; also an inspiration for other aspects of modern systems, including process management, virtual memory, and ﬁle systems.

## [S07] The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)
H. Shacham. CCS ’07, October 2007. 
A generalization of return-to-libc. Dr. Beth Garner said in Basic Instinct, She’s crazy! She’s brilliant!” We might say the same about ROP.

## [RL81] Segmented FIFO Page Replacement
R. Turner, H. Levy. SIGMETRICS ’81, Las Vegas, Nevada, September 1981. 
A short paper that shows for some workloads, segmented FIFO can approach the performance of LRU.

# Chapter 26: Concurrency and Threads

## [D68] Cooperating sequential processes
Edsger W. Dijkstra. 1968. Available at this site: http://www.cs.utexas.edu/users/EWD/ewd01xx/EWD123.PDF. 
Dijkstra has an amazing number of his old papers, notes, and thoughts recorded (for posterity) on this website at the last place he worked, the University of Texas. Much of his foundational work, however, was done years earlier while he was at the Technische Hochshule of Eindhoven (THE), including this famous paper on "cooperating sequential processes”, which basically outlines all of the thinking that has to go into writing multi-threaded programs. Dijkstra discovered much of this while working on an operating system named after his school: the "THE" operating system (said "T", "H", "E", and not like the word "the”).

## [NM92] What Are Race Conditions? Some Issues and Formalizations
Robert H. B. Netzer and Barton P. Miller. ACM Letters on Programming Languages and Systems, Volume 1:1, March 1992. 
An excellent discussion of the different types of races found in concurrent programs. In this chapter (and the next few), we focus on data races, but later we will broaden to discuss general races as well.

## [L+93] Atomic Transactions
Nancy Lynch, Michael Merritt, William Weihl, Alan Fekete. Morgan Kaufmann, August 1993.
A nice text on some of the theory and practice of atomic transactions for distributed systems. Perhaps a bit formal for some, but lots of good material is found herein.

## [GR92] Transaction Processing: Concepts and Techniques
Jim Gray and Andreas Reuter. Morgan Kaufmann, September 1992. 
This book is the bible of transaction processing, written by one of the legends of the ﬁeld, Jim Gray. It is, for this reason, also considered Jim Gray’s brain dump”, in which he wrote down everything he knows about how database management systems work. Sadly, Gray passed away tragically a few years back, and many of us lost a friend and great mentor, including the co-authors of said book, who were lucky enough to interact with Gray during their graduate school years.

## [D65] Solution of a problem in concurrent programming control
E. W. Dijkstra. Communications of the ACM, 8(9):569, September 1965. 
Pointed to as the ﬁrst paper of Dijkstra’s where he outlines the mutual exclusion problem and a solution. The solution, however, is not widely used; advanced hardware and OS support is needed, as we will see in the coming chapters.

## [SR05] Advanced Programming in the U NIX Environment
W. Richard Stevens and Stephen A. Rago. Addison-Wesley, 2005. 
As we’ve said many times, buy this book, and read it, in little chunks, preferably before going to bed. This way, you will actually fall asleep more quickly; more importantly, you learn a little more about how to become a serious U NIX programmer.

# Chapter 27: Thread API

## [B97] Programming with POSIX Threads
David R. Butenhof. Addison-Wesley, May 1997. 
Another one of these books on threads.

## [X+10] Ad Hoc Synchronization Considered Harmful
Weiwei Xiong, Soyeon Park, Jiaqi Zhang, Yuanyuan Zhou, Zhiqiang Ma. OSDI 2010, Vancouver, Canada. 
This paper shows how seemingly simple synchronization code can lead to a surprising number of bugs. Use condition variables and do the signaling correctly!

## [K+96] Programming With Threads
Steve Kleiman, Devang Shah, Bart Smaalders. Prentice Hall, January 1996. 
Probably one of the better books in this space. Get it at your local library. Or steal it from your mother. More seriously, just ask your mother for it – she’ll let you borrow it, don’t worry.

## [B+96] PThreads Programming: by A POSIX Standard for Better Multiprocessing.
Dick Buttlar, Jacqueline Farrell, Bradford Nichols. O’Reilly, September 1996 
A reasonable book from the excellent, practical publishing house O’Reilly. Our bookshelves certainly contain a great deal of books from this company, including some excellent offerings on Perl, Python, and Javascript (particularly Crockford’s Javascript: The Good Parts”.)

## [B89] An Introduction to Programming with Threads
Andrew D. Birrell. DEC Technical Report, January, 1989. Available: https://birrell.org/andrew/papers/035-Threads.pdf 
A classic but older introduction to threaded programming. Still a worthwhile read, and freely available.

# Chapter 28: Locks

## [WG00] The SPARC Architecture Manual: Version 9
D. Weaver, T. Germond. SPARC International, 2000. http://www.sparc.org/standards/SPARCV9.pdf. 
See developers. sun.com/solaris/articles/atomic sparc/ for more on atomics.

## [W09] Load-Link, Store-Conditional
Many authors.. en.wikipedia.org/wiki/LoadLink/Store-Conditional. 
Can you believe we referenced Wikipedia? But, we found the information there and it felt wrong not to. Further, it was useful, listing the instructions for the different architectures: ldl l/stl c and ldq l/stq c (Alpha), lwarx/stwcx (PowerPC), ll/sc (MIPS), and ldrex/strex (ARM). Actually Wikipedia is pretty amazing, so don’t be so harsh, OK?

## [H91] Wait-free Synchronization
Maurice Herlihy. ACM TOPLAS, Volume 13: 1, January 1991. 
A landmark paper introducing a different approach to building concurrent data structures. Because of the complexity involved, some of these ideas have been slow to gain acceptance in deployment.

## [D91] Just Win, Baby: Al Davis and His Raiders
Glenn Dickey. Harcourt, 1991. 
The book about Al Davis and his famous quote. Or, we suppose, the book is more about Al Davis and the Raiders, and not so much the quote. To be clear: we are not recommending this book, we just needed a citation.

## [D+13] Everything You Always Wanted to Know about Synchronization but Were Afraid to Ask
Tudor David, Rachid Guerraoui, Vasileios Trigonakis. SOSP ’13, Nemacolin Woodlands Resort, Pennsylvania, November 2013. 
An excellent paper comparing many different ways to build locks using hardware primitives. Great to see how many ideas work on modern hardware.

## [D68] Cooperating sequential processes
Edsger W. Dijkstra. 1968. Available online here: http://www.cs.utexas.edu/users/EWD/ewd01xx/EWD123.PDF. 
One of the early seminal papers. Discusses how Dijkstra posed the original concurrency problem, and Dekker’s solution.

## [H93] MIPS R4000 Microprocessor User’s Manual
Joe Heinrich. Prentice-Hall, June 1993. Available: http://cag.csail.mit.edu/raw/documents/R4400 Uman book Ed2.pdf. 
The old MIPS user’s manual. Download it while it still exists.

## [L09] glibc 2.9 (include Linux pthreads implementation)
Many authors.. Available here: http://ftp.gnu.org/gnu/glibc. 
In particular, take a look at the nptl subdirectory where you will ﬁnd most of the pthread support in Linux today.

## [M82] The Architecture of the Burroughs B5000: 20 Years Later and Still Ahead of the Times?
A. Mayer. 1982. Available: www.ajwm.net/amayer/papers/B5000.html.
It (RDLK) is an indivisible operation which reads from and writes into a memory location.” RDLK is thus testand-set! Dave Dahm created spin locks (“Buzz Locks”) and a two-phase lock called Dahm Locks.”

## [L81] Observations on the Development of an Operating System
Hugh Lauer. SOSP ’81, Paciﬁc Grove, California, December 1981. 
A must-read retrospective about the development of the Pilot OS, an early PC operating system. Fun and full of insights.

## [S05] Guide to porting from Solaris to Linux on x86
Ajay Sood, April 29, 2005. Available: http://www.ibm.com/developerworks/linux/library/l-solar/.


## [MS91] Algorithms for Scalable Synchronization on Shared-Memory Multiprocessors
John M. Mellor-Crummey and M. L. Scott. ACM TOCS, Volume 9, Issue 1, February 1991. 
An excellent and thorough survey on different locking algorithms. However, no operating systems support is used, just fancy hardware instructions.

## [S09] OpenSolaris Thread Library
Sun.. Code: src.opensolaris.org/source/xref/ onnv/onnv-gate/usr/src/lib/libc/port/threads/synch.c. 
Pretty interesting, although who knows what will happen now that Oracle owns Sun. Thanks to Mike Swift for the pointer.

## [M15] OSSpinLock Is Unsafe
J. McCall. mjtsai.com/blog/2015/12/16/osspinlock -is-unsafe. 
Calling OSSpinLock on a Mac is unsafe when using threads of different priorities – you might spin forever! So be careful, Mac fanatics, even your mighty system can be less than perfect...

## [P81] Myths About the Mutual Exclusion Problem
G.L. Peterson. Information Processing Letters, 12(3), pages 115–116, 1981. 
Peterson’s algorithm introduced here.

## [R97] What Really Happened on Mars?
Glenn E. Reeves. research.microsoft.com/en-us/um/people/mbj/Mars Pathfinder/Authoritative Account.html. 
A description of priority inversion on Mars Pathﬁnder. Concurrent code correctness matters, especially in space!

# Chapter 29: Locked Data Structures

## [B+10] An Analysis of Linux Scalability to Many Cores
Silas Boyd-Wickizer, Austin T. Clements, Yandong Mao, Aleksey Pesterev, M. Frans Kaashoek, Robert Morris, Nickolai Zeldovich . OSDI ’10, Vancouver, Canada, October 2010. 
A great study of how Linux performs on multicore machines, as well as some simple solutions. Includes a neat sloppy counter to solve one form of the scalable counting problem.

## [MS98] Nonblocking Algorithms and Preemption-safe Locking on by Multiprogrammed Shared-memory Multiprocessors.
M. Michael, M. Scott. Journal of Parallel and Distributed Computing, Vol. 51, No. 1, 1998 
Professor Scott and his students have been at the forefront of concurrent algorithms and data structures for many years; check out his web page, numerous papers, or books to ﬁnd out more.

## [MS04] Concurrent Data Structures
Mark Moir and Nir Shavit. In Handbook of Data Structures and Applications (Editors D. Metha and S.Sahni). Chapman and Hall/CRC Press, 2004. Available: www.cs.tau.ac.il/˜shanir/concurrent-data-structures.pdf. 
A short but relatively comprehensive reference on concurrent data structures. Though it is missing some of the latest works in the area (due to its age), it remains an incredibly useful reference.

## [MM00] Solaris Internals: Core Kernel Architecture
Jim Mauro and Richard McDougall. Prentice Hall, October 2000. 
The Solaris book. You should also read this, if you want to learn about something other than Linux.

## [S+11] Making the Common Case the Only Case with Anticipatory Memory Allocation
Swaminathan Sundararaman, Yupu Zhang, Sriram Subramanian, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau . FAST ’11, San Jose, CA, February 2011.
Our work on removing possibly-failing allocation calls from kernel code paths. By allocating all potentially needed memory before doing any work, we avoid failure deep down in the storage stack.

## [BH73] Operating System Principles
Per Brinch Hansen. Prentice-Hall, 1973. Available: http://portal.acm.org/citation.cfm?id=540365. 
One of the ﬁrst books on operating systems; certainly ahead of its time. Introduced monitors as a concurrency primitive.

## [L+13] A Study of Linux File System Evolution
Lanyue Lu, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau, Shan Lu. FAST ’13, San Jose, CA, February 2013. 
Our paper that studies every patch to Linux ﬁle systems over nearly a decade. Lots of fun ﬁndings in there; read it to see! The work was painful to do though; the poor graduate student, Lanyue Lu, had to look through every single patch by hand in order to understand what they did.

## [C06] The Search For Fast, Scalable Counters
Jonathan Corbet. February 1, 2006. Available: https://lwn.net/Articles/170003. 
LWN has many wonderful articles about the latest in Linux This article is a short description of scalable approximate counting; read it, and others, to learn more about the latest in Linux.

## [BC05] Understanding the Linux Kernel (Third Edition)
Daniel P. Bovet and Marco Cesati. O’Reilly Media, November 2005. 
The classic book on the Linux kernel. You should read it.

# Chapter 30: Condition Variables

## [D72] Information Streams Sharing a Finite Buffer
E.W. Dijkstra. Information Processing Letters 1: 179180, 1972. Available: http://www.cs.utexas.edu/users/EWD/ewd03xx/EWD329.PDF 
The famous paper that introduced the producer/consumer problem.

## [LR80] Experience with Processes and Monitors in Mesa
B.W. Lampson, D.R. Redell. Communications of the ACM. 23:2, pages 105-117, February 1980. 
A terriﬁc paper about how to actually implement signaling and condition variables in a real system, leading to the term "Mesa" semantics for what it mzshortns to be woken up; the older semantics, developed by Tony Hoare [H74], then became known as "Hoare" semantics, which is hard to say out loud in class with a straight face.

## [O49] 1984
George Orwell. Secker and Warburg, 1949. 
A little heavy-handed, but of course a must read. That said, we kind of gave away the ending by quoting the last sentence. Sorry! And if the government is reading this, let us just say that we think that the government is "double plus good”. Hear that, our pals at the NSA?

## [L11] Pthread cond signal Man Page
Mysterious author. March, 2011. Available online: http://linux.die.net/man/3/pthread cond signal. 
The Linux man page shows a nice simple example of why a thread might get a spurious wakeup, due to race conditions within the signal/wakeup code.

## [H74] Monitors: An Operating System Structuring Concept
C.A.R. Hoare. Communications of the ACM, 17:10, pages 549–557, October 1974. 
Hoare did a fair amount of theoretical work in concurrency. However, he is still probably most known for his work on Quicksort, the coolest sorting algorithm in the world, at least according to these authors.

## [D01] My recollections of operating system design
E.W. Dijkstra. April, 2001. Available: http://www.cs.utexas.edu/users/EWD/ewd13xx/EWD1303.PDF. 
A fascinating read for those of you interested in how the pioneers of our ﬁeld came up with some very basic and fundamental concepts, including ideas like "interrupts" and even a stack”!

## [D68] Cooperating sequential processes
Edsger W. Dijkstra. 1968. Available online here: http://www.cs.utexas.edu/users/EWD/ewd01xx/EWD123.PDF. 
Another classic from Dijkstra; reading his early works on concurrency will teach you much of what you need to know.

# Chapter 31: Semaphores

## [T99] Re: NT kernel guy playing with Linux
Linus Torvalds. June 27, 1999. Available: https://yarchive.net/comp/linux/semaphores.html. 
A response from Linus himself about the utility of semaphores, including the throttling case we mention in the text. As always, Linus is slightly insulting but quite informative.

## [GR92] Transaction Processing: Concepts and Techniques
Jim Gray, Andreas Reuter. Morgan Kaufmann, September 1992. 
The exact quote that we ﬁnd particularly humorous is found on page 485, at the top of Section 8.8: The ﬁrst multiprocessors, circa 1960, had test and set instructions ... presumably the OS implementors worked out the appropriate algorithms, although Dijkstra is generally credited with inventing semaphores many years later.” Oh, snap!

## [L83] Hints for Computer Systems Design
Butler Lampson. ACM Operating Systems Review, 15:5, October 1983. 
Lampson, a famous systems researcher, loved using hints in the design of computer systems. A hint is something that is often correct but can be wrong; in this use, a signal() is telling a waiting thread that it changed the condition that the waiter was waiting on, but not to trust that the condition will be in the desired state when the waiting thread wakes up. In this paper about hints for designing systems, one of Lampson’s general hints is that you should use hints. It is not as confusing as it sounds.

## [H87] Aspects of Cache Memory and Instruction Buffer Performance
Mark D. Hill. Ph.D. Dissertation, U.C. Berkeley, 1987. 
Hill’s dissertation work, for those obsessed with caching in early systems. A great example of a quantitative dissertation.

## [CHP71] Concurrent Control with Readers and Writers
P.J. Courtois, F. Heymans, D.L. Parnas. Communications of the ACM, 14:10, October 1971. 
The introduction of the reader-writer problem, and a simple solution. Later work introduced more complex solutions, skipped here because, well, they are pretty complex.

## [D71] Hierarchical ordering of sequential processes
E.W. Dijkstra. Available online here: http://www.cs.utexas.edu/users/EWD/ewd03xx/EWD310.PDF. 
Presents numerous concurrency problems, including Dining Philosophers. The wikipedia page about this problem is also useful.

## [D08] The Little Book of Semaphores
A.B. Downey. Available at the following site: http://greenteapress.com/semaphores/. 
A nice (and free!) book about semaphores. Lots of fun problems to solve, if you like that sort of thing.

## [D72] Information Streams Sharing a Finite Buffer
E.W. Dijkstra. Information Processing Letters 1, 1972. http://www.cs.utexas.edu/users/EWD/ewd03xx/EWD329.PDF. 
Did Dijkstra invent everything? No, but maybe close. He certainly was the ﬁrst to clearly write down what the problems were in concurrent code. However, practitioners in OS design knew of many of the problems described by Dijkstra, so perhaps giving him too much credit would be a misrepresentation.

## [D68b] The Structure of the THE Multiprogramming System
E.W. Dijkstra. CACM, volume 11(5), 1968. 
One of the earliest papers to point out that systems work in computer science is an engaging intellectual endeavor. Also argues strongly for modularity in the form of layered systems.

## [D68a] Go-to Statement Considered Harmful
E.W. Dijkstra. CACM, volume 11(3), March 1968. http://www.cs.utexas.edu/users/EWD/ewd02xx/EWD215.PDF. 
Sometimes thought of as the beginning of the ﬁeld of software engineering.

## [D59] A Note on Two Problems in Connexion with Graphs
E. W. Dijkstra. Numerische Mathematik 1, 269–271, 1959. Available: http://www-m3.ma.tum.de/twiki/pub/MN0506/ WebHome/dijkstra.pdf. 
Can you believe people worked on algorithms in 1959? We can’t. Even before computers were any fun to use, these people had a sense that they would transform the world...

## [CB08] Real-world Concurrency
Bryan Cantrill, Jeff Bonwick. ACM Queue. Volume 6, No. 5. September 2008. 
A nice article by some kernel hackers from a company formerly known as Sun on the real problems faced in concurrent code.

## [B04] Implementing Condition Variables with Semaphores
Andrew Birrell. December 2004. 
An interesting read on how difﬁcult implementing CVs on top of semaphores really is, and the mistakes the author and co-workers made along the way. Particularly relevant because the group had done a ton of concurrent programming; Birrell, for example, is known for (among other things) writing various thread-programming guides.

# Chapter 32: Concurrency Bugs

## [L+08] Learning from Mistakes — A Comprehensive Study on Real World Concurrency Bug Characteristics
Shan Lu, Soyeon Park, Eunsoo Seo, Yuanyuan Zhou. ASPLOS ’08, March 2008, Seattle, Washington. 
The ﬁrst in-depth study of concurrency bugs in real software, and the basis for this chapter. Look at Y.Y. Zhou’s or Shan Lu’s web pages for many more interesting papers on bugs.

## [B+87] Concurrency Control and Recovery in Database Systems
Philip A. Bernstein, Vassos Hadzilacos, Nathan Goodman. Addison-Wesley, 1987. 
The classic text on concurrency in database management systems. As you can tell, understanding concurrency, deadlock, and other topics in the world of databases is a world unto itself. Study it and ﬁnd out for yourself.

## [C+71] System Deadlocks
E.G. Coffman, M.J. Elphick, A. Shoshani. ACM Computing Surveys, 3:2, June 1971. 
The classic paper outlining the conditions for deadlock and how you might go about dealing with it. There are certainly some earlier papers on this topic; see the references within this paper for details.

## [D64] Een algorithme ter voorkoming van de dodelijke omarming
Edsger Dijkstra. 1964. Available: http://www.cs.utexas.edu/users/EWD/ewd01xx/EWD108.PDF. 
Indeed, not only did Dijkstra come up with a number of solutions to the deadlock problem, he was the ﬁrst to note its existence, at least in written form. However, he called it the "deadly embrace”, which (thankfully) did not catch on.

## [GD02] MapReduce: Simpliﬁed Data Processing on Large Clusters
Sanjay Ghemawhat, Jeff Dean. OSDI ’04, San Francisco, CA, October 2004. 
The MapReduce paper ushered in the era of large-scale data processing, and proposes a framework for performing such computations on clusters of generally unreliable machines.

## [H93] A Methodology for Implementing Highly Concurrent Data Objects
Maurice Herlihy. ACM TOPLAS, 15:5, November 1993. 
A nice overview of lock-free and wait-free structures. Both approaches eschew locks, but wait-free approaches are harder to realize, as they try to ensure than any operation on a concurrent structure will terminate in a ﬁnite number of steps (e.g., no unbounded looping).

## [K81] Soul of a New Machine
Tracy Kidder. Backbay Books, 2000 (reprint of 1980 ver-sion). 
A must-read for any systems builder or engineer, detailing the early days of how a team inside Data General (DG), led by Tom West, worked to produce a "new machine.” Kidder’s other books are also excellent, including "Mountains beyond Mountains.” Or maybe you don’t agree with us, comma?

## [J+08] Deadlock Immunity: Enabling Systems To Defend Against Deadlocks
Horatiu Jula, Daniel Tralamazza, Cristian Zamﬁr, George Candea. OSDI ’08, San Diego, CA, December 2008. 
An excellent recent paper on deadlocks and how to avoid getting caught in the same ones over and over again in a particular system.

## [H01] A Pragmatic Implementation of Non-blocking Linked-lists
Tim Harris. International Conference on Distributed Computing (DISC), 2001. 
A relatively modern example of the difﬁculties of building something as simple as a concurrent linked list without locks.

## [H91] Wait-free Synchronization
Maurice Herlihy . ACM TOPLAS, 13:1, January 1991. 
Herlihy’s work pioneers the ideas behind wait-free approaches to writing concurrent programs. These approaches tend to be complex and hard, often more difﬁcult than using locks correctly, probably limiting their success in the real world.

## [K87] Deadlock Detection in Distributed Databases
Edgar Knapp. ACM Computing Surveys, 19:4, December 1987. 
An excellent overview of deadlock detection in distributed database systems. Also points to a number of other related works, and thus is a good place to start your reading.

## [T+94] Linux File Memory Map Code
Linus Torvalds and many others. Available online at: http://lxr.free-electrons.com/source/mm/filemap.c. 
Thanks to Michael Walﬁsh (NYU) for pointing out this precious example. The real world, as you can see in this ﬁle, can be a bit more complex than the simple clarity found in textbooks...

# Chapter 33: Event-based Concurrency

## [A+02] Cooperative Task Management Without Manual Stack Management
Atul Adya, Jon Howell, Marvin Theimer, William J. Bolosky, John R. Douceur. USENIX ATC ’02, Monterey, CA, June 2002. 
This gem of a paper is the ﬁrst to clearly articulate some of the difﬁculties of event-based concurrency, and suggests some simple solutions, as well explores the even crazier idea of combining the two types of concurrency management into a single application!

## [O96] Why Threads Are A Bad Idea (for most purposes)
John Ousterhout. Invited Talk at USENIX ’96, San Diego, CA, January 1996. 
A great talk about how threads aren’t a great match for GUI-based applications (but the ideas are more general). Ousterhout formed many of these opinions while he was developing Tcl/Tk, a cool scripting language and toolkit that made it 100x easier to develop GUI-based applications than the state of the art at the time. While the Tk GUI toolkit lives on (in Python for example), Tcl seems to be slowly dying (unfortunately).

## [FHK84] Programming With Continuations
Daniel P. Friedman, Christopher T. Haynes, Eugene E. Kohlbecker. In Program Transformation and Programming Environments, Springer Verlag, 1984. 
The classic reference to this old idea from the world of programming languages. Now increasingly popular in some modern languages.

## [N13] Node.js Documentation
the folks who built node.js. Available: nodejs.org/api. 
One of the many cool new frameworks that help you readily build web services and applications. Every modern systems hacker should be proﬁcient in frameworks such as this one (and likely, more than one). Spend the time and do some development in one of these worlds and become an expert.

## [SR05] Advanced Programming in the U NIX Environment
W. Richard Stevens and Stephen A. Rago. Addison-Wesley, 2005. 
Once again, we refer to the classic must-have-on-your-bookshelf book of U NIX systems programming. If there is some detail you need to know, it is in here.

## [vB+03] Capriccio: Scalable Threads for Internet Services
Rob von Behren, Jeremy Condit, Feng Zhou, George C. Necula, Eric Brewer. SOSP ’03, Lake George, New York, October 2003. 
A paper about how to make threads work at extreme scale; a counter to all the event-based work ongoing at the time.

## [WCB01] SEDA: An Architecture for Well-Conditioned, Scalable Internet Services
Matt Welsh, David Culler, and Eric Brewer. SOSP ’01, Banff, Canada, October 2001.
A nice twist on event-based serving that combines threads, queues, and event-based handling into one streamlined whole. Some of these ideas have found their way into the infrastructures of companies such as Google, Amazon, and elsewhere.

## [PDZ99] Flash: An Efﬁcient and Portable Web Server
Vivek S. Pai, Peter Druschel, Willy Zwaenepoel. USENIX ’99, Monterey, CA, June 1999. 
A pioneering paper on how to structure web servers in the then-burgeoning Internet era. Read it to understand the basics as well as to see the authors’ ideas on how to build hybrids when support for asynchronous I/O is lacking.

# Chapter 36: I-O Devices

## [A+11] vIC: Interrupt Coalescing for Virtual Machine Storage Device IO
Irfan Ahmad, Ajay Gulati, Ali Mashtizadeh. USENIX ’11. 
A terriﬁc survey of interrupt coalescing in traditional and virtualized environments.

## [AD14] Operating Systems: Three Easy Pieces (Chapters: Crash Consistency: FSCK and Journaling and Log-Structured File Systems) 
Remzi Arpaci-Dusseau and Andrea ArpaciDusseau. Arpaci-Dusseau Books, 2014. 
A description of a ﬁle-system checker and how it works, which requires low-level access to disk devices not normally provided by the ﬁle system directly.

## [CK+08] The xv6 Operating System
Russ Cox, Frans Kaashoek, Robert Morris, Nickolai Zeldovich. From: http://pdos.csail.mit.edu/6.828/2008/index.html. 
See ide.c for the IDE device driver, with a few more details therein.

## [D07] What Every Programmer Should Know About Memory
Ulrich Drepper. November, 2007. Available: http://www.akkadia.org/drepper/cpumemory.pdf. 
A fantastic read about modern memory systems, starting at DRAM and going all the way up to virtualization and cache-optimized algorithms.

## [C01] An Empirical Study of Operating System Errors
Andy Chou, Junfeng Yang, Benjamin Chelf, Seth Hallem, Dawson Engler. SOSP ’01. 
One of the ﬁrst papers to systematically explore how many bugs are in modern operating systems. Among other neat ﬁndings, the authors show that device drivers have something like seven times more bugs than mainline kernel code.

## [H18] Hacker News
Many contributors. Available: https://news.ycombinator.com. One of the better aggregrators for tech-related stuff. 
Once back in 2014, this book became a highly-ranked entry, leading to 1 million chapter downloads in just one day! Sadly, we have yet to re-experience such a high.

## [L94] AT Attachment Interface for Disk Drives
Lawrence J. Lamers. Reference number: ANSI X3.221, 1994. Available: ftp://ftp.t10.org/t13/project/d0791r4c-ATA-1.pdf. 
A rather dry document about device interfaces. Read it at your own peril.

## [MR96] Eliminating Receive Livelock in an Interrupt-driven Kernel
Jeffrey Mogul, K. K. Ramakrishnan. USENIX ’96, San Diego, CA, January 1996. 
Mogul and colleagues did a great deal of pioneering work on web server network performance. This paper is but one example.

## [S08] Interrupts
Mark Smotherman. July ’08. Available: http://people.cs.clemson.edu/ ˜mark/interrupts.html. 
A treasure trove of information on the history of interrupts, DMA, and related early ideas in computing.

## [S03] Improving the Reliability of Commodity Operating Systems
Michael M. Swift, Brian N. Bershad, Henry M. Levy. SOSP ’03. 
Swift’s work revived interest in a more microkernel-like approach to operating systems; minimally, it ﬁnally gave some good reasons why address-space based protection could be useful in a modern OS.

## [W10] Hard Disk Driver
Washington State Course Homepage. Available online at this site: http://eecs.wsu.edu/˜cs460/cs560/HDdriver.html. 
A nice summary of a simple IDE disk drive’s interface and how to build a device driver for it.

## [G08] EIO: Error-handling is Occasionally Correct
Haryadi Gunawi, Cindy Rubio-Gonzalez, Andrea Arpaci-Dusseau, Remzi Arpaci-Dusseau, Ben Liblit. FAST ’08, San Jose, CA, February 2008. 
Our own work on building a tool to ﬁnd code in Linux ﬁle systems that does not handle error return properly. We found hundreds and hundreds of bugs, many of which have now been ﬁxed.

## [H17] Intel Core i7-7700K review: Kaby Lake Debuts for Desktop
Joel Hruska. January 3, 2017. www.extremetech.com/extreme/241950-intels-core-i7-7700k-reviewed-kaby -lake-debuts-desktop. 
An in-depth review of a recent Intel chipset, including CPUs and the I/O subsystem.

# Chapter 37: Hard Disk Drives

## [SCO90] Disk Scheduling Revisited
Margo Seltzer, Peter Chen, John Ousterhout. USENIX 1990. 
A paper that talks about how rotation matters too in the world of disk scheduling.

## [RW92] An Introduction to Disk Drive Modeling
C. Ruemmler, J. Wilkes. IEEE Computer, 27:3, March 1994. 
A terriﬁc introduction to the basics of disk operation. Some pieces are out of date, but most of the basics remain.

## [ADR03] More Than an Interface: SCSI vs. ATA
Dave Anderson, Jim Dykes, Erik Riedel. FAST ’03, 2003. 
One of the best recent-ish references on how modern disk drives really work; a must read for anyone interested in knowing more.

## [CKR72] Analysis of Scanning Policies for Reducing Disk Seek Times
 E.G. Coffman, L.A. Klimko, B. Ryan SIAM Journal of Computing, September 1972, Vol 1. No 3. 
Some of the early work in the ﬁeld of disk scheduling.

## [HK+17] The Unwritten Contract of Solid State Drives
Jun He, Sudarsun Kannan, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. EuroSys ’17, Belgrade, Serbia, April 2017. 
We take the idea of the unwritten contract, and extend it to SSDs. Using SSDs well seems as complicated than hard drives, and sometimes more so.

## [S09b] Cheetah 15K.5
Seagate, Inc.. Available at this website, we’re pretty sure it is: http://www.seagate.com/docs/pdf/datasheet/disc/ds-cheetah-15k-5-us.pdf. 
See above commentary on data sheets.

## [SG04] MEMS-based storage devices and standard disk interfaces: A square peg in a round hole?
 Steven W. Schlosser, Gregory R. Ganger FAST ’04, pp. 87-100, 2004 
While the MEMS aspect of this paper hasn’t yet made an impact, the discussion of the contract between ﬁle systems and disks is wonderful and a lasting contribution. We later build on this work to study the Unwritten Contract of Solid State Drives” [HK+17]

## [ID01] Anticipatory Scheduling: A Disk-scheduling Framework To Overcome Deceptive Idleness In Synchronous I/O
Sitaram Iyer, Peter Druschel. SOSP ’01, October 2001. 
A cool paper showing how waiting can improve disk scheduling: better requests may be on their way!

## [JW91] Disk Scheduling Algorithms Based On Rotational Position
D. Jacobson, J. Wilkes. Technical Report HPL-CSP-91-7rev1, Hewlett-Packard, February 1991. 
A more modern take on disk scheduling. It remains a technical report (and not a published paper) because the authors were scooped by Seltzer et al. [S90].

## [S09a] Barracuda ES.2 data sheet
Seagate, Inc.. Available at this website, at least, it was: http://www.seagate.com/docs/pdf/datasheet/disc/ds_barracuda_es.pdf. 
A data sheet; read at your own risk. Risk of what? Boredom.

# Chapter 38: Redundant Disk Arrays (RAID)

## [DAA05] Journal-guided Resynchronization for Software RAID
Timothy E. Denehy, A. Arpaci-Dusseau, R. Arpaci-Dusseau. FAST 2005. 
Our own work on the consistent-update problem. Here we solve it for Software RAID by integrating the journaling machinery of the ﬁle system above with the software RAID beneath it.

## [SG86] Disk Striping
K. Salem, H. Garcia-Molina. IEEE International Conference on Data Engineering, 1986. 
And yes, another early RAID work. There are a lot of these, which kind of came out of the woodwork when the RAID paper was published in SIGMOD.

## [PB86] Providing Fault Tolerance in Parallel Secondary Storage Systems
A. Park, K. Balasubramaniam. Department of Computer Science, Princeton, CS-TR-O57-86, November 1986. 
Another early work on RAID.

## [P+88] Redundant Arrays of Inexpensive Disks
D. Patterson, G. Gibson, R. Katz. SIGMOD 1988. This is considered the RAID paper, written by famous authors Patterson, Gibson, and Katz. 
The paper has since won many test-of-time awards and ushered in the RAID era, including the name RAID itself!

## [K88] Small Disk Arrays – The Emerging Approach to High Performance
F. Kurzweil. Presentation at Spring COMPCON ’88, March 1, 1988, San Francisco, California. 
Another early RAID reference.

## [K86] Synchronized Disk Interleaving
M.Y. Kim. IEEE Transactions on Computers, Volume C-35: 11, November 1986. 
Some of the earliest work on RAID is found here.

## [HLM94] File System Design for an NFS File Server Appliance
Dave Hitz, James Lau, Michael Malcolm. USENIX Winter 1994, San Francisco, California, 1994. 
The sparse paper introducing a landmark product in storage, the write-anywhere ﬁle layout or WAFL ﬁle system that underlies the NetApp ﬁle server.

## [C+04] Row-Diagonal Parity for Double Disk Failure Correction
P. Corbett, B. English, A. Goel, T. Grcanac, S. Kleiman, J. Leong, S. Sankar. FAST ’04, February 2004. 
Though not the ﬁrst paper on a RAID system with two disks for parity, it is a recent and highly-understandable version of said idea. Read it to learn more.

## [CL95] Striping in a RAID level 5 disk array
Peter M. Chen and Edward K. Lee. SIGMETRICS 1995. 
A nice analysis of some of the important parameters in a RAID-5 disk array.

## [BJ88] Disk Shadowing
D. Bitton and J. Gray. VLDB 1988. 
One of the ﬁrst papers to discuss mirroring, therein called "shadowing”.

## [B+08] An Analysis of Data Corruption in the Storage Stack
Lakshmi N. Bairavasundaram, Garth R. Goodson, Bianca Schroeder, Andrea C. Arpaci-Dusseau, Remzi H. ArpaciDusseau. FAST ’08, San Jose, CA, February 2008. 
Our own work analyzing how often disks actually corrupt your data. Not often, but sometimes! And thus something a reliable storage system must consider.

## [S84] Byzantine Generals in Action: Implementing Fail-Stop Processors
F.B. Schneider. ACM Transactions on Computer Systems, 2(2):145154, May 1984. 
Finally, a paper that is not about RAID! This paper is actually about how systems fail, and how to make something behave in a fail-stop manner.

# Chapter 39: Files and Directories

## [P+13] Towards Efﬁcient, Portable Application-Level Consistency
Thanumalayan S. Pillai, Vijay Chidambaram, Joo-Young Hwang, Andrea C. Arpaci-Dusseau, and Remzi H. ArpaciDusseau. HotDep ’13, November 2013. 
Our own work that shows how readily applications can make mistakes in committing data to disk; in particular, assumptions about the ﬁle system creep into applications and thus make the applications work correctly only if they are running on a speciﬁc ﬁle system.

## [H+18] TxFS: Leveraging File-System Crash Consistency to Provide ACID Transactions
Y. Hu, Z. Zhu, I. Neal, Y. Kwon, T. Cheng, V. Chidambaram, E. Witchel. USENIX ATC ’18, June 2018. 
The best paper at USENIX ATC ’18, and a good recent place to start to learn about transactional ﬁle systems.

## [CK+08] The xv6 Operating System
Russ Cox, Frans Kaashoek, Robert Morris, Nickolai Zeldovich. From: https://github.com/mit-pdos/xv6-public. 
As mentioned before, a cool and simple Unix implementation. We have been using an older version (2012-01-30-1-g1c41342) and hence some examples in the book may not match the latest in the source.

## [P+14] All File Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent Applications
Thanumalayan S. Pillai, Vijay Chidambaram, Ramnatthan Alagappan, Samer Al-Kiswany, Andrea C. Arpaci-Dusseau, and Remzi H. Arpaci-Dusseau. OSDI ’14, Broomﬁeld, Colorado, October 2014. 
The full conference paper on this topic – with many more details and interesting tidbits than the ﬁrst workshop paper above.

## [SK09] Principles of Computer System Design
Jerome H. Saltzer and M. Frans Kaashoek. Morgan-Kaufmann, 2009. 
This tour de force of systems is a must-read for anybody interested in the ﬁeld. It’s how they teach systems at MIT. Read it once, and then read it a few more times to let it all soak in.

## [T+08] Portably Solving File TOCTTOU Races with Hardness Ampliﬁcation
D. Tsafrir, T. Hertz, D. Wagner, D. Da Silva. FAST ’08, San Jose, California, 2008. 
Not the paper that introduced TOCTTOU, but a recent-ish and well-done description of the problem and a way to solve the problem in a portable manner.

## [L84] Capability-Based Computer Systems
Henry M. Levy. Digital Press, 1984. Available: http://homes.cs.washington.edu/˜levy/capabook. 
An excellent overview of early capability-based systems.

## [K84] Processes as Files
Tom J. Killian. USENIX, June 1984. 
The paper that introduced the /proc ﬁle system, where each process can be treated as a ﬁle within a pseudo ﬁle system. A clever idea that you can still see in modern U NIX systems.

## [MJLF84] A Fast File System for U NIX
Marshall K. McKusick, William N. Joy, Sam J. Lefﬂer, Robert S. Fabry. ACM TOCS, 2:3, August 1984. 
We’ll talk about the Fast File System (FFS) explicitly later on. Here, we refer to it because of all the other random fun things it introduced, like long ﬁle names and symbolic links. Sometimes, when you are building a system to improve one thing, you improve a lot of other things along the way.

## [SR05] Advanced Programming in the U NIX Environment
W. Richard Stevens and Stephen A. Rago. Addison-Wesley, 2005. 
We have probably referenced this book a few hundred thousand times. It is that useful to you, if you care to become an awesome systems programmer.

## [BD96] Checking for Race Conditions in File Accesses
Matt Bishop, Michael Dilger. Computing Systems 9:2, 1996. 
A great description of the TOCTTOU problem and its presence in ﬁle systems.

# Chapter 40: File System Implementation

## [H+88] Scale and Performance in a Distributed File System
John H. Howard, Michael L. Kazar, Sherri G. Menees, David A. Nichols, M. Satyanarayanan, Robert N. Sidebotham, Michael J. West.. ACM TOCS, Volume 6:1, February 1988. 
A classic distributed ﬁle system; we’ll be learning more about it later, don’t worry.

## [RT74] The U NIX Time-Sharing System
M. Ritchie, K. Thompson. CACM Volume 17:7, 1974. 
The original paper about UNIX. Read it to see the underpinnings of much of modern operating systems.

## [B02] The FAT File System
Andries Brouwer. September, 2002. Available online at: http://www.win.tue.nl/˜aeb/linux/fs/fat/fat.html. 
A nice clean description of FAT. The ﬁle system kind, not the bacon kind. Though you have to admit, bacon fat probably tastes better.

## [B07] ZFS: The Last Word in File Systems
Jeff Bonwick and Bill Moore. Available from: http://www.ostep.org/Citations/zfs_last.pdf. 
One of the most recent important ﬁle systems, full of features and awesomeness. We should have a chapter on it, and perhaps soon will.

## [A+07] A Five-Year Study of File-System Metadata
Nitin Agrawal, William J. Bolosky, John R. Douceur, Jacob R. Lorch. FAST ’07, San Jose, California, February 2007. 
An excellent recent analysis of how ﬁle systems are actually used. Use the bibliography within to follow the trail of ﬁle-system analysis papers back to the early 1980s.

## [S00] UBC: An Efﬁcient Uniﬁed I/O and Memory Caching Subsystem for NetBSD
Chuck Silvers. FREENIX, 2000. 
A nice paper about NetBSD’s integration of ﬁle-system buffer caching and the virtual-memory page cache. Many other systems do the same type of thing.

## [S+96] Scalability in the XFS File System
Adan Sweeney, Doug Doucette, Wei Hu, Curtis Anderson, Mike Nishimoto, Geoff Peck. USENIX ’96, January 1996, San Diego, California. 
The ﬁrst attempt to make scalability of operations, including things like having millions of ﬁles in a directory, a central focus. A great example of pushing an idea to the extreme. The key idea behind this ﬁle system: everything is a tree. We should have a chapter on this ﬁle system too.

## [P09] The Second Extended File System: Internal Layout
Dave Poirier. 2009. Available: http://www.nongnu.org/ext2-doc/ext2.html. 
Some details on ext2, a very simple Linux ﬁle system based on FFS, the Berkeley Fast File System. We’ll be reading about it in the next chapter.

## [C94] Inside the Windows NT File System
Helen Custer. Microsoft Press, 1994. 
A short book about NTFS; there are probably ones with more technical details elsewhere.

# Chapter 41: Fast File System (FFS)

## [AD14a] Operating Systems: Three Easy Pieces” (Chapter: Hard Disk Drives)	Remzi Arpaci-Dusseau and Andrea Arpaci-Dusseau. Arpaci-Dusseau Books, 2014. 	There is no way you should be reading about FFS without having ﬁrst understood hard drives in some detail. If you try to do so, please instead go directly to jail; do not pass go, and, critically, do not collect 200 much-needed simoleons.
[AD14b]	Operating Systems: Three Easy Pieces” (Chapter: File System Implementation)
Remzi Arpaci-Dusseau and Andrea Arpaci-Dusseau . Arpaci-Dusseau Books, 2014. 
As above, it makes little sense to read this chapter unless you have read (and understood) the chapter on ﬁle system implementation. Otherwise, we’ll be throwing around terms like "inode" and "indirect block” and you’ll be like "huh?” and that is no fun for either of us.

## [K94] The Design of the SEER Predictive Caching System
G. H. Kuenning. MOBICOMM ’94, Santa Cruz, California, December 1994. 
According to Kuenning, this is the best overview of the SEER project, which led to (among other things) the collection of these traces.

## [P98] Hardware Technology Trends and Database Opportunities
David A. Patterson. Keynote Lecture at SIGMOD ’98, June 1998. 
A great and simple overview of disk technology trends and how they change over time.

## [MJLF84] A Fast File System for U NIX
Marshall K. McKusick, William N. Joy, Sam J. Lefﬂer, Robert S. Fabry. ACM TOCS, 2:3, August 1984. McKusick was recently honored with the IEEE Reynold B. 
Johnson award for his contributions to ﬁle systems, much of which was based on his work building FFS. In his acceptance speech, he discussed the original FFS software: only 1200 lines of code! Modern versions are a little more complex, e.g., the BSD FFS descendant now is in the 50-thousand lines-of-code range.

# Chapter 42: FSCK and Journaling

## [C+13] Optimistic Crash Consistency
Vijay Chidambaram, Thanu S. Pillai, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau . SOSP ’13, Nemacolin Woodlands Resort, PA, November 2013. 
Our work on a more optimistic and higher performance journaling protocol. For workloads that call fsync() a lot, performance can be greatly improved.

## [M+13] ffsck: The Fast File System Checker
Ao Ma, Chris Dragga, Andrea C. ArpaciDusseau, Remzi H. Arpaci-Dusseau. FAST ’13, San Jose, California, February 2013. 
A recent paper of ours detailing how to make fsck an order of magnitude faster. Some of the ideas have already been incorporated into the BSD ﬁle system checker [MK96] and are deployed today.

## [H87] Reimplementing the Cedar File System Using Logging and Group Commit
Robert Hagmann. SOSP ’87, Austin, Texas, November 1987. 
The ﬁrst work (that we know of) that applied write-ahead logging (a.k.a. journaling) to a ﬁle system.

## [G+08] SQCK: A Declarative File System Checker
Haryadi S. Gunawi, Abhishek Rajimwale, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. OSDI ’08, San Diego, California. 
Our own paper on a new and better way to build a ﬁle system checker using SQL queries. We also show some problems with the existing checker, ﬁnding numerous bugs and odd behaviors, a direct result of the complexity of fsck.

## [GP94] Metadata Update Performance in File Systems
Gregory R. Ganger and Yale N. Patt. OSDI ’94. 
A clever paper about using careful ordering of writes as the main way to achieve consistency. Implemented later in BSD-based systems.

## [MK96] Fsck – The U NIX File System Check Program
Marshall Kirk McKusick and T. J. Kowalski. Revised in 1996. 
Describes the ﬁrst comprehensive ﬁle-system checking tool, the eponymous fsck. Written by some of the same people who brought you FFS.

## [B07] ZFS: The Last Word in File Systems
Jeff Bonwick and Bill Moore. Available online: http://www.ostep.org/Citations/zfs_last.pdf. 
ZFS uses copy-on-write and journaling, actually, as in some cases, logging writes to disk will perform better.

## [C+12] Consistency Without Ordering
Vijay Chidambaram, Tushar Sharma, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. FAST ’12, San Jose, California. 
A recent paper of ours about a new form of crash consistency based on back pointers. Read it for the exciting details!

## [P+05] IRON File Systems
Vijayan Prabhakaran, Lakshmi N. Bairavasundaram, Nitin Agrawal, Haryadi S. Gunawi, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. SOSP ’05, Brighton, England, October 2005. 
A paper mostly focused on studying how ﬁle systems react to disk failures. Towards the end, we introduce a transaction checksum to speed up logging, which was eventually adopted into Linux ext4.

## [PAA05] Analysis and Evolution of Journaling File Systems
Vijayan Prabhakaran, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. USENIX ’05, Anaheim, California, April 2005. 
An early paper we wrote analyzing how journaling ﬁle systems work.

## [R+11] Coerced Cache Eviction and Discreet-Mode Journaling
Abhishek Rajimwale, Vijay Chidambaram, Deepak Ramamurthi, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. DSN ’11, Hong Kong, China, June 2011.
 Our own paper on the problem of disks that buffer writes in a memory cache instead of forcing them to disk, even when explicitly told not to do that! Our solution to overcome this problem: if you want A to be written to disk before B, ﬁrst write A, then send a lot of "dummy” writes to disk, hopefully causing A to be forced to disk to make room for them in the cache. A neat if impractical solution.

## [T98] Journaling the Linux ext2fs File System
Stephen C. Tweedie. The Fourth Annual Linux Expo, May 1998. 
Tweedie did much of the heavy lifting in adding journaling to the Linux ext2 ﬁle system; the result, not surprisingly, is called ext3. Some nice design decisions include the strong focus on backwards compatibility, e.g., you can just add a journaling ﬁle to an existing ext2 ﬁle system and then mount it as an ext3 ﬁle system.

## [T00] EXT3, Journaling Filesystem
Stephen Tweedie. 
Talk at the Ottawa Linux Symposium, July 2000. olstrans.sourceforge.net/release/OLS2000-ext3/OLS2000-ext3.html A transcript of a talk given by Tweedie on ext3.

## [T01] The Linux ext2 File System
Theodore Ts’o, June, 2001.. Available online here: http://e2fsprogs.sourceforge.net/ext2.html. 
A simple Linux ﬁle system based on the ideas found in FFS. For a while it was quite heavily used; now it is really just in the kernel as an example of a simple ﬁle system.

## [P+14] All File Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent Applications
Thanumalayan Sankaranarayana Pillai, Vijay Chidambaram, Ramnatthan Alagappan, Samer Al-Kiswany, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. OSDI ’14, Broomﬁeld, Colorado, October 2014. 
A paper in which we study what ﬁle systems guarantee after crashes, and show that applications expect something different, leading to all sorts of interesting problems.

## [MJLF84] A Fast File System for UNIX
Marshall K. McKusick, William N. Joy, Sam J. Lefﬂer, Robert S. Fabry. ACM Transactions on Computing Systems, Volume 2:3, August 1984. 
You already know enough about FFS, right? But come on, it is OK to re-reference important papers.

# Chapter 43: Log-structured File System (LFS)

## [AD14] Operating Systems: Three Easy Pieces (Chapter: Flash-based Solid State Drives) 
Remzi Arpaci-Dusseau and Andrea Arpaci-Dusseau. Arpaci-Dusseau Books, 2014. 
A bit gauche to refer you to another chapter in this very book, but who are we to judge?

## [B07] ZFS: The Last Word in File Systems
Jeff Bonwick and Bill Moore. Copy Available: http://www.ostep.org/Citations/zfs_last.pdf. 
Slides on ZFS; unfortunately, there is no great ZFS paper (yet). Maybe you will write one, so we can cite it here?

## [H+17] The Unwritten Contract of of Solid State Drives
Jun He, Sudarsun Kannan, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. EuroSys ’17, April 2017. 
Which unwritten rules one must follow to extract high performance from an SSD? Interestingly, both request scale (large or parallel requests) and locality still matter, even on SSDs. The more things change ...

## [L77] Physical Integrity in a Large Segmented Database
R. Lorie. ACM Transactions on Databases, Volume 2:1, 1977. 
The original idea of shadow paging is presented here.

## [MJLF84] A Fast File System for UNIX
Marshall K. McKusick, William N. Joy, Sam J. Lefﬂer, Robert S. Fabry. ACM TOCS, Volume 2:3, August 1984. 
The original FFS paper; see the chapter on FFS for more details.

## [MR+97] Improving the Performance of Log-structured File Systems with Adaptive Methods
Jeanna Neefe Matthews, Drew Roselli, Adam M. Costello, Randolph Y. Wang, Thomas E. Anderson. SOSP 1997, pages 238-251, October, Saint Malo, France. 
A more recent paper detailing better policies for cleaning in LFS.

## [M94] A Better Update Policy
Jeffrey C. Mogul. USENIX ATC ’94, June 1994. 
In this paper, Mogul ﬁnds that read workloads can be harmed by buffering writes for too long and then sending them to the disk in a big burst. Thus, he recommends sending writes more frequently and in smaller batches.

## [P98] Hardware Technology Trends and Database Opportunities
David A. Patterson. ACM SIGMOD ’98 Keynote, 1998. Available online here: http://www.cs.berkeley.edu/ ˜pattrsn/talks/keynote.html.
 A great set of slides on technology trends in computer systems. Hopefully, Patterson will create another of these sometime soon.

## [R+13] BTRFS: The Linux B-Tree Filesystem
Ohad Rodeh, Josef Bacik, Chris Mason. ACM Transactions on Storage, Volume 9 Issue 3, August 2013. 
Finally, a good paper on BTRFS, a modern take on copy-on-write ﬁle systems.

## [RO91] Design and Implementation of the Log-structured File System
Mendel Rosenblum and John Ousterhout. SOSP ’91, Paciﬁc Grove, CA, October 1991. 
The original SOSP paper about LFS, which has been cited by hundreds of other papers and inspired many real systems.

## [R92] Design and Implementation of the Log-structured File System
Mendel Rosenblum. http://www.eecs.berkeley.edu/Pubs/TechRpts/1992/CSD-92-696.pdf. 
The award-winning dissertation about LFS, with many of the details missing from the paper.

## [SS+95] File system logging versus clustering: a performance comparison
Margo Seltzer, Keith A. Smith, Hari Balakrishnan, Jacqueline Chang, Sara McMains, Venkata Padmanabhan. USENIX 1995 Technical Conference, New Orleans, Louisiana, 1995. 
A paper that showed the LFS performance sometimes has problems, particularly for workloads with many calls to fsync() (such as database workloads). The paper was controversial at the time.

## [HLM94] File System Design for an NFS File Server Appliance
Dave Hitz, James Lau, Michael Malcolm. USENIX Spring ’94. 
WAFL takes many ideas from LFS and RAID and puts it into a high-speed NFS appliance for the multi-billion dollar storage company NetApp.

## [SO90] Write-Only Disk Caches
Jon A. Solworth, Cyril U. Orji. SIGMOD ’90, Atlantic City, New Jersey, May 1990. 
An early study of write buffering and its beneﬁts. However, buffering for too long can be harmful: see Mogul [M94] for details.

## [Z+12] De-indirection for Flash-based SSDs with Nameless Writes
Yiying Zhang, Leo Prasath Arulraj, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. FAST ’13, San Jose, California, February 2013. 
Our paper on a new way to build ﬂash-based storage devices, to avoid redundant mappings in the ﬁle system and FTL. The idea is for the device to pick the physical location of a write, and return the address to the ﬁle system, which stores the mapping.

# Chapter 44: Flash-based SSDs

## [KK+02] A Space-Efﬁcient Flash Translation Layer For Compact Flash Systems
Jesung Kim, Jong Min Kim, Sam H. Noh, Sang Lyul Min, Yookun Cho. IEEE Transactions on Consumer Electronics, Volume 48, Number 2, May 2002. 
One of the earliest proposals to suggest hybrid mappings.

## [L+07] A Log Buffer-Based Flash Translation Layer by Using Fully-Associative Sector Translation.
Sang-won Lee, Tae-Sun Chung, Dong-Ho Lee, Sangwon Park, Ha-Joo Song. ACM Transactions on Embedded Computing Systems, Volume 6, Number 3, July 2007 
A terriﬁc paper about how to build hybrid log/block mappings.

## [M+14] A Survey of Address Translation Technologies for Flash Memories
Dongzhe Ma, Jianhua Feng, Guoliang Li. ACM Computing Surveys, Volume 46, Number 3, January 2014. 
Probably the best recent survey of ﬂash and related technologies.

## [Z+12] De-indirection for Flash-based SSDs with Nameless Writes
Yiying Zhang, Leo Prasath Arulraj, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. FAST ’13, San Jose, California, February 2013. 
Our research on a new idea to reduce mapping table space; the key is to re-use the pointers in the ﬁle system above to store locations of blocks, instead of adding another level of indirection.

## [T15] Performance Charts Hard Drives
Tom’s Hardware. January 2015. Available here: http://www.tomshardware.com/charts/enterprise-hdd-charts. 
Yet another site with performance data, this time focusing on hard drives.

## [W15] List of Ships Sunk by Icebergs
Many authors. Available at this location on the "web": http://en.wikipedia.org/wiki/List of ships sunk by icebergs. 
Yes, there is a wikipedia page about ships sunk by icebergs. It is a really boring page and basically everyone knows the only ship the iceberg-sinking-maﬁa cares about is the Titanic.

## [S13] The Seagate 600 and 600 Pro SSD Review
Anand Lal Shimpi. AnandTech, May 7, 2013. Available: http://www.anandtech.com/show/6935/seagate-600-ssd-review. 
One of many SSD performance measurements available on the internet. Haven’t heard of the internet? No problem. Just go to your web browser and type "internet" into the search tool. You’ll be amazed at what you can learn.

## [J10] Failure Mechanisms and Models for Semiconductor Devices
Unknown author. Report JEP122F, November 2010. Available on the internet at this exciting so-called web site: http://www.jedec.org/sites/default/files/docs/JEP122F.pdf. 
A highly detailed discussion of what is going on at the device level and how such devices fail. Only for those not faint of heart. Or physicists. Or both.

## [V12] Understanding TLC Flash
Kristian Vatto. AnandTech, September, 2012. Available: http://www.anandtech.com/show/5067/understanding-tlc-nand. 
A short description about TLC ﬂash and its characteristics.

## [HK+17] The Unwritten Contract of Solid State Drives
Jun He, Sudarsun Kannan, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. EuroSys ’17, Belgrade, Serbia, April 2017. 
Our own paper which lays out ﬁve rules clients should follow in order to get the best performance out of modern SSDs. The rules are request scale, locality, aligned sequentiality, grouping by death time, and uniform lifetime. Read the paper for details!

## [H+14] An Aggressive Worn-out Flash Block Management Scheme To Alleviate SSD Performance Degradation
Ping Huang, Guanying Wu, Xubin He, Weijun Xiao. EuroSys ’14, 2014. 
Recent work showing how to really get the most out of worn-out ﬂash blocks; neat!

## [A+08] Design Tradeoffs for SSD Performance
N. Agrawal, V. Prabhakaran, T. Wobber, J. D. Davis, M. Manasse, R. Panigrahy. USENIX ’08, San Diego California, June 2008. 
An excellent overview of what goes into SSD design.

## [AD14] Operating Systems: Three Easy Pieces
Chapters: Crash Consistency: FSCK and Journaling and Log-Structured File Systems. Remzi Arpaci-Dusseau and Andrea Arpaci-Dusseau. 
A lot more detail here about how logging can be used in ﬁle systems; some of the same ideas can be applied inside devices too as need be.

## [A15] Amazon Pricing Study
Remzi Arpaci-Dusseau. February, 2015. 
This is not an actual paper, but rather one of the authors going to Amazon and looking at current prices of hard drives and SSDs. You too can repeat this study, and see what the costs are today. Do it!

## [B+12] CORFU: A Shared Log Design for Flash Clusters
M. Balakrishnan, D. Malkhi, V. Prabhakaran, T. Wobber, M. Wei, J. D. Davis. NSDI ’12, San Jose, California, April 2012. 
A new way to think about designing a high-performance replicated log for clusters using Flash.

## [CG+09] Gordon: Using Flash Memory to Build Fast, Power-efﬁcient Clusters for Data-intensive Applications
Adrian M. Caulﬁeld, Laura M. Grupp, Steven Swanson. ASPLOS ’09, Washington, D.C., March 2009. 
Early research on assembling ﬂash into larger-scale clusters; deﬁnitely worth a read.

## [B07] ZFS: The Last Word in File Systems
Jeff Bonwick and Bill Moore. Available here: http://www.ostep.org/Citations/zfs_last.pdf. 
Was this the last word in ﬁle systems? No, but maybe it’s close.

## [CK+09] Understanding Intrinsic Characteristics and System Implications of Flash Memory based Solid State Drives
Feng Chen, David A. Koufaty, and Xiaodong Zhang. SIGMETRICS/Performance ’09, Seattle, Washington, June 2009. 
An excellent overview of SSD performance problems circa 2009 (though now a little dated).

## [G14] The SSD Endurance Experiment
Geoff Gasior. The Tech Report, September 19, 2014. Available: http://techreport.com/review/27062. 
A nice set of simple experiments measuring performance of SSDs over time. There are many other similar studies; use google to ﬁnd more.

## [GC+09] Characterizing Flash Memory: Anomalies, Observations, and Applications
L. M. Grupp, A. M. Caulﬁeld, J. Coburn, S. Swanson, E. Yaakobi, P. H. Siegel, J. K. Wolf. IEEE MICRO ’09, New York, New York, December 2009. 
Another excellent characterization of ﬂash performance.

## [GY+09] DFTL: a Flash Translation Layer Employing Demand-Based Selective Caching of Page-Level Address Mappings
Aayush Gupta, Youngjae Kim, Bhuvan Urgaonkar. ASPLOS ’09, Washington, D.C., March 2009. 
This paper gives an excellent overview of different strategies for cleaning within hybrid SSDs as well as a new scheme which saves mapping table space and improves performance under many workloads.

## [BD10] Write Endurance in Flash Drives: Measurements and Analysis
Simona Boboila, Peter Desnoyers. FAST ’10, San Jose, California, February 2010. 
A cool paper that reverse engineers ﬂash-device lifetimes. Endurance sometimes far exceeds manufacturer predictions, by up to 100×.

# Chapter 45: Data Integrity and Protection

## [B+07] An Analysis of Latent Sector Errors in Disk Drives
L. Bairavasundaram, G. Goodson, S. Pasupathy, J. Schindler. SIGMETRICS ’07, San Diego, CA. 
The ﬁrst paper to study latent sector errors in detail. The paper also won the Kenneth C. Sevcik Outstanding Student Paper award, named after a brilliant researcher and wonderful guy who passed away too soon. To show the OSTEP authors it was possible to move from the U.S. to Canada, Ken once sang us the Canadian national anthem, standing up in the middle of a restaurant to do so. We chose the U.S., but got this memory.

## [B+08] An Analysis of Data Corruption in the Storage Stack
Lakshmi N. Bairavasundaram, Garth R. Goodson, Bianca Schroeder, Andrea C. Arpaci-Dusseau, Remzi H. ArpaciDusseau. FAST ’08, San Jose, CA, February 2008. 
The ﬁrst paper to truly study disk corruption in great detail, focusing on how often such corruption occurs over three years for over 1.5 million drives.

## [BS04] Commercial Fault Tolerance: A Tale of Two Systems
Wendy Bartlett, Lisa Spainhower. IEEE Transactions on Dependable and Secure Computing, Vol. 1:1, January 2004. 
This classic in building fault tolerant systems is an excellent overview of the state of the art from both IBM and Tandem. Another must read for those interested in the area.

## [C+04] Row-Diagonal Parity for Double Disk Failure Correction
P. Corbett, B. English, A. Goel, T. Grcanac, S. Kleiman, J. Leong, S. Sankar. FAST ’04, San Jose, CA, February 2004. 
An early paper on how extra redundancy helps to solve the combined full-disk-failure/partial-disk-failure problem. Also a nice example of how to mix more theoretical work with practical.

## [F04] Checksums and Error Control
Peter M. Fenwick. Copy available online here: http://www.ostep.org/Citations/checksums-03.pdf. 
A great simple tutorial on checksums, available to you for the amazing cost of free.

## [K+08] Parity Lost and Parity Regained
Andrew Krioukov, Lakshmi N. Bairavasundaram, Garth R. Goodson, Kiran Srinivasan, Randy Thelen, Andrea C. Arpaci-Dusseau, Remzi H. Arpaci-Dusseau. FAST ’08, San Jose, CA, February 2008. 
This work explores how different checksum schemes work (or don’t work) in protecting data. We reveal a number of interesting ﬂaws in current protection strategies.

## [HLM94] File System Design for an NFS File Server Appliance
Dave Hitz, James Lau, Michael Malcolm. USENIX Spring ’94. 
The pioneering paper that describes the ideas and product at the heart of NetApp’s core. Based on this system, NetApp has grown into a multi-billion dollar storage company. To learn more about NetApp, read Hitz’s autobiography "How to Castrate a Bull” (which is the actual title, no joking). And you thought you could avoid bull castration by going into CS.

## [M13] Cyclic Redundancy Checks
unknown. Available: http://www.mathpages.com/ home/kmath458.htm. 
A super clear and concise description of CRCs. The internet is full of information, as it turns out.

## [P+05] IRON File Systems
V. Prabhakaran, L. Bairavasundaram, N. Agrawal, H. Gunawi, A. Arpaci-Dusseau, R. Arpaci-Dusseau. SOSP ’05, Brighton, England. 
Our paper on how disks have partial failure modes, and a detailed study of how modern ﬁle systems react to such failures. As it turns out, rather poorly! We found numerous bugs, design ﬂaws, and other oddities in this work. Some of this has fed back into the Linux community, thus improving ﬁle system reliability. You’re welcome!

## [RO91] Design and Implementation of the Log-structured File System
Mendel Rosenblum and John Ousterhout. SOSP ’91, Paciﬁc Grove, CA, October 1991. 
So cool we cite it again.

## [Z+13] Zettabyte Reliability with Flexible End-to-end Data Integrity
Y. Zhang, D. Myers, A. Arpaci-Dusseau, R. Arpaci-Dusseau. MSST ’13, Long Beach, California, May 2013. 
How to add data protection to the page cache of a system. Out of space, otherwise we would write something...

## [F82] An Arithmetic Checksum for Serial Transmissions
John G. Fletcher. IEEE Transactions on Communication, Vol. 30:1, January 1982. 
Fletcher’s original work on his eponymous checksum. He didn’t call it the Fletcher checksum, rather he just didn’t call it anything; later, others named it after him. So don’t blame old Fletch for this seeming act of braggadocio. This anecdote might remind you of Rubik; Rubik never called it "Rubik’s cube”; rather, he just called it "my cube.”

## [S90] Implementing Fault-Tolerant Services Using The State Machine Approach: A Tutorial
Fred B. Schneider. ACM Surveys, Vol. 22, No. 4, December 1990. 
How to build fault tolerant services. A must read for those building distributed systems.

# Chapter 48: Distributed Systems

## [VJ88] Congestion Avoidance and Control
Van Jacobson. SIGCOMM ’88 . 
A pioneering paper on how clients should adjust to perceived network congestion; deﬁnitely one of the key pieces of technology underlying the Internet, and a must read for anyone serious about systems, and for Van Jacobson’s relatives because well relatives should read all of your papers.

## [A70] The ALOHA System — Another Alternative for Computer Communications
Norman Abramson. The 1970 Fall Joint Computer Conference. 
The ALOHA network pioneered some basic concepts in networking, including exponential back-off and retransmit, which formed the basis for communication in shared-bus Ethernet networks for years.

## [BN84] Implementing Remote Procedure Calls
Andrew D. Birrell, Bruce Jay Nelson. ACM TOCS, Volume 2:1, February 1984. 
The foundational RPC system upon which all others build. Yes, another pioneering effort from our friends at Xerox PARC.

## [MK09] The Effectiveness of Checksums for Embedded Control Networks
Theresa C. Maxino and Philip J. Koopman. IEEE Transactions on Dependable and Secure Computing, 6:1, January ’09. 
A nice overview of basic checksum machinery and some performance and robustness comparisons between them.

## [LH89] Memory Coherence in Shared Virtual Memory Systems
Kai Li and Paul Hudak. ACM TOCS, 7:4, November 1989. 
The introduction of software-based shared memory via virtual memory. An intriguing idea for sure, but not a lasting or good one in the end.

## [SK09] Principles of Computer System Design
Jerome H. Saltzer and M. Frans Kaashoek. Morgan-Kaufmann, 2009.
An excellent book on systems, and a must for every bookshelf. One of the few terriﬁc discussions on naming we’ve seen.

## [SRC84] End-To-End Arguments in System Design
Jerome H. Saltzer, David P. Reed, David D. Clark. ACM TOCS, 2:4, November 1984.
A beautiful discussion of layering, abstraction, and where functionality must ultimately reside in computer systems.

# Chapter 49: Network File System (NFS)

## [Sun89] NFS: Network File System Protocol Speciﬁcation
Sun Microsystems, Inc. Request for Comments: 1094, March 1989. Available: http://www.ietf.org/rfc/rfc1094.txt. 
The dreaded speciﬁcation; read it if you must, i.e., you are getting paid to read it. Hopefully, paid a lot. Cash money!

## [C00] NFS Illustrated
Brent Callaghan. Addison-Wesley Professional Computing Series, 2000. 
A great NFS reference; incredibly thorough and detailed per the protocol itself.

## [ES03] New NFS Tracing Tools and Techniques for System Analysis
Daniel Ellard and Margo Seltzer. LISA ’03, San Diego, California. 
An intricate, careful analysis of NFS done via passive tracing. By simply monitoring network trafﬁc, the authors show how to derive a vast amount of ﬁle system understanding.

## [HLM94] File System Design for an NFS File Server Appliance
Dave Hitz, James Lau, Michael Malcolm. USENIX Winter 1994. San Francisco, California, 1994. 
Hitz et al. were greatly inﬂuenced by previous work on log-structured ﬁle systems.

## [K86] Vnodes: An Architecture for Multiple File System Types in Sun U NIX
Steve R. Kleiman. USENIX Summer ’86, Atlanta, Georgia. 
This paper shows how to build a ﬂexible ﬁle system architecture into an operating system, enabling multiple different ﬁle system implementations to coexist. Now used in virtually every modern operating system in some form.

## [NT94] Kerberos: An Authentication Service for Computer Networks
B. Clifford Neuman, Theodore Ts’o. IEEE Communications, 32(9):33-38, September 1994. 
Kerberos is an early and hugely inﬂuential authentication service. We probably should write a book chapter about it sometime...

## [O91] The Role of Distributed State
John K. Ousterhout. 1991. Available at this site: ftp://ftp.cs.berkeley.edu/ucb/sprite/papers/state.ps. 
A rarely referenced discussion of distributed state; a broader perspective on the problems and challenges.

## [P+94] NFS Version 3: Design and Implementation
Brian Pawlowski, Chet Juszczak, Peter Staubach, Carl Smith, Diane Lebel, Dave Hitz. USENIX Summer 1994, pages 137-152. 
The small modiﬁcations that underlie NFS version 3.

## [P+00] The NFS version 4 protocol
Brian Pawlowski, David Noveck, David Robinson, Robert Thurlow. 2nd International System Administration and Networking Conference (SANE 2000). 
Undoubtedly the most literary paper on NFS ever written.

## [AKW88] The AWK Programming Language
Alfred V. Aho, Brian W. Kernighan, Peter J. Weinberger. Pearson, 1988 (1st edition). 
A concise, wonderful book about awk. We once had the pleasure of meeting Peter Weinberger; when he introduced himself, he said I’m Peter Weinberger, you know, the ’W’ in awk?” As huge awk fans, this was a moment to savor. One of us (Remzi) then said, I love awk! I particularly love the book, which makes everything so wonderfully clear.” Weinberger replied (crestfallen), "Oh, Kernighan wrote the book.”

## [S86] The Sun Network File System: Design, Implementation and Experience
Russel Sandberg. USENIX Summer 1986. 
The original NFS paper; though a bit of a challenging read, it is worthwhile to see the source of these wonderful ideas.

## [V72] La Begueule
Francois-Marie Arouet a.k.a. Voltaire. Published in 1772. 
Voltaire said a number of clever things, this being but one example. For example, Voltaire also said "If you have two religions in your land, the two will cut each others throats; but if you have thirty religions, they will dwell in peace.” What do you say to that, Democrats and Republicans?

## [RO91] The Design and Implementation of the Log-structured File System
Mendel Rosenblum, John Ousterhout. Symposium on Operating Systems Principles (SOSP), 1991. LFS again. 
No, you can never get enough LFS.

# Chapter 50: Andrew File System (AFS)

## [V99] File system usage in Windows NT 4.0
Werner Vogels. SOSP ’99, Kiawah Island Resort, South Carolina, December 1999. 
A cool study of Windows workloads, which are inherently different than many of the U NIX-based studies that had previously been done.

## [B+91] Measurements of a Distributed File System
Mary Baker, John Hartman, Martin Kupfer, Ken Shirriff, John Ousterhout. SOSP ’91, Paciﬁc Grove, California, October 1991. 
An early paper measuring how people use distributed ﬁle systems. Matches much of the intuition found in AFS.

## [H+11] A File is Not a File: Understanding the I/O Behavior of Apple Desktop Applications
Tyler Harter, Chris Dragga, Michael Vaughn, Andrea C. Arpaci-Dusseau, Remzi H. ArpaciDusseau. SOSP ’11, New York, New York, October 2011. 
Our own paper studying the behavior of Apple Desktop workloads; turns out they are a bit different than many of the server-based workloads the systems research community usually focuses upon. Also a good recent reference which points to a lot of related work.

## [H+88] Scale and Performance in a Distributed File System
John H. Howard, Michael L. Kazar, Sherri G. Menees, David A. Nichols, M. Satyanarayanan, Robert N. Sidebotham, Michael J. West. ACM Transactions on Computing Systems (ACM TOCS), Volume 6:1, February 1988. 
The long journal version of the famous AFS system, still in use in a number of places throughout the world, and also probably the earliest clear thinking on how to build distributed ﬁle systems. A wonderful combination of the science of measurement and principled engineering.

## [R+00] A Comparison of File System Workloads
Drew Roselli, Jacob R. Lorch, Thomas E. Anderson. USENIX ’00, San Diego, California, June 2000. 
A more recent set of traces as compared to the Baker paper [B+91], with some interesting twists.

## [S+85] The ITC Distributed File System: Principles and Design
M. Satyanarayanan, J.H. Howard, D.A. Nichols, R.N. Sidebotham, A. Spector, M.J. West. SOSP ’85, Orcas Island, Washington, December 1985. 
The older paper about a distributed ﬁle system. Much of the basic design of AFS is in place in this older system, but not the improvements for scale. The name change to "Andrew” is an homage to two people both named Andrew, Andrew Carnegie and Andrew Mellon. These two rich dudes started the Carnegie Institute of Technology and the Mellon Institute of Industrial Research, respectively, which eventually merged to become what is now known as Carnegie Mellon University.

