1. For the TaskB, we are using the code of TaskA.py
2. we have created a method timedifference(), inside which we have pasted the TaskA.py code
3. We are importing flsk  and jesonify for this task
4. in @app.route('/'), we are mentioning the method name which is timedifference and then / and then we are telling python that in the url, we need to provide an interger named n
5. Then inside the method at last, we are returning the result of the taskA.py to see the result 
6. Then we should write the following ode in the terminal: python taskB.py
7. We will see the localhost url, where the code will be run
8. We need to go to the url and then write /1(the value of the n)
9. Then the we will be asked to provide the timestamps and the code will return the difference between two timestamps 