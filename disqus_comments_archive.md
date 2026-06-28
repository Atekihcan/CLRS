# Disqus Comments Archive

Exported from atekihcan.disqus.com on 2026-06-28. 25 comments total.

## Re: CLRS Solutions | Exercise 5.4-7 | Probabilistic Analysis and Randomized Algorithms
**Atekihcan** | Thu, 28 May 2026 09:18:18 -0000

Thanks for your comment. I am not sure what was going through my mind when I wrote the previous solution haha. I have taken another shot at this hellspawn. And admittedly I needed some help from Claude to sharpen my final reasoning. Hope it holds now. Claude also pointed out a more rigorous proof, but I'm just leaving is as a note as I'm not really sure if that belongs here.

---

## Re: exercise 4.4-3
**Mark** | Tue, 24 Feb 2026 14:52:02 -0000

Thanks

---

## Re: CLRS Solutions | Exercise 5.4-7 | Probabilistic Analysis and Randomized Algorithms
**Ilya** | Sun, 30 Nov 2025 07:31:25 -0000

I'm sorry, but the way you arrive at the upper bound is flawed. In particular, the very last inequality -- n^(-1/2) < 1/n -- is obviously false, since n^(-1/2) = 1/sqrt(n) which is asymptotically larger than 1/n. Also, the statement you're aiming to prove here is actually different from the original problem statement: you're trying to prove the upper bound for the event that no streak of length s occurs, while you should've been trying to prove the upper bound for the event that no streak of length s+1 occurs.This is not to blame you or anything, just pointing out that, as of late 2025, it looks like there's still no correct solution to this hellish exercise, at least none that are available on the internet.

---

## Re: Exercise 2.3-7
**Andres Calderon Romero** | Wed, 19 Feb 2025 18:44:03 -0000

I hate ads but not you.  Go ahead!

---

## Re: CLRS - Problem 3-6
**bernie_haxx** | Sun, 26 Jan 2025 07:51:58 -0000

true

---

## Re: Exercise 2.3-5
**bernie_haxx** | Tue, 21 Jan 2025 10:07:06 -0000

hiIn the iterative approach, do the low and high values have to be the indices or the elements themselves in lines 1-2 cause I think it should be in tuned with their indices in order to work cause with their allocations it doesn't work

---

## Re: Exercise 2.1-3
**bernie_haxx** | Mon, 13 Jan 2025 05:50:10 -0000

hi I was asking about this statement on the maintenance part of the loop schema, does the subarray A[1..i] may or may not contain the value v before the next iteration? like the last portion cause it doesn't make sense if A[1..i] is the unchecked subarray

---

## Re: Problem 2-1
**shadowReader** | Thu, 03 Oct 2024 09:22:32 -0000

The recursive equation for complexity isT(n) = 2T(n/2) + Θ(n)as it is for normal merge sort.But T(k) = Θ(k^2) [Since it is insertion sort]Solving this gives your required answer

---

## Re: Changing Timeframe of OHLC Candlestick Data in Pandas
**Ajinkya JyotiPrakash Tambe** | Tue, 06 Feb 2024 07:10:48 -0000

Well articulated article...Older version :df = data.resample('5min', base=15).apply(ohlc)Since 2.0.0 versiondf = data.resample('5min',  offset=datetime.timedelta(minutes=5)).apply(ohlc)

---

## Re: Exercise 2.3-7
**5can** | Thu, 28 Dec 2023 00:30:00 -0000

firstline is nlgn,other is n, so is nlgn

---

## Re: Exercise 2.3-3
**sverde** | Fri, 08 Sep 2023 04:24:14 -0000

Yes, you're right. For the record:= 2*2^k * log(2^k) + 2*2^k  = 2^(k+1) * log(2^k) + 2^(k+1)  ; [a^m + a^n = a^(m+n)] = 2^(k+1)(log(2^k) + 1)                ; [factor 2^(k+1)] = 2^(k+1)(log(2^k) + log(2))      ; [log_b(b) = 1] (assume we're working with base 2)

---

## Re: Exercise 2.3-3
**Pizzaboo** | Fri, 08 Sep 2023 03:40:22 -0000

No, the answer is correct.

---

## Re: exercise 4.4-3
**artem** | Fri, 25 Aug 2023 07:43:05 -0000

i think so coast of node in i lvl isnt equal n/2^i+2 its equal to(n+4*2^i-4)/2^i (geometry progresion)

---

## Re: exercise 2.1-2
**jmac** | Wed, 19 Jul 2023 19:27:27 -0000

The book considers the indexes of an array in the range of [1, n] so it's okay.

---

## Re: Exercise 2.3-3
**sverde** | Tue, 04 Jul 2023 09:28:07 -0000

I think that the fourth step in the formula is not correct: 2⋅2^k(lg2^k + 1)The correct way is 2⋅2^k(lg2^k + 2) isn't it?

---

## Re: exercise 4.3-2
**sverde** | Wed, 21 Jun 2023 05:09:44 -0000

lg(n/2 + 1) +1 < lg(n+2/2)+1this doesn't hold for n = 1

---

## Re: Exercise 2.3-5
**Ovidiu Oprea** | Sun, 04 Jun 2023 05:25:27 -0000

tried the recursive variant in python and it doesn't return your value unless you set 'return Recursive-Binary-Search (A,v,mid + 1,high)' and 'return Recursive-Binary-Search (A,v,low,mid -1)' in the elseif and else branches. Otherwise you get None or the return of your first run through the recursive function. The return mid is overriden.

---

## Re: exercise 2.1-4
**Ovidiu Oprea** | Thu, 25 May 2023 06:19:35 -0000

Thank you for creating this website. I had put off the book indefinitely because I got stuck early, at 1.2-2. This website helped me because I could see that this was really advanced maths that was needed and there was no shame in using a hit-and-miss method instead or designing a simple computer program to bear the brunt.

---

## Re: Exercise 2.3-7
**Saurabh Verma** | Wed, 03 May 2023 13:48:31 -0000

The other method, total time for 2-11 isn't nlgn. Right? Therfore Not a suitable solution

---

## Re: Exercise 2.3-4
**Saurabh Verma** | Thu, 27 Apr 2023 14:41:55 -0000

I think You are getting the solution wrong.Subroutine in line 3 is called for value n Once the line 2 function is ready with sorted array A[1....n-1].This is simple "divide and conquer approach".

---

## Re: Problem 2-1
**Stv Cl** | Fri, 10 Mar 2023 15:37:48 -0000

but, what will be the value of k?

---

## Re: Exercise 2.3-5
**Stv Cl** | Fri, 10 Mar 2023 11:28:08 -0000

Hi, sorry for my bad English. There is an error in Iterative-Binary-Search. Low and high must be index, and not value.

---

## Re: Exercise 2.3-7
**Stv Cl** | Wed, 08 Mar 2023 16:46:55 -0000

Hi, sorry for mi English, but if you look at the code, first apply merge sort, then apply binary search in adittion  a loop for. So they are not nested.This is Θ(nlgn)+Θ(nlgn) =Θ(nlogn)

---

## Re: Exercise 2.3-5
**Andrea Attardo** | Mon, 24 Oct 2022 12:09:01 -0000

I got it now. Thanks for clarifying.

---

## Re: Exercise 2.3-5
**Atekihcan** | Mon, 24 Oct 2022 04:25:26 -0000

We are comparing the middle element, and then checking half of rest of the elements in the array, which is (n - 1)/2, as you are taking out the middle element from the consideration, hence (n - 1). But practically either way, worst case runtime is going to be lg(n). n or (n - 1) is not going to make any difference there.Try taking a practical example, say an array with 1024 elements. If you consider n/2, you'll reach down to 1 element in 10 steps. If you consider (n - 1)/2, same 10 steps will be required to reach down to 1 element, just that in every step, you'll have two arrays, but not of same size. For example, the first division will give you two arrays of size 511 and 512 elements, and so on. If you take larger of these, which you should for worst case, it's exactly same as considering n/2.

---
