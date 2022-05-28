# Dynamic-Pricing

Dynamic pricing in hotels is a strategy used to improve revenue and ensure maximum occupancy for the hotel based on supply and demand. 

![image](https://user-images.githubusercontent.com/70309244/170830019-e5cb8bac-a572-4ea6-aa7a-b5d18e2956a8.png)

**Thompson Sampling** (Posterior Sampling or Probability Matching) is an algorithm for choosing the actions that address the exploration-exploitation dilemma in the multi-armed bandit problem.

![image](https://user-images.githubusercontent.com/70309244/170830112-6bdf14e6-c63a-4fd7-af3d-34555b353186.png)

By using the implementation (refer the uploaded Python file), visualizing 200 iterations:
![image](https://user-images.githubusercontent.com/70309244/170830181-a9b68f9c-204f-49e1-8c21-48f77ae31cc7.png)
![image](https://user-images.githubusercontent.com/70309244/170830187-bb0e3d49-b9da-45e3-801b-04b8ff5d6ff0.png)
![image](https://user-images.githubusercontent.com/70309244/170830207-879f9ee2-d177-47e0-8cbe-bf145b44579b.png)
After 200 iterations, we can see that the price of $3.49 was selected 87% of the time.
$3.49 is the closest to the optimal price as per the true demand distribution and the algorithm has successfully exploited the price while continuing to explore the available options.
