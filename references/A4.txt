[BH73] “Operating System Principles” Per Brinch Hansen, Prentice-Hall, 1973 Available: http://portal.acm.org/citation.cfm?id=540365 One of the ﬁrst books on operating systems; certainly ahead of its time. concurrency primitive.

Introduced monitors as a

[H74] “Monitors: An Operating System Structuring Concept” C.A.R. Hoare CACM, Volume 17:10, pages 549–557, October 1974 An early reference to monitors; however, Brinch Hansen probably was the true inventor.

[H61] “Quicksort: Algorithm 64” C.A.R. Hoare CACM, Volume 4:7, July 1961 The famous quicksort algorithm.

[LR80] “Experience with Processes and Monitors in Mesa” B.W. Lampson and D.R. Redell CACM, Volume 23:2, pages 105–117, February 1980 An early and important paper highlighting the differences between theory and practice.

[L83] “Hints for Computer Systems Design” Butler Lampson ACM Operating Systems Review, 15:5, October 1983 Lampson, a famous systems researcher, loved using hints in the design of computer systems. A hint is something that is often correct but can be wrong; in this use, a signal() is telling a waiting thread that it changed the condition that the waiter was waiting on, but not to trust that the condition will be in the desired state when the waiting thread wakes up. In this paper about hints for designing systems, one of Lampson’s general hints is that you should use hints. It is not as confusing as it sounds.

[S12a] “Synchronized Methods” Sun documentation http://java.sun.com/docs/books/tutorial/essential/concurrency/syncmeth.html

[S12b] “Condition Interface” Sun documentation http://java.sun.com/j2se/1.5.0/docs/api/java/util/concurrent/locks/Condition.html