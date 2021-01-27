Readme on TaskC

1. Create a new text file named Dockerfile
2. Go to Docker Hub and search for base python image for your project nad get that image 
3. For example- we are going to use the python image which I have mentioned inside the Dockerfile
4. Mention the working directory inside Docker virtual environemnt
5. Copy all fileswith COPY command 
6. pipinsall all the important libraries. 
7. Write pip install to go through the requirements file to install all the necessary libraries
8. Now write the CMD command file to run the taskB file 
9. Now rename the file of Dockerfile by removing the .txt extension and making it an actual docker file
10. Now open the Windwos Power Shell on the computer  
11. Write this command and pres ENTER: docker build -t 'secondtask' .
12. This command will look for a docker file inside the directory 
13. While executing this command, python will be downloaded and all the mentioned ones
14. Write ths command to see the available images: docker images
15. To Run write this command in secondtask container and press enter: docker run -ti secondtask
16. Successfully run. We will be able to see the result of the code on the Power Shell 
17. Thus we can create another image with this command "docker build -t 'secondtask2' ." and run our taskB.py


