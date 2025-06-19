from playsound import playsound
question=["Q1. How many days are there in a leap year? ","Q2. Which planet is known as the \"Red Planet\"?",
   "Q3. The famous Konark Sun Temple is located in which state?","Q4. How many seats are there in the Lok Sabha of India?",
   "Q5. Who was the first woman to win a Nobel Prize?"]

option=["A. 364 B. 365 C. 366 D. 367","A. Venus B. Earth C. Jupiter D. Mars","A. Odisha  B. Gujarat C. Tamil Nadu D. Rajasthan",
        "A. 545 B. 250 C. 500 D. 600","A. Mother Teresa B. Marie Curie  C. Rosalind Franklin D. Indira Gandhi"
        ]
answers=["c","d","a","a","b"]
winning=[1000,2000,3000,5000,10000]
sum=0
for i in range(len(question)):
    playsound("kbc-question.mp3")
    print(question [i])
    print(option[i])
    a=input("enter the option a/b/c/d \n").lower()
    if a in ("a","b","c","d"):
        if(answers[i]==a):
            print("congratulations you have won ",winning[i])
            sum=sum+winning[i]
            print("you have won total winning of ₹",sum)
        else:
            print("sorry wrong answer \n But you played well")
            print("Your winning amount is ₹",sum)
            print("the correct answer is ",answers[i])
            break
    else:
        print("invalid input. Please enter a,b,c,d")        
        break